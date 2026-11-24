
from database import SessionLocal
from models import User, Course

session = SessionLocal()

try:
    # Start performing database operations

    new_user = User(
        name="Transaction Demo",
        email="transaction_demo@gmail.com",
        age=22
    )

    session.add(new_user)

    # Commit the transaction
    session.commit()

    print("Transaction committed successfully!")

except Exception as e:
    # Undo uncommitted changes if an error occurs
    session.rollback()

    print("Transaction failed!")
    print("Error:", e)

finally:
    # Always close the session
    session.close()

    print("Session closed!")

# Cleaner approach using (session.begin())
with SessionLocal() as session:
    with session.begin():

        new_user = User(
            name="Transaction Demo 2",
            email="transaction_demo2@gmail.com",
            age=22
        )

        session.add(new_user)