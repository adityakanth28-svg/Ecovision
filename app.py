import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
model = tf.keras.models.load_model("ecovision_model.keras")

class_names = ["Plastic", "glass", "metal", "organic", "paper"]

st.title("EcoVision")
st.write("AI-Based Waste Image Classifier")

st.divider()

uploaded_file = st.file_uploader(
    "Upload a waste image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image")

    image = image.resize((224, 224))

    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    prediction = model.predict(image_array)

    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    st.success(f"Prediction: {predicted_class}")
    st.info(f"Confidence: {confidence:.2f}%")