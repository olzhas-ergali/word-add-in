from pydantic import BaseModel, Field
from typing import List
from uuid import UUID


class LoginRequest(BaseModel):
    """User login request"""
    
    username: str = Field(..., min_length=1, description="Username or email")
    password: str = Field(..., min_length=1, description="User password")


class VariableValuesRequest(BaseModel):
    """Request for getting variable values by IDs"""
    
    ids: List[str] = Field(..., min_items=1, description="List of variable IDs")

