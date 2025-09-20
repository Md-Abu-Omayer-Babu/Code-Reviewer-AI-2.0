"""
File service for handling file-related business logic.

This module provides the FileService class that contains all business logic
related to file operations, including upload, read, delete, and validation.
"""

import os
from typing import List, Dict, Any
from fastapi import HTTPException, UploadFile, status

from .base_service import BaseService
from ..services.check_validation import FileValidator
from ..services.path_finder import PathFinder
from ..services.uploaded_dir import get_user_upload_dir


class FileService(BaseService):
    """
    Service class for file-related business operations.
    
    This class encapsulates all business logic related to file operations,
    including validation, upload, read, and delete operations.
    """
    
    def __init__(self):
        """Initialize the file service."""
        # File service doesn't need a repository as it works with the filesystem
        pass
    
    def get_user_files(self, username: str) -> Dict[str, List[str]]:
        """
        Get all files for a specific user.
        
        Args:
            username: The username to get files for
            
        Returns:
            Dictionary containing list of filenames
            
        Raises:
            HTTPException: If directory doesn't exist or access error
        """
        try:
            uploaded_dir = get_user_upload_dir(username)
            if not os.path.exists(uploaded_dir):
                os.makedirs(uploaded_dir, exist_ok=True)
                return {"files": []}
            
            files = os.listdir(uploaded_dir)
            return {"files": files}
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error accessing user files: {str(e)}"
            )
    
    def upload_files(self, files: List[UploadFile], username: str) -> Dict[str, str]:
        """
        Upload multiple files for a user.
        
        Args:
            files: List of files to upload
            username: Username of the file owner
            
        Returns:
            Success message
            
        Raises:
            HTTPException: If file validation fails or upload error
        """
        try:
            uploaded_dir = get_user_upload_dir(username)
            os.makedirs(uploaded_dir, exist_ok=True)
            
            uploaded_count = 0
            for file in files:
                # Validate file type
                if not FileValidator.isPython(file.filename):
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"File '{file.filename}' is not a Python file"
                    )
                
                # Get file path and write file
                file_path = PathFinder.find_path(file.filename, uploaded_dir)
                self._write_file(file_path, file)
                uploaded_count += 1
            
            return {
                "message": f"Successfully uploaded {uploaded_count} file(s)",
                "count": uploaded_count
            }
            
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error uploading files: {str(e)}"
            )
    
    def get_file_content(self, filename: str, username: str) -> Dict[str, str]:
        """
        Get the content of a specific file.
        
        Args:
            filename: Name of the file to read
            username: Username of the file owner
            
        Returns:
            Dictionary containing file content
            
        Raises:
            HTTPException: If file not found, not Python file, or read error
        """
        try:
            uploaded_dir = get_user_upload_dir(username)
            
            # Validate file type
            if not FileValidator.isPython(filename):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="File is not a Python file"
                )
            
            file_path = PathFinder.find_path(filename, uploaded_dir)
            
            # Check if file exists
            if not os.path.exists(file_path):
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="File not found"
                )
            
            # Read file content
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            
            return {
                "filename": filename,
                "content": content,
                "size": len(content)
            }
            
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error reading file: {str(e)}"
            )
    
    def delete_file(self, filename: str, username: str) -> Dict[str, str]:
        """
        Delete a specific file.
        
        Args:
            filename: Name of the file to delete
            username: Username of the file owner
            
        Returns:
            Success message
            
        Raises:
            HTTPException: If file not found or delete error
        """
        try:
            uploaded_dir = get_user_upload_dir(username)
            file_path = PathFinder.find_path(filename, uploaded_dir)
            
            # Check if file exists
            if not os.path.exists(file_path):
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="File not found"
                )
            
            # Delete file
            os.remove(file_path)
            
            return {
                "message": f"File '{filename}' deleted successfully",
                "filename": filename
            }
            
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error deleting file: {str(e)}"
            )
    
    def validate_file(self, filename: str) -> bool:
        """
        Validate if a file is a Python file.
        
        Args:
            filename: Name of the file to validate
            
        Returns:
            True if file is valid Python file, False otherwise
        """
        return FileValidator.isPython(filename)
    
    def _write_file(self, file_path: str, file: UploadFile) -> None:
        """
        Write uploaded file to disk.
        
        Args:
            file_path: Path where to write the file
            file: Uploaded file object
            
        Raises:
            Exception: If write operation fails
        """
        try:
            with open(file_path, "wb") as buffer:
                content = file.file.read()
                buffer.write(content)
        except Exception as e:
            raise Exception(f"Failed to write file: {str(e)}")
        finally:
            file.file.close()