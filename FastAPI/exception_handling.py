from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

# 400	Bad Request	(Invalid request)
# 401	Unauthorized	(Missing/invalid authentication)
# 403	Forbidden	(User lacks permission)
# 404	Not Found	(Product doesn't exist)
# 409	Conflict	(Duplicate resource)
# 422	Validation Error	(Invalid input data)
# 500	Internal Server Error	(Unexpected server error)

app = FastAPI()

load_dotenv()
APP_NAME = os.getenv("APP NAME")
DEBUG = os.getenv("DEBUG")
API_KEY = os.getenv("API_KEY")

products = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Mouse", "price": 500},
    {"id": 3, "name": "Keyboard", "price": 1200}
]

class CreateProduct(BaseModel):
    name: str
    price: int = Field(gt=0)

@app.post("/products")
async def create_product(product: CreateProduct):
    new_id = max(product["id"] for product in products) + 1

    new_product = {
        "id": new_id, 
        "name": product.name,
        "price": product.price
    }

    products.append(new_product)
    return new_product