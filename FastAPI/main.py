from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from routers import users, products

app = FastAPI()

app.include_router(users.router)
app.include_router(products.router)

class User(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: str
    age: int = Field(gt=0, lt=100)

class UserResponse(BaseModel):
    name: str
    email: str

class Product(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    price: float = Field(gt=0)
    quantity: int = Field(ge=1)

@app.get("/")
async def home():
    return {"message": "Welcome to my API"}

@app.get("/users")
async def get_users():
    return {"users": ["Rahul", "Amit", "Priya"]}

@app.post("/users", response_model=UserResponse)
async def create_user(user: User):
    return user

@app.get("/products")
async def get_products():
    return {"products": ["laptop", "phone", "tablet"]}

@app.post("/users")
async def create_user(user: User):
    return {"message": "User Created", 
            "user": user}

@app.post("/products")
async def create_product(product: Product):
    return {
        "message": "Product received successfully",
        "product": product
    }

@app.delete("/users")
async def delete_user():
    return {"message": "Users deleted"}

@app.get("/about")
async def about():
    return {"project": "FastAPI Learning",
            "status": "In Progress"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/products/filter")
async def filter_products(category: str, limit: int = 10):
    return {
        "category": category,
        "limit": limit
    }

@app.get("/products")
async def get_products(limit: int = Query(default=10, ge=1, le=100)):
    return {"limit": limit}

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    return {"product_id": product_id}

