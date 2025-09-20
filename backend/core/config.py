"""
Application configuration settings.

This module contains configuration classes and settings for the application,
including database settings, security settings, and environment-specific configurations.
"""

import os
from typing import List, Optional
from pydantic import BaseSettings, Field


class DatabaseSettings(BaseSettings):
    """Database configuration settings."""
    
    url: str = Field(
        default="sqlite:///User.db",
        env="DATABASE_URL",
        description="Database connection URL"
    )
    echo: bool = Field(
        default=False,
        env="DATABASE_ECHO",
        description="Enable SQLAlchemy query logging"
    )
    connect_args: dict = Field(
        default_factory=lambda: {"check_same_thread": False},
        description="Additional database connection arguments"
    )

    class Config:
        env_file = ".env"
        env_prefix = "DATABASE_"


class SecuritySettings(BaseSettings):
    """Security configuration settings."""
    
    secret_key: str = Field(
        default="your-secret-key-here",
        env="SECRET_KEY",
        description="Secret key for JWT token generation"
    )
    algorithm: str = Field(
        default="HS256",
        env="JWT_ALGORITHM",
        description="JWT algorithm"
    )
    access_token_expire_minutes: int = Field(
        default=30,
        env="ACCESS_TOKEN_EXPIRE_MINUTES",
        description="Access token expiration time in minutes"
    )
    
    class Config:
        env_file = ".env"
        env_prefix = "SECURITY_"


class CORSSettings(BaseSettings):
    """CORS configuration settings."""
    
    allow_origins: List[str] = Field(
        default=["*"],
        env="CORS_ALLOW_ORIGINS",
        description="Allowed CORS origins"
    )
    allow_credentials: bool = Field(
        default=True,
        env="CORS_ALLOW_CREDENTIALS",
        description="Allow credentials in CORS requests"
    )
    allow_methods: List[str] = Field(
        default=["*"],
        env="CORS_ALLOW_METHODS",
        description="Allowed HTTP methods for CORS"
    )
    allow_headers: List[str] = Field(
        default=["*"],
        env="CORS_ALLOW_HEADERS",
        description="Allowed headers for CORS"
    )

    class Config:
        env_file = ".env"
        env_prefix = "CORS_"


class FileSettings(BaseSettings):
    """File handling configuration settings."""
    
    upload_dir: str = Field(
        default="uploads",
        env="UPLOAD_DIR",
        description="Base directory for file uploads"
    )
    max_file_size: int = Field(
        default=10 * 1024 * 1024,  # 10MB
        env="MAX_FILE_SIZE",
        description="Maximum file size in bytes"
    )
    allowed_extensions: List[str] = Field(
        default=[".py"],
        env="ALLOWED_EXTENSIONS",
        description="Allowed file extensions"
    )

    class Config:
        env_file = ".env"
        env_prefix = "FILE_"


class AppSettings(BaseSettings):
    """Main application configuration settings."""
    
    title: str = Field(
        default="Code Reviewer AI Backend",
        env="APP_TITLE",
        description="Application title"
    )
    description: str = Field(
        default="A clean, OOP-structured FastAPI backend for code review operations",
        env="APP_DESCRIPTION",
        description="Application description"
    )
    version: str = Field(
        default="2.0.0",
        env="APP_VERSION",
        description="Application version"
    )
    debug: bool = Field(
        default=False,
        env="DEBUG",
        description="Enable debug mode"
    )
    environment: str = Field(
        default="development",
        env="ENVIRONMENT",
        description="Application environment"
    )

    class Config:
        env_file = ".env"


class Settings:
    """
    Main settings class that combines all configuration sections.
    
    This class provides a centralized way to access all application settings
    with proper typing and validation.
    """
    
    def __init__(self):
        """Initialize all settings sections."""
        self.app = AppSettings()
        self.database = DatabaseSettings()
        self.security = SecuritySettings()
        self.cors = CORSSettings()
        self.file = FileSettings()
    
    @property
    def is_development(self) -> bool:
        """Check if application is running in development mode."""
        return self.app.environment.lower() == "development"
    
    @property
    def is_production(self) -> bool:
        """Check if application is running in production mode."""
        return self.app.environment.lower() == "production"
    
    @property
    def is_testing(self) -> bool:
        """Check if application is running in testing mode."""
        return self.app.environment.lower() == "testing"


# Global settings instance
settings = Settings()


def get_settings() -> Settings:
    """
    Get application settings instance.
    
    This function can be used as a FastAPI dependency to inject
    settings into route handlers and services.
    
    Returns:
        Settings instance
    """
    return settings