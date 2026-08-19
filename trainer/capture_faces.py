import cv2
import os

SAVE_DIR = "faces/pratham"
os.makedirs(SAVE_DIR, exist_ok=True)

cap = cv2.VideoCapture(0)

count = 0

print("Press SPACE to capture an image.")
print("Press ESC to exit.")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Capture Faces", frame)

    key = cv2.waitKey(1)

    if key == 32:  # Space key
        filename = os.path.join(SAVE_DIR, f"{count}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")
        count += 1

    elif key == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()