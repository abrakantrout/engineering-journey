from fastapi import APIRouter

router = APIRouter()

@router.get("/products")
async def get_products():
    return {"message": "All products"}

@router.get("/products/{product_id}")
async def get_product(product_id: int):
    return {"product_id": product_id}