import httpx
from typing import Optional
from app.config import settings
from app.models.keycloak import KeyCloakToken, KeyCloakResponse, KeyCloakError


class KeyCloakService:
    """Service for KeyCloak authentication"""
    
    def __init__(self):
        self.client_api = settings.keycloak_client_api
        self.client_id = settings.keycloak_client_id
        self.client_secret = settings.keycloak_client_secret
    
    async def validate_user(self, username: str, password: str) -> KeyCloakResponse:
        """
        Authenticate user with KeyCloak
        
        Args:
            username: User's username or email
            password: User's password
            
        Returns:
            KeyCloakResponse with token data or error
        """
        # ДЕМО-РЕЖИМ: Принимаем любые учетные данные
        from app.config import settings
        from uuid import uuid4
        if settings.demo_mode:
            print(f"🎭 DEMO MODE: Accepting login for user '{username}'")
            # Возвращаем фейковый токен для демо-режима
            demo_token = KeyCloakToken(
                access_token="demo_access_token_" + username,
                expires_in=3600,
                refresh_expires_in=7200,
                refresh_token="demo_refresh_token",
                token_type="Bearer",
                session_state=uuid4()  # Генерируем валидный UUID для session
            )
            return KeyCloakResponse(
                success=True,
                status_code=200,
                data=demo_token,
                message=f"Demo mode: authenticated as {username}"
            )
        
        # Обычный режим с реальным KeyCloak
        data = {
            "grant_type": "password",
            "scope": "openid",
            "username": username,
            "password": password,
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self.client_api,
                    data=data,
                    headers={"Content-Type": "application/x-www-form-urlencoded"}
                )
                
                return await self._process_response(response)
                
        except httpx.HTTPError as e:
            return KeyCloakResponse(
                success=False,
                status_code=500,
                error="connection_error",
                error_description=str(e)
            )
    
    async def _process_response(self, response: httpx.Response) -> KeyCloakResponse:
        """Process KeyCloak API response"""
        
        status_code = response.status_code
        success = response.is_success
        
        # Handle server errors (5xx)
        if status_code >= 500:
            return KeyCloakResponse(
                success=False,
                status_code=status_code,
                error="server_error",
                error_description=response.text
            )
        
        # Handle client errors (4xx)
        if status_code >= 400:
            try:
                error_data = response.json()
                return KeyCloakResponse(
                    success=False,
                    status_code=status_code,
                    error=error_data.get("error"),
                    error_description=error_data.get("error_description")
                )
            except Exception:
                return KeyCloakResponse(
                    success=False,
                    status_code=status_code,
                    error="unknown_error",
                    error_description=response.text
                )
        
        # Handle success (2xx)
        try:
            token_data = KeyCloakToken(**response.json())
            return KeyCloakResponse(
                success=True,
                status_code=status_code,
                data=token_data
            )
        except Exception as e:
            return KeyCloakResponse(
                success=False,
                status_code=status_code,
                error="deserialization_error",
                error_description=f"Failed to parse token: {str(e)}"
            )

