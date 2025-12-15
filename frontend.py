# --- Streamlit UI ---
import streamlit as st
from skin_care_recommendation import get_acne_recommendation
from PIL import Image
import cv2
from prediction import predict_acne_auto_cv2
from tensorflow.keras.models import load_model
import numpy as np
# --- Load model ---
@st.cache_resource
def load_acne_model(path="acne_classifier.h5"):
    model = load_model(path)
    return model

model = load_acne_model()
st.title("Acne Detection & Skin Care Recommendation")

option = st.radio("Select Input Method", ["Upload Image", "Capture from Webcam"])

if option == "Upload Image":
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"])
    if uploaded_file:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Uploaded Image", use_container_width=True)
elif option == "Capture from Webcam":
    img_file_buffer = st.camera_input("Capture your image")
    if img_file_buffer:
        file_bytes = np.asarray(bytearray(img_file_buffer.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Captured Image", use_container_width=True)

# ----------------------------
# Predict & Recommend
# ----------------------------
if st.button("Predict") and 'img' in locals():
    label, confidence, crop_img = predict_acne_auto_cv2(img, model)
    st.success(f"Predicted Acne Type: {label} ({confidence*100:.2f}%)")


    rec = get_acne_recommendation(label)

    st.subheader("General Tips")

    st.write(f"- {rec['advice']}")
    st.write(f"- {rec['diet_tips']}")
    st.write(f"- {rec['lifestyle']}")

    st.subheader("Recommended Cleanser")
    for name, link in rec['cleanser']:
        st.markdown(f"- [{name}]({link})")

    st.subheader("Recommended Moisturizer")
    for name, link in rec['moisturizer']:
        st.markdown(f"- [{name}]({link})")

    st.subheader("Recommended Spot Treatment")
    for name, link in rec['spot_treatment']:
        st.markdown(f"- [{name}]({link})")