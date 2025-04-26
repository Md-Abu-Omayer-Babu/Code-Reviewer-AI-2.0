import os
from fastapi import APIRouter

from backend.services.file_reader import FileReader
from backend.services.function_under_class import ClassFunctionFinder
from backend.services.function_finder import FunctionFinder

router = APIRouter(
    prefix = "/functions",
    tags = ["function_operation"]
)

uploaded_dir = './db'

if not os.path.isdir(uploaded_dir):
    os.makedirs(uploaded_dir)


# all functions
@router.get("/get_functions/{filename}")
async def function_finder(filename: str):
    content = FileReader.read_file(filename, uploaded_dir)
    functions = FunctionFinder.find_functions(content)
    return {"functions": functions}
    
# functions under class
@router.get("/get_functions_under_classes/{filename}")
async def function_under_classes(filename: str):
    content = FileReader.read_file(filename, uploaded_dir)
    functions = ClassFunctionFinder.find_functions_by_class(content)
    return {"functions_under_classes": functions}