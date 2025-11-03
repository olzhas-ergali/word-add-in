from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from enum import Enum


class KeyCloakToken(BaseModel):
    """KeyCloak authentication token response"""
    
    access_token: str = Field(..., description="JWT access token")
    expires_in: int = Field(..., description="Token expiration time in seconds")
    refresh_expires_in: int = Field(..., description="Refresh token expiration time in seconds")
    refresh_token: str = Field(..., description="Refresh token for obtaining new access tokens")
    token_type: str = Field(default="Bearer", description="Token type")
    id_token: Optional[str] = Field(None, description="OpenID Connect ID token")
    not_before_policy: int = Field(default=0, alias="not-before-policy")
    session_state: Optional[UUID] = Field(None, description="Session state UUID")
    scope: str = Field(default="openid", description="Token scope")
    
    class Config:
        populate_by_name = True


class KeyCloakError(BaseModel):
    """KeyCloak error response"""
    
    error: str = Field(..., description="Error code")
    error_description: str = Field(..., description="Detailed error description")


class KeyCloakResponse(BaseModel):
    """Unified KeyCloak API response"""
    
    data: Optional[KeyCloakToken] = Field(None, description="Token data if successful")
    error: Optional[str] = Field(None, description="Error code if failed")
    error_description: Optional[str] = Field(None, description="Error description if failed")
    success: bool = Field(..., description="Whether the request was successful")
    status_code: int = Field(..., description="HTTP status code")
    
    @property
    def message(self) -> Optional[str]:
        """Get localized error message"""
        if self.success:
            return None
        
        error_messages = {
            ("invalid_grant", "Invalid user credentials"): "Неверный логин или пароль.",
            ("invalid_grant", "Token is not active"): "Токен не активен.",
            ("invalid_grant", "Invalid refresh token"): "Недействительный рефреш токен.",
            ("invalid_grant", "Session not active"): "Сессия пользователя не активна.",
            ("invalid_grant", "Code not valid"): "Недействительный код.",
            ("invalid_grant", "Stale token"): "Устаревший токен.",
            ("invalid_request", "Missing form parameter"): "Отсутствует один или несколько параметров атрибута 'form' запроса.",
            ("invalid_request", "Missing parameter"): "Отсутствует один или несколько параметров запроса.",
            ("invalid_request", "No refresh token"): "Рефреш не возвращен и сессия пользователя не создана.",
            ("unauthorized_client", "Invalid client credentials"): "Неверный логин или пароль клиента.",
            ("unauthorized_client", "Invalid client secret"): "Невалидный секрет клиента.",
            ("unauthorized_client", "Client secret not provided in request"): "Секрет клиента не был предоставлен в запросе.",
            ("unsupported_grant_type", "Unsupported grant_type"): "Неподдерживаемый тип гранта.",
            ("response-deserialization-failed", "response-deserialization-failed"): "Произошла ошибка во время десериализации.",
            ("invalid_scope", None): "Невалидный scope.",
            ("Could not find role", None): "Не найдена роль.",
            ("User not found", None): "Учетная запись не найдена.",
            (None, "Invalid email address."): "Неверный адрес электронной почты.",
        }
        
        message = error_messages.get((self.error, self.error_description))
        if message:
            return message
        
        return f"{self.error or ''} {self.error_description or ''}".strip()

