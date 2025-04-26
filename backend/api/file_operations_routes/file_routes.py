from ast import List
import os
from fastapi import APIRouter, File, HTTPException, UploadFile

from backend.services.delete_file import FileDeleter
from backend.services.file_writer import FileWriter
from backend.services.check_validation import FileValidator
from backend.services.file_reader import FileReader
from backend.services.path_finder import PathFinder

router = APIRouter(
    prefix="/files",
    tags=["files_operations"]
)

uploaded_dir = 'db'

if not os.path.isdir(uploaded_dir):
    os.mkdir(uploaded_dir)

@router.get("/test_api")
async def test_api():
    return {"message": "This Test API is working!"}

@router.get("/get_all_files")
async def all_files():
    return {"files": os.listdir(uploaded_dir)}

# multiple file upload
@router.post("/upload")
async def upload_files(files: list[UploadFile]):
    for file in files:
        if FileValidator.isPython(file.filename):
            file_path = PathFinder.find_path(file.filename, uploaded_dir)
            message = FileWriter.write_file(file_path, file)
            return message
        else:
            raise HTTPException(status_code=400, detail="File is not a python file")

# get contents
@router.get("/get_contents/{file_name}")
async def get_file_contents(file_name: str):
    return {"content": FileReader.read_file(file_name, uploaded_dir)}

# delete file
@router.delete("/delete/{file_name}")
async def delete_file(file_name: str):
    file_path = PathFinder.find_path(file_name, uploaded_dir)
    message = FileDeleter.delete_file(file_path)
    return message