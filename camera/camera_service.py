import cv2
from services.face_service import FaceService


class CameraService:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            raise Exception("Could not open webcam.")

        self.face_service = FaceService()

    def get_frame(self):
        ret, frame = self.cap.read()

        if not ret:
            return None, False, "No Face"

        # Flip camera for mirror effect
        frame = cv2.flip(frame, 1)

        # Perform face recognition
        frame, person = self.face_service.recognize(frame)

        # Check if the recognized person is the owner
        owner_present = (person.lower() == "pratham")

        return frame, owner_present, person

    def release(self):
        if self.cap.isOpened():
            self.cap.release()