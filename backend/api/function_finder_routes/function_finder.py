import os
from fastapi import APIRouter

from backend.services.file_reader import FileReader
from backend.services.function_under_class import ClassFunctionFinder
from backend.services.function_finder import FunctionFinder
from backend.security.oauth2 import get_current_active_user
from fastapi import Depends
from ...services.uploaded_dir import get_user_upload_dir
from ...models.userInAlchemy import UserInAlchemy

router = APIRouter(
    prefix = "/functions",
    tags = ["function_operation"],
    dependencies=[Depends(get_current_active_user)]
)


# all functions
@router.get("/get_functions/{filename}")
async def function_finder(
    filename: str,
        current_user: UserInAlchemy = Depends(get_current_active_user),
):
    uploaded_dir = get_user_upload_dir(current_user.username)
    """
    Get a list of all functions of a files.

    Args:
        filename (str): The name of the file to analyze

    Returns:
        dict: A dictionary containing a list of all funtion names found in the file
    """
    content = FileReader.read_file(filename, uploaded_dir)
    functions = FunctionFinder.find_functions(content)
    return {"functions": functions}
    
# functions under class
@router.get("/get_functions_under_classes/{filename}")
async def function_under_classes(
    filename: str,
        current_user: UserInAlchemy = Depends(get_current_active_user),
):
    uploaded_dir = get_user_upload_dir(current_user.username)
    """
    Get a list of all functions under all classes of a files.

    Args:
        filename (str): The name of the file to analyze

    Returns:
        dict: A dictionary containing a list of all funtion names under all classes found in the file
    """
    content = FileReader.read_file(filename, uploaded_dir)
    functions = ClassFunctionFinder.find_functions_by_class(content)
    return {"functions_under_classes": functions}