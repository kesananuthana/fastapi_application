from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from  .database import *
from .models import *

app=FastAPI()
Base.metadata.create_all(bind=engine)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/employee")
def users(db:Session=Depends(get_db)):
    users = db.query(Employee).all()
    return {"data":users}