from fastapi import FastAPI, Depends

app = FastAPI()

def common_parameters():
    return {
        "message": "This is reusable logic"
    }

@app.get("/test")
async def test_endpoint(data = Depends(common_parameters)):
    return data

# dependencies with parameters:
def get_product_limit(limit: int = 10):
    return limit


@app.get("/limited-products")
async def limited_products(limit: int = Depends(get_product_limit)):
    return {"limit": limit}

# Reusing dependencies across endpoints
def verify_access():
    return "Access granted"


@app.get("/dashboard")
async def dashboard(access = Depends(verify_access)):
    return {"access": access}


@app.get("/profile")
async def profile(access = Depends(verify_access)):
    return {"access": access}


@app.get("/settings")
async def settings(access = Depends(verify_access)):
    return {"access": access}