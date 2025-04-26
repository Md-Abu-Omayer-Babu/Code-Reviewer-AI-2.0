from fastapi import APIRouter, Form
from typing import Annotated
from pydantic import BaseModel
from ...services.email_validation_check import EmailValidator

router = APIRouter(
    prefix="/login",
    tags=["login_operations"]
)

class FormData(BaseModel):
    email: str
    password: str

@router.get("/root")
async def login_api_testing():
    return {"message": "Login api working..."}

@router.post("/login_api")
async def login(data: Annotated[FormData, Form()]):
    if EmailValidator.is_valid_email(data.email):
        return data
    return {"message": "Invalid email"}

