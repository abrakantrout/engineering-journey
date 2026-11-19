from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# CORS (Cross-Origin Resource Sharing) allows the backend to specify which frontend origins are permitted to access it.

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)