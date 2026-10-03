from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import tensorflow as tf
import numpy as np
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = tf.keras.models.load_model("ecovision_model.keras")

class_names = [
    "Plastic",
    "glass",
    "metal",
    "organic",
    "paper"
]


@app.get("/")
def home():
    return {
        "message": "EcoVision API is running"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    contents = await file.read()

    image = Image.open(
        io.BytesIO(contents)
    ).convert("RGB")

    image = image.resize((224, 224))

    image_array = np.array(image)

    image_array = image_array / 255.0

    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    predictions = model.predict(image_array)

    predicted_index = np.argmax(predictions[0])

    predicted_class = class_names[predicted_index]

    confidence = float(
        predictions[0][predicted_index] * 100
    )

    return {
        "prediction": predicted_class,
        "confidence": round(confidence, 2)
    }