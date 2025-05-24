import os
from fastapi import Depends
from fastapi import APIRouter
from typing import Dict

from ...services.file_reader import FileReader
from ...services.class_finder import ClassFinder
from backend.security.oauth2 import get_current_active_user
from ...services.uploaded_dir import get_user_upload_dir
from ...models.userInAlchemy import UserInAlchemy


router = APIRouter(
    prefix="/class_finding",
    tags=["class_finding_operations"],
    dependencies=[Depends(get_current_active_user)]
)

@router.get("/")
async def class_finder_route_testing():
    """
    Test endpoint to verify the class finder API is working.
    
    Returns:
        dict: A message indicating the API is working
    """
    return {"message": "Class finder APIs are working!"}

# class finder
# @router.get("/get_classes/{filename}")
# async def class_finder(
#     filename: str,
#     current_user: UserInAlchemy = Depends(get_current_active_user),
# ):
#     uploaded_dir = get_user_upload_dir(current_user.username)
#     """
#     Find all classes in a Python file.
    
#     Args:
#         filename (str): The name of the file to analyze
        
#     Returns:
#         dict: A dictionary containing a list of all class names found in the file
        
#     Raises:
#         HTTPException: If the file is not found (404) or not a Python file (400)
#     """
#     content = FileReader.read_file(filename, uploaded_dir)
#     classes = ClassFinder.find_classes(content)
#     return {"classes": classes}

@router.get("/get_classes/{filename}")
async def get_class_inheritance(
    filename: str,
    current_user: UserInAlchemy = Depends(get_current_active_user),
) -> Dict[str, dict]:
    """
    Retrieve all class names and their parent (base) classes from a Python file.

    Args:
        filename (str): The name of the uploaded Python file.
        current_user (UserInAlchemy): The currently authenticated user.

    Returns:
        dict: A dictionary containing class inheritance information.
    """
    uploaded_dir = get_user_upload_dir(current_user.username)
    content = FileReader.read_file(filename, uploaded_dir)
    class_data = ClassFinder.find_classes_with_parents(content)
    return {"classes": class_data}
