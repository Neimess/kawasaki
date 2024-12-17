import cv2
import numpy as np


def detect_objects(image_data: bytes):
    """
    Обрабатывает изображение и возвращает список распознанных объектов с координатами.
    """
    # Преобразуем байты в изображение
    np_image = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

    # TODO: Здесь нужно подключить модель распознавания, например, YOLOv5
    # Заглушка: возвращаем пример координат
    predictions = [
        {"label": "object1", "confidence": 0.95, "bbox": [100, 50, 200, 150]},
        {"label": "object2", "confidence": 0.88, "bbox": [300, 200, 400, 350]},
    ]
    return predictions
