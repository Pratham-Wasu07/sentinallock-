import cv2
import mediapipe as mp

class FaceService:
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        from utils.resource_path import resource_path
        self.recognizer.read(
    resource_path("models/face_model.yml")
)

        self.face_detection = mp.solutions.face_detection.FaceDetection(
            model_selection=0,
            min_detection_confidence=0.6
        )

        # Label mapping from your training script
        self.labels = {
            0: "pratham"
        }

    def recognize(self, frame):

        if frame is None or frame.size == 0:
            return None, "No Face"

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_detection.process(rgb)

        if not results.detections:
            return frame, "No Face"

        h, w, _ = frame.shape

        for detection in results.detections:

            bbox = detection.location_data.relative_bounding_box

            x = max(0, int(bbox.xmin * w))
            y = max(0, int(bbox.ymin * h))
            bw = int(bbox.width * w)
            bh = int(bbox.height * h)

            # Clamp to image boundaries
            x2 = min(x + bw, w)
            y2 = min(y + bh, h)

            if x >= x2 or y >= y2:
                return frame, "No Face"

            face = frame[y:y2, x:x2]

            if face is None or face.size == 0:
                return frame, "No Face"

            gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            gray = cv2.resize(gray, (200, 200))

            try:
                label, confidence = self.recognizer.predict(gray)
            except cv2.error:
                return frame, "Unknown"

            if confidence < 70:
                name = self.labels.get(label, "Unknown")
                color = (0, 255, 0)
            else:
                name = "Unknown"
                color = (0, 0, 255)

            cv2.rectangle(frame, (x, y), (x2, y2), color, 2)

            cv2.putText(
                frame,
                f"{name} ({confidence:.1f})",
                (x, max(30, y - 10)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                color,
                2,
            )

            return frame, name

        return frame, "No Face"
    