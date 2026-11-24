
from database import SessionLocal
from models import User

session = SessionLocal()

try:
    # 1. Find the user to delete
    user = session.get(User, 1)

    if user:
        print("User found:", user.name)

        # 2. Mark the object for deletion
        session.delete(user)

        # 3. Commit the deletion
        session.commit()

        print("User deleted successfully!")

    else:
        print("User not found!")

except Exception as e:
    session.rollback()
    print("Error:", e)

finally:
    session.close()
