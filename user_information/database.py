from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#db_url = "postgresql://postgres:nuthana@localhost/profile"
db_url =  "postgresql://postgres:nuthana@host.docker.internal:5432/profile"
engine=create_engine(db_url)

SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base=declarative_base()