from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
async def get_users():
    return {"message": "All users"}

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}