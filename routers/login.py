from fastapi import APIRouter,Depends,HTTPException,status
from jose import jwt
from sqlalchemy.orm import Session
import models
from hashing import Hash
from jwt_token import create_access_token
from database import get_db
from fastapi.security import OAuth2PasswordRequestForm
router=APIRouter(tags=["Authentication"])
@router.post("/login")
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credentials")
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid password")
    jwttoken=create_access_token(data={"sub":user.email})
    return {"access_token":jwttoken,"type":'bearer'}

