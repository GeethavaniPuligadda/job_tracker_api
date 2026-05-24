from fastapi import FastAPI
from database import engine
import models
from routers import user,job,login

app=FastAPI()


models.Base.metadata.create_all(bind=engine)
app.include_router(login.router)
app.include_router(user.router)
app.include_router(job.router)




