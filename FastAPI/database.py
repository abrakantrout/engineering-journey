
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, DeclarativeBase

import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# Creating a session:
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


# Create Declarative Base:
class Base(DeclarativeBase):
    pass
