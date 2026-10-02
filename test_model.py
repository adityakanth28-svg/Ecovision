import tensorflow as tf
import numpy as np
from PIL import Image

MODEL_PATH = "ecovision_model.keras"

model = tf.keras.models.load_model(MODEL_PATH)

class_names = ["Plastic", "glass", "metal", "organic", "paper"]

image_path = input("Enter image path: ")

image = Image.open(image_path).convert("RGB")
image = image.resize((224, 224))

image_array = np.array(image) / 255.0
image_array = np.expand_dims(image_array, axis=0)

prediction = model.predict(image_array)

predicted_class = class_names[np.argmax(prediction)]
confidence = np.max(prediction) * 100

print("\nPrediction:", predicted_class)
print("Confidence:", round(confidence, 2), "%")