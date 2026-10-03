import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="EcoVision",
    page_icon="♻️",
    layout="wide"
)

# -----------------------------
# Load model
# -----------------------------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("ecovision_model.keras")

model = load_model()

class_names = ["Plastic", "glass", "metal", "organic", "paper"]

# -----------------------------
# Custom styling
# -----------------------------
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        font-size: 1.15rem;
        margin-top: 0;
        margin-bottom: 2rem;
    }

    .result-card {
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid rgba(128, 128, 128, 0.3);
        text-align: center;
        margin-top: 1rem;
    }

    .prediction {
        font-size: 2rem;
        font-weight: 700;
        margin: 0.5rem 0;
    }

    .confidence {
        font-size: 1.2rem;
    }

    .section-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-top: 2rem;
    }

    .category-box {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        text-align: center;
    }

    footer {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="main-title">♻️ EcoVision</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-Powered Waste Image Classification'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

st.write(
    "Upload an image of waste and EcoVision will identify its category "
    "using a deep learning model."
)

# -----------------------------
# Upload section
# -----------------------------
st.markdown(
    '<div class="section-title">📸 Upload Waste Image</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"],
    help="Supported formats: JPG, JPEG and PNG"
)

# -----------------------------
# Prediction
# -----------------------------
if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.divider()

    image_col, result_col = st.columns(2)

    # Image preview
    with image_col:
        st.subheader("🖼️ Uploaded Image")
        st.image(
            image,
            use_container_width=True
        )

    # Prediction
    with result_col:

        st.subheader("🔍 EcoVision Result")

        resized_image = image.resize((224, 224))

        image_array = np.array(resized_image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        prediction = model.predict(image_array, verbose=0)

        predicted_class = class_names[np.argmax(prediction)]
        confidence = np.max(prediction) * 100

        st.markdown(
            '<div class="result-card">',
            unsafe_allow_html=True
        )

        st.write("Predicted Category")

        st.markdown(
            f'<div class="prediction">{predicted_class}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="confidence">'
            f'Confidence: <b>{confidence:.2f}%</b>'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

        st.progress(
            int(confidence),
            text=f"Model confidence: {confidence:.2f}%"
        )

# -----------------------------
# Supported categories
# -----------------------------
st.divider()

st.markdown(
    '<div class="section-title">🗂️ Supported Waste Categories</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4, col5 = st.columns(5)

categories = [
    ("🧴", "Plastic"),
    ("🍾", "Glass"),
    ("🔩", "Metal"),
    ("🌱", "Organic"),
    ("📄", "Paper")
]

for col, (icon, category) in zip(
    [col1, col2, col3, col4, col5],
    categories
):
    with col:
        st.markdown(
            f"""
            <div class="category-box">
                <div style="font-size: 2rem;">{icon}</div>
                <b>{category}</b>
            </div>
            """,
            unsafe_allow_html=True
        )

# -----------------------------
# About
# -----------------------------
st.divider()

with st.expander("ℹ️ About EcoVision"):

    st.write(
        """
        **EcoVision** is an AI-based waste image classifier.

        It uses a deep learning model based on **MobileNetV2**
        to classify waste images into five categories:

        **Plastic, Glass, Metal, Organic, and Paper.**
        """
    )

    st.caption(
        "Upload an image above to get a prediction."
    )

# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "♻️ EcoVision • AI for smarter waste classification"
)