from ast import List
import os
from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi import Depends
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from backend.services.delete_file import FileDeleter
from backend.services.file_writer import FileWriter
from backend.services.check_validation import FileValidator
from backend.services.file_reader import FileReader
from backend.services.path_finder import PathFinder
from backend.security.oauth2 import get_current_active_user

from ...models.userInAlchemy import UserInAlchemy

router = APIRouter(
    prefix="/files",
    tags=["files_operations"],
    dependencies=[Depends(get_current_active_user)]
)

def get_user_upload_dir(username: str) -> str:
    path = f'uploads/{username}'
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    return path

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def is_valid_token(token: str) -> bool:
    """
    Validate the token. This is a placeholder function.
    
    Args:
        token (str): The token to validate
        
    Returns:
        bool: True if the token is valid, False otherwise
    """
    return True


@router.get("/get_all_files")
async def all_files(current_user: UserInAlchemy = Depends(get_current_active_user)):
    uploaded_dir = get_user_upload_dir(current_user.username)
    """
    Get a list of all files in the uploads directory.
    
    Returns:
        dict: A dictionary containing a list of all filenames
    """
    return {"files": os.listdir(uploaded_dir)}

# multiple file upload
@router.post("/upload")
async def upload_files(
    files: list[UploadFile],
    current_user: UserInAlchemy = Depends(get_current_active_user),
):
    uploaded_dir = get_user_upload_dir(current_user.username)
    
    """
    Upload multiple Python files.
    
    Args:
        files (list[UploadFile]): A list of files to upload
        
    Returns:
        dict: A message indicating the file was uploaded successfully
        
    Raises:
        HTTPException: If the file is not a Python file (400)
    """
    
    for file in files:
        if FileValidator.isPython(file.filename):
            file_path = PathFinder.find_path(file.filename, uploaded_dir)
            message = FileWriter.write_file(file_path, file)
            # return message
        else:
            raise HTTPException(status_code=400, detail="File is not a python file")
    return message

# get contents
@router.get("/get_contents/{file_name}")
async def get_file_contents(
    file_name: str, current_user: UserInAlchemy = Depends(get_current_active_user)
):
    uploaded_dir = get_user_upload_dir(current_user.username)
    """
    Get the contents of a specific file.
    
    Args:
        file_name (str): The name of the file to retrieve
        
    Returns:
        dict: A dictionary containing the file content
        
    Raises:
        HTTPException: If the file is not found (404) or not a Python file (400)
    """
    return {"content": FileReader.read_file(file_name, uploaded_dir)}

# delete file
@router.delete("/delete/{file_name}")
async def delete_file(
    file_name: str, current_user: UserInAlchemy = Depends(get_current_active_user)
):
    uploaded_dir = get_user_upload_dir(current_user.username)
    """
    Delete a specific file.
    
    Args:
        file_name (str): The name of the file to delete
        
    Returns:
        dict: A message indicating the file was deleted successfully
        
    Raises:
        HTTPException: If the file is not found (404) or an error occurs during deletion (500)
    """
    file_path = PathFinder.find_path(file_name, uploaded_dir)
    message = FileDeleter.delete_file(file_path)
    return message