from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from  .database import *
from .models import *

router = APIRouter()
Base.metadata.create_all(bind=engine)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/employee")
def users(db:Session=Depends(get_db)):
    users = db.query(Employee).all()
    return {"data":users}

@router.get("/hello")
def user():
    return {"message":"hello world"}