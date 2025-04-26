import os
from fastapi import APIRouter
from ...services.file_reader import FileReader
from ...services.class_finder import ClassFinder

router = APIRouter(
    prefix="/class_finding",
    tags=["class_finding_operations"]
)

uploaded_dir = './db'

if not os.path.isdir(uploaded_dir):
    os.makedirs(uploaded_dir)

@router.get("/")
async def class_finder_route_testing():
    return {"message": "Class finder APIs are working!"}

# class finder
@router.get("/get_classes/{filename}")
async def class_finder(filename: str):
    content = FileReader.read_file(filename, uploaded_dir)
    classes = ClassFinder.find_classes(content)
    return {"classes": classes}
