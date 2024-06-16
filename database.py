from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Vondabaic2020@localhost:5432/TODOLIST"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
