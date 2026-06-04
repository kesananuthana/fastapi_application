from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from .database import *
from .models import *

app=FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/persons")
def getpersons(db:Session= Depends(get_db)):
    persons = db.query(Person).all()
    return {"data":persons}
