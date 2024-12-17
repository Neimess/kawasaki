from fastapi import APIRouter, Response
from app.services.camera import Camera
from app.services.image_processor import ImageProcessor
from fastapi.responses import JSONResponse, StreamingResponse
import cv2

router = APIRouter()

# Initialize components
# Example: Use video file for debugging or switch to IP camera by changing parameters

camera = Camera(ip="vid1.avi")
image_processor = ImageProcessor(
    model_path="app/best.pt",
    class_labels=["class1", "class2", "class3"]
)
print(camera.is_opened())
@router.get("/coords")
def get_coords():
    try:
        frame = camera.capture_frame()
        coords = image_processor.process_image(frame)
        return JSONResponse(content={
            "coords": coords
        }, media_type="application/json")
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
@router.get("/camera/capture")
def capture_image():
    try:
        frame = camera.capture_frame()
        _, buffer = cv2.imencode(".jpg", frame)
        return Response(content=buffer.tobytes(), media_type="image/jpeg")
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@router.get("/camera/stream")
def video_steam():
    return StreamingResponse(generate_video(), media_type="multipart/x-mixed-replace;boundary=frame")
@router.post("/detect")
def detect_objects():
    try:
        frame = camera.capture_frame()
        detections, transformed_frame = image_processor.process_and_detect(frame)
        return {"detections": detections}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@router.post("/camera/release")
def shutdown_event():
    camera.release()
    return JSONResponse(content={"status": "shutting down..."}, media_type="application/json")


def generate_video():
    while True:
        try:
            frame = camera.capture_frame()
            _, buffer = cv2.imencode(".jpg", frame)
            yield (b"--frame\r\n"
                   b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n")
        except Exception as e:
            break
