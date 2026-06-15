from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from .database import *
from .models import *

router = APIRouter()

Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/persons")
def getpersons(db:Session= Depends(get_db)):
    persons = db.query(Person).all()
    return {"data":persons}
