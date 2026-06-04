from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#db_url = "postgresql://postgres:nuthana@localhost/person"
db_url = "postgresql://postgres:nuthana@host.docker.internal:5432/person"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autoflush=False,bind=engine, autocommit=False)
Base = declarative_base()