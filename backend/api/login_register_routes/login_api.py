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
from ...services.crud_user import getUserByUsername


router = APIRouter(
    prefix="/login",
    tags=["login_operations"]
)

@router.post("/")
async def login(username: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(username, password, db)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/get-user-by-username")
async def getUser(username: str, password: str, db: Session = Depends(get_db), current_user: UserInDB = Depends(get_current_active_user)):
    user = getUserByUsername(username, password, db=db)
    if not user:
        return {"message": "Invalid username or password"}
    return user
