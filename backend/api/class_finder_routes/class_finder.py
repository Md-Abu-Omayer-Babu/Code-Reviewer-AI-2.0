import os
from fastapi import APIRouter
from ...services.file_reader import FileReader
from ...services.class_finder import ClassFinder
from backend.security.oauth2 import get_current_active_user
from fastapi import Depends

router = APIRouter(
    prefix="/class_finding",
    tags=["class_finding_operations"],
    dependencies=[Depends(get_current_active_user)]
)

uploaded_dir = './db'

if not os.path.isdir(uploaded_dir):
    os.makedirs(uploaded_dir)

@router.get("/")
async def class_finder_route_testing():
    """
    Test endpoint to verify the class finder API is working.
    
    Returns:
        dict: A message indicating the API is working
    """
    return {"message": "Class finder APIs are working!"}

# class finder
@router.get("/get_classes/{filename}")
async def class_finder(filename: str):
    """
    Find all classes in a Python file.
    
    Args:
        filename (str): The name of the file to analyze
        
    Returns:
        dict: A dictionary containing a list of all class names found in the file
        
    Raises:
        HTTPException: If the file is not found (404) or not a Python file (400)
    """
    content = FileReader.read_file(filename, uploaded_dir)
    classes = ClassFinder.find_classes(content)
    return {"classes": classes}
