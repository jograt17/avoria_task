from fastapi import FastAPI
from app.controller.routes import router
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

app = FastAPI()
app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "API is running"}
