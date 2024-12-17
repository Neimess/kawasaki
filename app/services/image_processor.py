import cv2
import numpy as np
from ultralytics import YOLO

class ImageProcessor:
    def __init__(self, model_path, class_labels, img_height=128, img_width=128):
        self.model = YOLO(model_path)
        self.class_labels = class_labels
        self.img_height = img_height
        self.img_width = img_width

    def process_image(self, image):
        results = self.model(image)
        detections = []

        for result in results:
            for data in result.boxes.data.tolist():
                xmin, ymin, xmax, ymax, confidence, class_id = data[:6]
                if confidence < 0.5:
                    continue
                detections.append({
                    "coordinates": (int(xmin), int(ymin), int(xmax), int(ymax)),
                    "class": self.class_labels[int(class_id)],
                    "confidence": float(confidence)
                })

        return detections

    def transform_zone(self, frame):
        """
        Applies the perspective transformation using pre-stored matrix in transformation_data.json.
        """
        import json

        with open('transformation_data.json', 'r') as json_file:
            data = json.load(json_file)

        M = np.array(data['M'])
        maxWidth = data['maxWidth']
        maxHeight = data['maxHeight']

        transformed_frame = cv2.warpPerspective(frame, M, (maxWidth, maxHeight))
        return transformed_frame

    def process_and_detect(self, frame):
        transformed_frame = self.transform_zone(frame)
        detections = self.process_image(transformed_frame)
        return detections, transformed_frame
