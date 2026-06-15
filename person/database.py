import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
db_url = os.getenv("PERSON_DB_URL")
if not db_url:
    raise RuntimeError("PERSON_DB_URL environment variable is not defined")
#db_url = "postgresql://postgres:nuthana@host.docker.internal:5432/person"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autoflush=False,bind=engine, autocommit=False)
Base = declarative_base()