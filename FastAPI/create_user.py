from database import SessionLocal
from models import User

session = SessionLocal()

try:
    new_user = User(
        name="Rahul",
        email="rahul@gmail.com",
        age=21,
        phone="9876543210"
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    print("User created successfully.")
    print("User ID:", new_user.id)
    print("Name:", new_user.name)
    print("Email:", new_user.email)

except Exception as e:
    session.rollback()
    print("Error:", e)

finally:
    session.close()