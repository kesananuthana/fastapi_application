import hashlib
from .models import *
from .schema import *
from .database import *
from sqlalchemy.orm import Session


def create_user_info_data(db:Session,userinfo:UserInformationDetails):
    username_hash = hashlib.sha256(userinfo.username.encode()).digest()
    user_id = int.from_bytes(username_hash[:8], 'big') % (10**8)
    db_userinfo_data = db.query(UserInfo).filter_by(username=userinfo.username).first()
    if db_userinfo_data is None or db_userinfo_data.password_hash != userinfo.password_hash.encode('utf-8'):
        db_userinfo_data=UserInfo(
            user_id=str(user_id),
            username=userinfo.username,
            password_hash=userinfo.password_hash.encode('utf-8'),
            is_verified=userinfo.is_verified,
            #is_admin=userinfo.is_admin,
            #created_by=userinfo.created_by,
            #updated_by =userinfo.updated_by 
        )
        db.add(db_userinfo_data)
        db.commit()
        return db_userinfo_data,
    return 'error'