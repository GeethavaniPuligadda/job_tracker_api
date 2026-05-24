from fastapi import Depends,APIRouter,HTTPException,status
from sqlalchemy.orm import Session
from oauth2 import get_current_user
from typing import List
import schemas,models
from database import get_db
router=APIRouter(prefix="/job",tags=["job"])

@router.post("/")
def post_job(request:schemas.job,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    new_job=models.Jobs(company_name=request.company_name,job_role=request.job_role,job_url=request.job_url,job_status=request.job_status,applied_date=request.applied_date,user_id=request.user_id)
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job
@router.get("/",response_model=List[schemas.showjob])
def get_job(current_user=Depends(get_current_user),db:Session=Depends(get_db)):
    return db.query(models.Jobs).all()
@router.get("/{id}",response_model=schemas.showjob)
def getone_job(id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    job= db.query(models.Jobs).filter(models.Jobs.id==id).first()
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Job not found")
    return job
@router.put("/{id}")
def update_job(id:int,request:schemas.updatejob,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    db.query(models.Jobs).filter(models.Jobs.id==id).update(request.dict())
    db.commit()
    return "updated successfully"
@router.delete("/{id}")
def destroy(id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    db.query(models.Jobs).filter(models.Jobs.id==id).delete(synchronize_session=False)
    db.commit()
    return "deleted successfully"

