from fastapi import HTTPException

from .check_validation import isPython
from .path_finder import PathFinder


def FileReader(file_name, uploaded_dir):
    file_path = PathFinder(file_name, uploaded_dir)
    try:
        if not isPython(file_name):
            raise HTTPException(status_code=400, detail="File is not a python file")
        else:
            with open(file_path, "r") as file:
                content = file.read()
                return content
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")