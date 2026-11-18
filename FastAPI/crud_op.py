from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Mouse", "price": 500},
    {"id": 3, "name": "Keyboard", "price": 1200}
]

# Retrieve all the products:
@app.get("/products")
async def get_products():
    return products

# Retrieve a specific product: 
@app.get("/products/{product_id}")
async def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(status_code=404, detail="product not found")

# POST:
class CreateProduct(BaseModel):
    name: str
    price: int

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

@app.put("/products/{product_id}")
async def update_product(product_id: int, product: CreateProduct):
    for p in products:
        if p["id"] == product_id:
            p.update({
                "name": product.name,
                "price": product.price
            })

            return p

    raise HTTPException(status_code=404, detail="Product not found")

# PATCH:
class UpdateProduct(BaseModel):
    name: str | None = None
    price: int | None = None

@app.patch("/products/{product_id}")
async def update_product(product_id: int, product: UpdateProduct):
    for p in products:
        if p['id'] == product_id:
            p.update(product.model_dump(exclude_unset = True))
            return p

    raise HTTPException(status_code=404, detail="Product not found")

# DELETE:
@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    for p in products:
        if p["id"] == product_id:
            products.remove(p)

            return {
                "messsage": "Product deleted successfully",
                "product": p
            }

    raise HTTPException(status_code=404, detail="Product not found")