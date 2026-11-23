
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "postgresql+psycopg://postgres:dblearn%4029@localhost:5432/engineering_journey_db"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version()"))

        print("Database connected successfully!")
        print(result.scalar())

except Exception as e:
    print("Database connection failed!")
    print(e)


# Creating a session:
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

try:
    print("SQLAlchemy Session created successfully.")

finally:
    session.close()
    print("Session closed successfully.")

# Create Declarative Base:
class Base(DeclarativeBase):
    pass
