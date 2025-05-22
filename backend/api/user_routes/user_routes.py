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
from ...security.oauth2 import get_current_active_user
from fastapi import Depends

router = APIRouter(
    prefix="/user",
    tags=["user_operations"],
    dependencies=[Depends(get_current_active_user)]
)

@router.get("/get_current_active_user")
async def get_user(current_user: UserInAlchemy = Depends(get_current_active_user)):
    return {
        "fullname": current_user.full_name,
        "username": current_user.username,
        "email": current_user.email,
        "hashed_password": current_user.hashed_password
    }
    
@router.post("/get-user-by-username")
async def getUser(username: str, password: str, db: Session = Depends(get_db)):
    user = getUserByUsername(username, password, db=db)
    if not user:
        return {"message": "Invalid username or password"}
    return user
