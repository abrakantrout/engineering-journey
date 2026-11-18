from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user():
    return {"message": "User created successfully"}

# if somone requests a user who doesn't exit:
@app.get("/users/{user_id}")
async def get_user(user_id: int):

    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {"user_id": 1, "name": "Rahul"}


# Example: 
class Product(BaseModel):
    name: str
    price: float


class ProductResponse(BaseModel):
    name: str
    price: float


@app.post(
    "/products",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_product(product: Product):
    return product


@app.get("/products/{product_id}")
async def get_product(product_id: int):

    if product_id != 1:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "product_id": 1,
        "name": "Laptop",
        "price": 55000
    }