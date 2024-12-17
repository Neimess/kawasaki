from pydantic import BaseModel
from typing import List

 
class ObjectPrediction(BaseModel):
    label: str
    confidence: float
    bbox: List[int]  # [x_min, y_min, x_max, y_max]


class PredictionResponse(BaseModel):
    objects: List[ObjectPrediction]
