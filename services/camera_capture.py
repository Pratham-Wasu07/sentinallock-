import cv2
import os
from datetime import datetime


def save_intruder_photo(frame):

    os.makedirs("intruders", exist_ok=True)

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.jpg")

    path = os.path.join("intruders", filename)

    cv2.imwrite(path, frame)

    return path