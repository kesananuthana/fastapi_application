from pydantic import BaseModel

class UserInformationDetails(BaseModel):
    username:str
    password_hash: str
    is_verified:bool
    #is_admin:bool