import cv2
from services.face_service import FaceService

service = FaceService()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame, name = service.recognize(frame)

    print(name)

    cv2.imshow("Face Recognition Test", frame)

    if cv2.waitKey(1) == 27:   # ESC
        break

cap.release()
cv2.destroyAllWindows()