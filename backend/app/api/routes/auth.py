from fastapi import APIRouter, HTTPException, Header
from typing import Optional
from uuid import uuid4
from app.models.keycloak import KeyCloakResponse
from app.models.requests import LoginRequest
from app.services.keycloak_service import KeyCloakService
from app.services.cache_service import cache_service

router = APIRouter()


@router.post("/login", response_model=KeyCloakResponse)
async def login(request: LoginRequest):
    """
    Authenticate user with KeyCloak
    
    Args:
        request: Login credentials (username and password)
        
    Returns:
        KeyCloakResponse with token data or error
    """
    keycloak_service = KeyCloakService()
    
    response = await keycloak_service.validate_user(
        username=request.username,
        password=request.password
    )
    
    if not response.success:
        raise HTTPException(
            status_code=response.status_code,
            detail={
                "error": response.error,
                "error_description": response.error_description,
                "message": response.message
            }
        )
    
    # Generate session ID and cache token
    session_id = str(uuid4())
    if response.data:
        cache_service.cache_token(session_id, response.data)
    
    # Add session_id to response for client to use in subsequent requests
    return {
        **response.model_dump(),
        "session_id": session_id
    }


@router.post("/logout")
async def logout(session_id: Optional[str] = Header(None, alias="X-Session-ID")):
    """
    Logout user and clear cached token
    
    Args:
        session_id: Session ID from header
        
    Returns:
        Success message
    """
    if session_id:
        cache_service.remove_token(session_id)
    
    return {"success": True, "message": "Logged out successfully"}


@router.get("/validate")
async def validate_session(session_id: Optional[str] = Header(None, alias="X-Session-ID")):
    """
    Validate if session is still active
    
    Args:
        session_id: Session ID from header
        
    Returns:
        Validation result
    """
    if not session_id:
        return {"valid": False, "message": "No session ID provided"}
    
    token = cache_service.get_token(session_id)
    
    if not token:
        return {"valid": False, "message": "Session expired or not found"}
    
    return {"valid": True, "message": "Session is valid"}

