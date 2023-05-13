import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_NAME = "test.db"
SQLALCHEMY_DB_URL = f"sqlite:///{DB_NAME}"
#create engine with pool_pre_ping =True to enable the engine to check the database connection before every transaction
engine = create_engine(SQLALCHEMY_DB_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#creates a new declarative base for our SQLAlchemy models to inherit from
Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
