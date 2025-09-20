"""
Request and response schemas for the API.

This module contains Pydantic models for API request and response validation,
separated from database models to follow clean architecture principles.
"""

from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field


# User-related schemas
class UserBase(BaseModel):
    """Base user schema with common fields."""
    username: str = Field(..., min_length=3, max_length=50, description="Username")
    email: Optional[EmailStr] = Field(None, description="User email address")
    full_name: Optional[str] = Field(None, max_length=100, description="Full name")


class UserCreate(UserBase):
    """Schema for user creation requests."""
    password: str = Field(..., min_length=6, description="User password")


class UserUpdate(BaseModel):
    """Schema for user update requests."""
    email: Optional[EmailStr] = Field(None, description="Updated email address")
    full_name: Optional[str] = Field(None, max_length=100, description="Updated full name")


class UserResponse(UserBase):
    """Schema for user response data."""
    disabled: bool = Field(default=False, description="Whether user is disabled")
    
    class Config:
        from_attributes = True


class UserInDBResponse(UserResponse):
    """Schema for user data including database metadata."""
    hashed_password: str
    
    class Config:
        from_attributes = True


# Authentication-related schemas
class LoginRequest(BaseModel):
    """Schema for login requests."""
    username: str = Field(..., description="Username")
    password: str = Field(..., description="Password")


class TokenResponse(BaseModel):
    """Schema for token responses."""
    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field(default="bearer", description="Token type")


class TokenData(BaseModel):
    """Schema for token data validation."""
    username: Optional[str] = Field(None, description="Username from token")


# File-related schemas
class FileInfo(BaseModel):
    """Schema for file information."""
    filename: str = Field(..., description="Name of the file")
    size: Optional[int] = Field(None, description="File size in bytes")
    is_python: bool = Field(default=True, description="Whether file is a Python file")


class FileContentResponse(BaseModel):
    """Schema for file content responses."""
    filename: str = Field(..., description="Name of the file")
    content: str = Field(..., description="File content")
    size: int = Field(..., description="Content size in bytes")


class FileUploadResponse(BaseModel):
    """Schema for file upload responses."""
    message: str = Field(..., description="Upload status message")
    count: int = Field(..., description="Number of files uploaded")
    files: Optional[List[str]] = Field(None, description="List of uploaded filenames")


class FileDeleteResponse(BaseModel):
    """Schema for file deletion responses."""
    message: str = Field(..., description="Deletion status message")
    filename: str = Field(..., description="Name of deleted file")


class FilesListResponse(BaseModel):
    """Schema for files list responses."""
    files: List[str] = Field(..., description="List of filenames")
    count: int = Field(..., description="Number of files")


class FileValidationResponse(BaseModel):
    """Schema for file validation responses."""
    filename: str = Field(..., description="Name of the file")
    is_valid_python: bool = Field(..., description="Whether file is valid Python")


# Error response schemas
class ErrorResponse(BaseModel):
    """Schema for error responses."""
    detail: str = Field(..., description="Error message")
    error_code: Optional[str] = Field(None, description="Error code")


class ValidationErrorResponse(BaseModel):
    """Schema for validation error responses."""
    detail: List[dict] = Field(..., description="Validation error details")


# Success response schemas
class SuccessResponse(BaseModel):
    """Schema for general success responses."""
    message: str = Field(..., description="Success message")
    data: Optional[dict] = Field(None, description="Additional response data")


# Health check schema
class HealthCheckResponse(BaseModel):
    """Schema for health check responses."""
    status: str = Field(..., description="Application status")
    database: str = Field(..., description="Database status")
    version: str = Field(..., description="Application version")