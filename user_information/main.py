
from fastapi import FastAPI,Depends, HTTPException,requests
from sqlalchemy import inspect, text
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from .database import *
from .models import *
from .crud import *
from .schema import *
import datetime

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get('/add-column')
def add_column(db:Session=Depends(get_db)):
    query=text('Alter table userinfo add Column is_admin Boolean')
    db.execute(query)
    db.commit()
    return {'msg':'column added successfully'}


@app.post('/insert-data')
def create_api(userinfo:UserInformationDetails, db: Session = Depends(get_db)):
    api_created_at = datetime.datetime.utcnow()
    db_userinfo=create_user_info_data(db,userinfo)
    return {"data": db_userinfo, "api_created_at": str(api_created_at)}


@app.get("/users/")
def read_user(db: Session = Depends(get_db)):
    try:
        api_created_at = datetime.datetime.utcnow()
        user = db.query(UserInfo).all()
        if user is None:
            raise HTTPException(status_code=404, detail="No user information")
        return {'title':'User Information','properties':user,"api_created_at": str(api_created_at)}
    except HTTPException as e:
        raise e
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.get("/users/{user_id}")
def read_user(user_id: str, db: Session = Depends(get_db)):
    try:
        user = db.query(UserInfo).filter(UserInfo.user_id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="The ID not found")
        return {'User Information':user}
    except HTTPException as e:
        raise e
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error")


#update details
@app.put("/users/{user_id}/{password}")
def read_user(user_id: str,password:str,db: Session = Depends(get_db)):
    try:
        db_user = db.query(UserInfo).filter(UserInfo.user_id == user_id).first()
        if not db_user:
            raise HTTPException(status_code=404, detail="The ID not found")
        db_user.password_hash=password
        db.commit()
        return {'message':'Updated successfully'}
    except HTTPException as e:
        raise e
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error")



#delete details
@app.delete('/deletedetails/{profile_id}')
def delete_details(profile_id: str, db: Session = Depends(get_db)):
    try:
        deleted_rows = db.query(UserInfo).filter(UserInfo.profile_id == profile_id).delete()

        if deleted_rows == 0:
            raise HTTPException(status_code=404, detail="The ID not found")

        db.commit()
        return {'message': 'Deleted successfully'}

    except HTTPException as e:
        raise e
    except Exception as e:
        # Optional: log the actual error
        print(f"Unexpected error during delete: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    



#insert api response in new table
@app.post('/insertdata-in-new-table')
def insert_data_new_table(db:Session=Depends(get_db)):
    api_created_at = datetime.datetime.utcnow()
    response=requests.get('http://127.0.0.1:8000/users/')
    data=response.json()
    properties=data.get('properties')
    for user_info_data in properties:
        new_user_info=UserInformation(
            user_info_id=user_info_data["user_info_id"],
            user_id=user_info_data["user_id"],
            profile_id=user_info_data["profile_id"],
            username=user_info_data["username"],
            password_hash = user_info_data["password_hash"].encode('utf-8'),
            is_verified=user_info_data["is_verified"],
            created_at = user_info_data["created_at"],
            updated_at = user_info_data["updated_at"],
            created_by=user_info_data["created_by"],
            updated_by =user_info_data["updated_by"]
        )
        db.add(new_user_info)
        db.commit()
    return {'message': new_user_info,'api_created_at':str(api_created_at)}




inspector = inspect(engine)
tables = inspector.get_table_names()
print(tables)

