"""
Token models for authentication.

This module contains Pydantic models for JWT token handling and validation.
"""

from typing import Optional
from pydantic import BaseModel, Field


class Token(BaseModel):
    """
    Token model for JWT authentication responses.
    
    This model represents the structure of authentication tokens
    returned to clients after successful login.
    """
    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field(default="bearer", description="Token type")

    class Config:
        """Pydantic configuration."""
        json_schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "token_type": "bearer"
            }
        }


class TokenData(BaseModel):
    """
    Token data model for JWT payload validation.
    
    This model represents the data extracted from JWT tokens
    for user identification and authorization.
    """
    username: Optional[str] = Field(None, description="Username from token payload")

    class Config:
        """Pydantic configuration."""
        json_schema_extra = {
            "example": {
                "username": "john_doe"
            }
        }