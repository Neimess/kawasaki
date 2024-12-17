from fastapi import FastAPI
from app.api.routers import predict
from fastapi import FastAPI
from app.api.routers.camera_router import router as camera_router

app = FastAPI()


app.include_router(camera_router, prefix="/api")
