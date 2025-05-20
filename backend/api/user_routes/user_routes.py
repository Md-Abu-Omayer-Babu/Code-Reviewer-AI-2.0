from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from fastapi import Depends

from ...database.database import get_db
from ...models.user import UserInDB
from ...security.oauth2 import create_access_token
from ...security.oauth2 import get_current_active_user
from ...security.auth import authenticate_user
from ...models.userInAlchemy import UserInAlchemy
from ...models.user import User, UserInDB
from ...services.crud_user import getUserByUsername

router = APIRouter(
    prefix="/user",
    tags=["user_operations"]
)

@router.get("/get-user")
async def get_user(current_user: UserInAlchemy = Depends(get_current_active_user)):
    return {
        "username": current_user.username,
        "email": current_user.email,
        "fullname": current_user.full_name,
        "hashed_password": current_user.hashed_password
    }
    
@router.post("/get-user")
async def getUser(username: str, password: str, db: Session = Depends(get_db), current_user: UserInDB = Depends(get_current_active_user)):
    user = getUserByUsername(username, password, db=db)
    if not user:
        return {"message": "Invalid username or password"}
    return user