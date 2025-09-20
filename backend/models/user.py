"""
User models for the application.

This module contains Pydantic models for user data validation and serialization.
These models are used for business logic and API serialization.
"""

from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    """
    User model for general user data.
    
    This model represents user information without sensitive data
    and is used for API responses and business logic.
    """
    username: str = Field(..., min_length=3, max_length=50, description="Unique username")
    email: Optional[EmailStr] = Field(None, description="User email address")
    full_name: Optional[str] = Field(None, max_length=100, description="User's full name")
    disabled: Optional[bool] = Field(default=False, description="Whether user is disabled")

    class Config:
        """Pydantic configuration."""
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "john_doe",
                "email": "john@example.com",
                "full_name": "John Doe",
                "disabled": False
            }
        }


class UserInDB(User):
    """
    User model including hashed password for database operations.
    
    This model extends the User model to include the hashed password
    for database storage and authentication purposes.
    """
    hashed_password: str = Field(..., description="Hashed password")

    class Config:
        """Pydantic configuration."""
        from_attributes = True