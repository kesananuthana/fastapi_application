import uuid
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy import UUID, Column, ForeignKey,String,Boolean,DateTime,func
from .database import *


class UserInfo(Base):
    __tablename__="userinfo"
    user_info_id=Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    user_id=Column(String,index=True,unique=True)
    profile_id=Column(String,index=True,unique=True)
    username=Column(String,index=True,unique=True)
    password_hash = Column(BYTEA, nullable=False)
    is_verified=Column(Boolean)
    is_admin=Column(Boolean)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
    created_by=Column(String,index=True)
    updated_by =Column(String,index=True)

    @property
    def user_info(self):
        return {
            "user_id":self.user_id,
            "profile_id":self.profile_id,
            "username":self.username,
            "password_hash":self.password_hash,
            "is_verified":self.is_verified,
            "is_admin":self.is_admin,
            "created_at":self.created_at,
            "updated_at":self.updated_at,
            "created_by":self.created_by,
            "updated_by":self.updated_by
        }
    
    @user_info.setter
    def user_info(self,value):
        self.user_id=value.get("user_id")
        self.profile_id=value.get("profile_id")
        self.username=value.get("username")
        self.password_hash=value.get("password_hash")
        self.is_verified=value.get("is_verified")
        self.is_admin=value.get("is_admin")
        self.created_at=value.get("created_at")
        self.updated_at=value.get("updated_at")
        self.created_by=value.get("created_by")
        self.updated_by=value.get("updated_by")




#insert api response in new table
class UserInformation(Base):
    __tablename__ = "userinformation"
    user_info_id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(String, index=True, unique=True)
    profile_id = Column(String, index=True, unique=True)
    username = Column(String, index=True, unique=True)
    password_hash = Column(BYTEA, nullable=False)
    is_verified = Column(Boolean)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
    created_by = Column(String, index=True)
    updated_by = Column(String,index=True)

    @property
    def user_information(self):
        return {
            "user_id":self.user_id,
            "profile_id":self.profile_id,
            "username":self.username,
            "password_hash":self.password_hash,
            "is_verified":self.is_verified,
            "created_at":self.created_at,
            "updated_at":self.updated_at,
            "created_by":self.created_by,
            "updated_by":self.updated_by
        }
    
    @user_information.setter
    def user_information(self,value):
        self.user_id=value.get("user_id")
        self.profile_id=value.get("profile_id")
        self.username=value.get("username")
        self.password_hash=value.get("password_hash")
        self.is_verified=value.get("is_verified")
        self.created_at=value.get("created_at")
        self.updated_at=value.get("updated_at")
        self.created_by=value.get("created_by")
        self.updated_by=value.get("updated_by")
