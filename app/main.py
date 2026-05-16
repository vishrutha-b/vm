from fastapi import FastAPI
from app.config import settings
from app.routers.health import router as health_router

import logging
import os

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title=settings.APP_NAME
)

@app.get("/")
def root():
    logging.info("Root endpoint called")

    return {
        "message": "FastAPI backend running successfully",
        "environment": settings.ENVIRONMENT
    }

app.include_router(health_router)

PORT = int(os.environ.get("PORT", 8080))