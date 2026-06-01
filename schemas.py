from pydantic import BaseModel
from datetime import date
from typing import Optional
class user(BaseModel):
    name:str
    email:str
    password:str
class job(BaseModel):
    company_name:str
    job_role:str
    job_url:Optional[str]
    job_status:str
    applied_date:Optional[date]
    user_id:int
class showuser(BaseModel):
    name:str
    email:str
    class config:
        orm_mode=True
class updatejob(BaseModel):
    job_status:str
class showjob(BaseModel):
    company_name:str
    job_role:str
    job_status:str
    user_id:int
    class config:
        orm_mode=True
class Tokendata(BaseModel):
    email:str
    