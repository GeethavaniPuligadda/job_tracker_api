from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
from typing import List
import schemas,models
from hashing import Hash
from database import get_db
router=APIRouter(prefix="/user",tags=["user"])

@router.post("/user")
def post_user(request:schemas.user,db:Session=Depends(get_db)):
    new_user=models.User(name=request.name,email=request.email,password=Hash.hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
@router.get("/",response_model=List[schemas.showuser])
def get_user(db:Session=Depends(get_db)):
    return db.query(models.User).all()
@router.get("/{id}",response_model=schemas.showuser)
def getone_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    return user