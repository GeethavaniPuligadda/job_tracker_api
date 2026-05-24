from database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,Enum,Date
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
    jobs=relationship("Jobs",back_populates="applier")

class Jobs(Base):
    __tablename__="jobs"
    id=Column(Integer,primary_key=True,index=True)
    company_name=Column(String)
    job_role=Column(String)
    job_url=Column(String)
    job_status=Column(Enum("applied","interview","rejected","selected",name="job_status"),default="applied")
    applied_date=Column(Date)
    user_id=Column(Integer,ForeignKey("users.id"))
    applier=relationship("User",back_populates="jobs")
    


