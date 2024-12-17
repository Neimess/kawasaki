from fastapi import APIRouter, UploadFile, File
from app.services import detect_objects
from app.models.prediction import PredictionResponse

router = APIRouter()


@router.post("/predict/", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    """
    Принимает изображение и возвращает координаты распознанных объектов.
    """
    # Читаем изображение из файла
    image_data = await file.read()

    # Обрабатываем изображение
    predictions = detect_objects(image_data)

    return {"objects": predictions}
