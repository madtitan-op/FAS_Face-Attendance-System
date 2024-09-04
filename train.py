import cv2
import numpy as np
import os

# Initialize the LBPHFaceRecognizer
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def prepare_training_data(data_folder_path):
    faces = []
    labels = []
    for label, person_name in enumerate(os.listdir(data_folder_path)):
        person_folder_path = os.path.join(data_folder_path, person_name)
        if not os.path.isdir(person_folder_path):
            continue
        for image_name in os.listdir(person_folder_path):
            image_path = os.path.join(person_folder_path, image_name)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            faces_detected = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)
            for (x, y, w, h) in faces_detected:
                faces.append(image[y:y+h, x:x+w])
                labels.append(label)
    return faces, labels

# Prepare the training data
data_folder_path = "image"
faces, labels = prepare_training_data(data_folder_path)

# Train the recognizer
face_recognizer.train(faces, np.array(labels))

# Save the trained model to a file
face_recognizer.save("model/model.yml")
