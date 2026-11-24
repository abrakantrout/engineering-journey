
from database import SessionLocal
from models import User

session = SessionLocal()

try:
    # 1. Find the user we want to update
    user = session.get(User, 1)

    if user:
        # 2. Modify the user's attributes
        print("Before update:", user.name, user.age)

        user.age = 22
        user.name = "Rahul Kumar"

        # 3. Save changes to the database
        session.commit()

        print("User updated successfully!")

        # 4. Display updated information
        session.refresh(user)

        print("After update:", user.name, user.age)

    else:
        print("User not found!")

except Exception as e:
    session.rollback()
    print("Error:", e)

finally:
    session.close()
