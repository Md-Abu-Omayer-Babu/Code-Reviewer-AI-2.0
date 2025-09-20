"""
File controller for handling file-related HTTP requests.

This module provides the FileController class that handles all HTTP requests
related to file operations and coordinates with the FileService.
"""

from typing import List, Dict, Any
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, status
from sqlalchemy.orm import Session

from .base_controller import BaseController
from .auth_controller import get_current_active_user
from ..services.file_service import FileService
from ..models.userInAlchemy import UserInAlchemy
from ..database.database import get_db


class FileController(BaseController[FileService]):
    """
    Controller class for file-related HTTP operations.
    
    This class handles all HTTP requests related to file management
    and coordinates with the FileService for business logic.
    """
    
    def __init__(self, file_service: FileService):
        """
        Initialize the file controller.
        
        Args:
            file_service: Service for file business logic
        """
        super().__init__(file_service)
        self.router = APIRouter(
            prefix="/files",
            tags=["file_operations"],
            dependencies=[Depends(get_current_active_user)]
        )
        self._setup_routes()
    
    def _setup_routes(self):
        """Set up the routes for this controller."""
        
        @self.router.get("/", response_model=Dict[str, List[str]])
        async def get_all_files(
            current_user: UserInAlchemy = Depends(get_current_active_user)
        ):
            """
            Get all files for the current user.
            
            Args:
                current_user: Current authenticated user
                
            Returns:
                Dictionary containing list of filenames
            """
            file_service = FileService()
            return file_service.get_user_files(current_user.username)
        
        @self.router.post("/upload", response_model=Dict[str, Any])
        async def upload_files(
            files: List[UploadFile] = File(...),
            current_user: UserInAlchemy = Depends(get_current_active_user)
        ):
            """
            Upload multiple Python files.
            
            Args:
                files: List of files to upload
                current_user: Current authenticated user
                
            Returns:
                Upload success message and count
            """
            if not files:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="No files provided"
                )
            
            file_service = FileService()
            return file_service.upload_files(files, current_user.username)
        
        @self.router.get("/{filename}", response_model=Dict[str, Any])
        async def get_file_content(
            filename: str,
            current_user: UserInAlchemy = Depends(get_current_active_user)
        ):
            """
            Get the content of a specific file.
            
            Args:
                filename: Name of the file to retrieve
                current_user: Current authenticated user
                
            Returns:
                File content and metadata
            """
            file_service = FileService()
            return file_service.get_file_content(filename, current_user.username)
        
        @self.router.delete("/{filename}", response_model=Dict[str, str])
        async def delete_file(
            filename: str,
            current_user: UserInAlchemy = Depends(get_current_active_user)
        ):
            """
            Delete a specific file.
            
            Args:
                filename: Name of the file to delete
                current_user: Current authenticated user
                
            Returns:
                Deletion success message
            """
            file_service = FileService()
            return file_service.delete_file(filename, current_user.username)
        
        @self.router.post("/validate", response_model=Dict[str, bool])
        async def validate_file(filename: str):
            """
            Validate if a filename represents a Python file.
            
            Args:
                filename: Name of the file to validate
                
            Returns:
                Validation result
            """
            file_service = FileService()
            is_valid = file_service.validate_file(filename)
            
            return {
                "filename": filename,
                "is_valid_python": is_valid
            }


def get_file_controller() -> FileController:
    """
    Dependency to get file controller with injected dependencies.
    
    Returns:
        FileController instance
    """
    file_service = FileService()
    return FileController(file_service)