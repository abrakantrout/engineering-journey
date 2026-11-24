
from sqlalchemy import select
from database import SessionLocal
from models import User

session = SessionLocal()

try:
    # 1. Retrieve all users
    statement = select(User)
    users = session.scalars(statement).all()

    print("\n--- ALL USERS ---")

    for user in users:
        print(
            f"ID: {user.id} | "
            f"Name: {user.name} | "
            f"Email: {user.email} | "
            f"Age: {user.age}"
        )

    # 2. Retrieve a user by ID
    statement = select(User).where(User.id == 1)
    user = session.scalar(statement)

    print("\n--- USER WITH ID 1 ---")

    if user:
        print("Name:", user.name)
        print("Email:", user.email)
    else:
        print("User not found!")

    # 3. Retrieve a user by email
    statement = select(User).where(
        User.email == "rahul@gmail.com"
    )

    user = session.scalar(statement)

    print("\n--- USER BY EMAIL ---")

    if user:
        print("Name:", user.name)
        print("Email:", user.email)
    else:
        print("User not found!")

except Exception as e:
    print("Error:", e)

finally:
    session.close()
