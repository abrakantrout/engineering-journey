import time
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def measure_time(reqeust: Request, call_next):
    start_time = time.time
    response = await call_next(reqeust)
    process_time = time.time() - start_time
    print(f"Request took {process_time:.4f} seconds")
    return response