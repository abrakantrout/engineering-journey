from fastapi import FastAPI, Query

app = FastAPI()

products = [
    {"id": i, "name": f"Product {i}"}
    for i in range(1, 101)
]


@app.get("/products")
async def get_products(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=50)
):
    return products[skip:skip + limit]