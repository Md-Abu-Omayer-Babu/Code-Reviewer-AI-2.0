import os
from fastapi import APIRouter

from backend.services.file_reader import FileReader
from backend.services.function_under_class import functionUnderClass
from backend.services.function_finder import functionFinder

router = APIRouter(
    prefix = "/functions",
    tags = ["function_operation"]
)

uploaded_dir = './db'

if not os.path.isdir(uploaded_dir):
    os.makedirs(uploaded_dir)


# all classes
@router.get("/get_functions/{filename}")
async def function_finder(filename: str):
    content = FileReader(filename, uploaded_dir)
    functions = functionFinder(content)
    return {"functions": functions}
    
# functions under class
@router.get("/get_functions_under_classes/{filename}")
async def function_under_classes(filename: str):
    content = FileReader(filename, uploaded_dir)
    functions = functionUnderClass(content)
    return {"functions_under_classes": functions}