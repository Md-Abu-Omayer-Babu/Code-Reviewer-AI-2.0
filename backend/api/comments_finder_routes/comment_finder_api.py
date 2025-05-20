import os
from fastapi import APIRouter

from backend.services.comment_finder import CommentFinder
from backend.services.file_reader import FileReader
from backend.security.oauth2 import get_current_active_user
from fastapi import Depends

router = APIRouter(
    prefix="/comments_finding",
    tags=["comments_finding_operations"],
    dependencies=[Depends(get_current_active_user)]
)

uploaded_dir = './db'

if not os.path.isdir(uploaded_dir):
    os.makedirs(uploaded_dir)
     
@router.get("/root")
async def comments_finder_route_root():
    """
    Test endpoint to verify the comments finder API is working.
    
    Returns:
        dict: A message indicating the API is working
    """
    return {"message": "Comments finder routes is working...."}

@router.get("/get_comments/{filename}")
async def comments_finder(filename: str):
    """
    Find all comments in a Python file.
    
    Args:
        filename (str): The name of the file to analyze
        
    Returns:
        dict: A dictionary containing all comments found in the file
        
    Raises:
        HTTPException: If the file is not found (404) or not a Python file (400)
    """
    content = FileReader.read_file(filename, uploaded_dir)
    comments = CommentFinder.find_comments(content)
    return {"comments": comments}