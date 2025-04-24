import os
from fastapi import APIRouter

from backend.services.comment_finder import commentFinder
from backend.services.file_reader import FileReader


router = APIRouter(
    prefix="/comments_finding",
    tags=["comments_finding_operations"]
)

uploaded_dir = './db'

if not os.path.isdir(uploaded_dir):
    os.makedirs(uploaded_dir)
     
@router.get("/root")
async def comments_finder_route_root():
    return {"message": "Comments finder routes is working...."}

@router.get("/get_comments/{filename}")
async def comments_finder(filename: str):
    content = FileReader(filename, uploaded_dir)
    comments = commentFinder(content)
    return {"comments": comments}