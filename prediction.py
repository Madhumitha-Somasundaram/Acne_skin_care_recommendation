# app.py

import cv2
import numpy as np
from mtcnn import MTCNN

from tensorflow.keras.applications.mobilenet_v2 import preprocess_input



class_names = ['Blackheads', 'Cyst', 'Papules', 'Pustules', 'Whiteheads']

# --- Initialize MTCNN detector ---
detector = MTCNN()

# --- Helper functions ---
def detect_face(image):
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = detector.detect_faces(img_rgb)
    if len(results) == 0:
        return None
    x, y, w, h = results[0]['box']
    return (x, y, w, h)

def crop_acne_region(image, face):
    x, y, w, h = face
    y_start = y + int(0.4*h)
    y_end = y + h
    crop = image[y_start:y_end, x:x+w]
    return crop

def predict_acne_auto_cv2(img, model):
    face = detect_face(img)
    if face is not None:
        img_crop = crop_acne_region(img, face)
    else:
        img_crop = img

    img_resized = cv2.resize(img_crop, (224,224))
    img_array = np.expand_dims(img_resized, axis=0)
    img_array = preprocess_input(img_array)

    pred = model.predict(img_array)
    class_id = int(np.argmax(pred))
    confidence = float(np.max(pred))
    label = class_names[class_id]

    return label, confidence, img_crop

