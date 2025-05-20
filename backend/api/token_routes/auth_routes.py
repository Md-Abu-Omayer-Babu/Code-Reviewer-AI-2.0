from fastapi import APIRouter
from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

from ...models.token import Token
from ...security.oauth2 import create_access_token
from ...security.auth import authenticate_user
from ...security.oauth2 import get_current_active_user
from ...models.user import User
from ...models.userInAlchemy import UserInAlchemy
from ...database.database import get_db
from ...models.user import UserInDB


router = APIRouter(
    prefix="/token",
    tags=["token_operations"]
)

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30


@router.post("/")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(get_db)],
) -> Token:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/me", response_model=UserInDB)
async def read_users_me(
    current_user: Annotated[UserInAlchemy, Depends(get_current_active_user)],
):
    return current_user