from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from .database import *

class Person(Base):
    __tablename__='person'
    id=Column(Integer,primary_key=True)
    name=Column(String,index=True)
    age=Column(Integer)
    address=relationship('Address',back_populates='person')

class Address(Base):
    __tablename__='address'
    pid=Column(Integer,ForeignKey('person.id'))
    id=Column(Integer,primary_key=True)
    street=Column(String,index=True)
    city=Column(String,index=True)
    state=Column(String,index=True)
    person=relationship('Person',back_populates='address')