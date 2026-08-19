import os
import cv2
import numpy as np

DATASET_PATH = "faces"
MODEL_PATH = "models"

os.makedirs(MODEL_PATH, exist_ok=True)

recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []

label_map = {}
current_label = 0

for person in os.listdir(DATASET_PATH):

    person_path = os.path.join(DATASET_PATH, person)

    if not os.path.isdir(person_path):
        continue

    label_map[current_label] = person

    for image_name in os.listdir(person_path):

        image_path = os.path.join(person_path, image_name)

        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if image is None:
            continue

        faces.append(image)
        labels.append(current_label)

    current_label += 1

recognizer.train(faces, np.array(labels))
recognizer.save(os.path.join(MODEL_PATH, "face_model.yml"))

print("✅ Model trained successfully!")
print("Saved to models/face_model.yml")

print("\nLabel Mapping:")
for key, value in label_map.items():
    print(f"{key} -> {value}")