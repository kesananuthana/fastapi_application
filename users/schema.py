from pydantic import BaseModel

class Employees(BaseModel):
    id:int
    name:str
    email:str