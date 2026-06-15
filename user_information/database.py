from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 
from dotenv import load_dotenv

load_dotenv()
db_url = os.getenv("USER_INFO_DB_URL")
if not db_url:
    raise RuntimeError("USER_INFO_DB_URL environment variable is not defined")
#db_url =  "postgresql://postgres:nuthana@host.docker.internal:5432/profile"
engine=create_engine(db_url)

SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base=declarative_base()