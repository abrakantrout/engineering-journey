
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "postgresql+psycopg://postgres:dblearn%4029@localhost:5432/engineering_journey_db"

engine = create_engine(DATABASE_URL)

# Creating a session:
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


# Create Declarative Base:
class Base(DeclarativeBase):
    pass
