from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import HTTPException
from pydantic import BaseModel
from fastapi import Form
from typing import Annotated

from ...database.database import get_db
from ...models.user import User
from ...models.userInAlchemy import UserInAlchemy
from ...services.crud_user import userCreator



router = APIRouter(
    prefix="/register",
    tags=["register_operations"]
)

class FormData(BaseModel):
    username: str
    email: str
    password: str
    confirmPassword: str

@router.post("/")
async def create_user(payload: Annotated[FormData, Form()], db: Session = Depends(get_db)):
    if payload.password != payload.confirmPassword:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    user = User(username=payload.username, email=payload.email, full_name="")
    userCreator(user, payload.password, payload.email, db=db)
    return {"message": "User created successfully"}
