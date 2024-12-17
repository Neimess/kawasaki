from fastapi import FastAPI
from app.api.routers import predict
from fastapi import FastAPI
from app.api.routers.camera_router import router as camera_router

app = FastAPI()

# Основной маршрут


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}



# Подключаем маршруты из predict.py
app.include_router(predict.router)
app.include_router(camera_router, prefix="/api")
