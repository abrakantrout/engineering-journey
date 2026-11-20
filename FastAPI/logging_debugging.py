import logging
import time

from fastapi import FastAPI, Request

app = FastAPI()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


@app.get("/")
async def home():
    logger.info("Home endpoint accessed")
    return {"message": "Welcome"}


@app.get("/error")
async def error():
    try:
        result = 10 / 0
        return {"result": result}

    except Exception:
        logger.exception("An error occurred")
        return {"message": "Something went wrong"}