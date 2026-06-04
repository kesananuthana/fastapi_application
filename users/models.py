from sqlalchemy import Column,String,Integer
from .database import *

class Employee(Base):
    __tablename__="employee"
    id=Column(Integer,primary_key=True)
    name=Column(String,index=True)
    email=Column(String,index=True)