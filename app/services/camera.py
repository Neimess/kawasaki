# camera.py
import cv2
from app.utility.HikCamera.HikCamera import Camera as IPCamera
from pydantic import BaseModel, Field, ValidationError, model_validator

class CameraConfig(BaseModel):
    ip: str | None = Field(default=None, description="IP address of the camera")
    host_ip: str | None = Field(default=None, description="Host IP for the camera")
    video_path: str | None = Field(default=None, description="Path to the video file for debugging")

    @model_validator(mode="before")
    def validate_config(cls, values):
        ip, video_path = values.get("ip"), values.get("video_path")
        if not ip and not video_path:
            raise ValueError("Either IP address or video path must be provided.")
        if ip and video_path:
            raise ValueError("Provide only one: either IP address or video path.")
        return values

class Camera:
    def __init__(self, ip=None, host_ip=None, video_path=None):
        try:
            config = CameraConfig(ip=ip, host_ip=host_ip, video_path=video_path)
        except ValidationError as e:
            raise ValueError(f"Invalid camera configuration: {e}")

        self.cam = None
        self.capture = None
        if config.video_path:
            self.capture = cv2.VideoCapture(config.video_path)
            if not self.capture.isOpened():
                raise RuntimeError("Failed to open the video file.")
        elif config.ip:
            self.cam = IPCamera(config.ip, config.host_ip)
            self.cam.open()

    def capture_frame(self):
        if self.capture:
            ret, frame = self.capture.read()
            if not ret:
                raise RuntimeError("Failed to read frame from video file.")
            return frame
        elif self.cam:
            try:
                frame = self.cam.get_frame()
                return frame
            except Exception as e:
                raise RuntimeError(f"Failed to capture frame from IP camera: {str(e)}")
        else:
            raise RuntimeError("Camera is not initialized.")

    def is_opened(self):
        if self.capture:
            return self.capture.isOpened()
        else:
            return self.cam.__is_opened

    def release(self):
        if self.capture:
            self.capture.release()
        elif self.cam and self.cam.__is_opened:
            self.cam.close()

    def set_exposure(self, exposure_time):
        """
        Set the camera exposure time.

        :param exposure_time: Desired exposure time in microseconds.
        """
        if self.cam:
            self.cam.set_exposure(exposure_time)
        else:
            raise RuntimeError("Exposure setting is not supported for video files.")

    def set_pixel_format(self, format="RGB8Packed"):
        """
        Set the pixel format for the camera.

        :param format: Pixel format (default: "RGB8Packed").
        """
        if self.cam:
            self.cam.pixel_format = format
            self.cam.__set_item("PixelFormat", format)
        else:
            raise RuntimeError("Pixel format setting is not supported for video files.")