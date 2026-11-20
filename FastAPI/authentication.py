from pwdlib import PasswordHash
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt.exceptions import InvalidTokenError
from pydantic import BaseModel, EmailStr
import os
import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
)

if not SECRET_KEY:
    raise RuntimeError("JWT_SECRET_KEY is missing from .env")

password_hash = PasswordHash.recommended()

def hash_password(password: str):
    return password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return password_hash.verify(plain_password, hashed_password)

# Testing
hashed = hash_password("mypassword123")

print("Hashed password:", hashed)
print("Correct password:", verify_password("mypassword123", hashed))
print("Wrong password:", verify_password("wrongpassword", hashed))

app = FastAPI()

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

users = []

@app.post("/register")
async def register_user(user: UserRegister):
    for existing_user in users:
        if existing_user["username"] == user.username:
            raise HTTPException(
                status_code=400, detail="Username already exits"
            )

        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=400, detail="Email already registered"
            )

    hashed_password = hash_password(user.password)

    new_user = {
        "id": len(users) + 1,
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_password,
        "role": "user"
    }

    users.append(new_user)

    return {
        "message": "User registered successfully",
        "user": {
            "id": new_user["id"],
            "username": new_user["username"],
            "email": new_user["email"]
        }
    }

@app.post("/login")
async def login_user(user: UserLogin):
    existing_user = None

    for u in users:
        if u["email"] == user.email:
            existing_user = u
            break

    if existing_user is None:
        raise HTTPException(
            status_code=401, detail="Invalid email or password"
        )

    if not verify_password( user.password, existing_user["hashed_password"]):
        raise HTTPException(
            status_code=401, detail="Invalid email or password"
        )

    access_token = create_access_token(
    data={"sub": existing_user["email"]}
)

    return {
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "bearer"
    }

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token, SECRET_KEY, algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return email

    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

def get_admin_user(current_user: str = Depends(get_current_user)):
    for user in users:
        if user["email"] == current_user:
            if user["role"] != "admin":
                raise HTTPException(status_code=403, detail="Admin access required")

            return user

    raise HTTPException(status_code=401, detail="User not found")

@app.get("/profile")
async def get_profile(current_user: str = Depends(get_current_user)):
    return {
        "message": "You accessed a protected endpoint",
        "email": current_user
    }

@app.get("/admin")
async def admin_dashboard(admin = Depends(get_admin_user)):
    return {
        "message": "Welcome to the admin dashboard",
        "admin": admin["username"]
    }