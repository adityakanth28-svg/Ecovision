# 🌱 EcoVision

AI-Powered Waste Classification Using Computer Vision

\<p align="center">
&#x20; \<b>Smarter Waste. Cleaner Future.\</b>
\</p>

\<p align="center">
&#x20; EcoVision is an AI-powered web application that uses deep learning and computer vision to classify waste images into five categories.
\</p>

\<p align="center">
&#x20; \<a href="[https://eco-lens-project.lovable.app](https://eco-lens-project.lovable.app)">
&#x20;   \<img src="[https://img.shields.io/badge/🌐%20Live%20Demo-EcoVision-16a34a?style=for-the-badge](https://img.shields.io/badge/🌐%20Live%20Demo-EcoVision-16a34a?style=for-the-badge)" alt="Live Demo">
&#x20; \</a>
&#x20; \<a href="[https://ecovision-67mp.onrender.com/docs](https://ecovision-67mp.onrender.com/docs)">
&#x20;   \<img src="[https://img.shields.io/badge/⚡%20API%20Docs-FastAPI-009688?style=for-the-badge](https://img.shields.io/badge/⚡%20API%20Docs-FastAPI-009688?style=for-the-badge)" alt="API Docs">
&#x20; \</a>
&#x20; \<a href="[https://github.com/adityakanth28-svg/Ecovision](https://github.com/adityakanth28-svg/Ecovision)">
&#x20;   \<img src="[https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge\&logo=github)" alt="GitHub">
&#x20; \</a>
\</p>
---
## 🚀 Live Demo

### 🌐 Try EcoVision

\<p align="center">
&#x20; \<a href="[https://eco-lens-project.lovable.app](https://eco-lens-project.lovable.app)">
&#x20;   \<img src="[https://img.shields.io/badge/🚀%20OPEN%20ECOVISION-Live%20Application-22c55e?style=for-the-badge](https://img.shields.io/badge/🚀%20OPEN%20ECOVISION-Live%20Application-22c55e?style=for-the-badge)" alt="Open EcoVision">
&#x20; \</a>
\</p>
**Live Application:**
[https://eco-lens-project.lovable.app](https://eco-lens-project.lovable.app)

**FastAPI Backend:**
[https://ecovision-67mp.onrender.com](https://ecovision-67mp.onrender.com)

**Interactive API Documentation:**
[https://ecovision-67mp.onrender.com/docs](https://ecovision-67mp.onrender.com/docs)

> Note: The Render backend uses a free-tier deployment, so the first request after a period of inactivity may take longer because the service can cold-start.

---

# 📸 Screenshots 
<img width="1887" height="902" alt="Image" src="https://github.com/user-attachments/assets/41302c6f-d26b-4769-8dd0-f1112cc623ba" />

<img width="1865" height="815" alt="Image" src="https://github.com/user-attachments/assets/c3aa7011-b6ac-44a9-9757-9767d6970e0a" />
<img width="1895" height="883" alt="Image" src="https://github.com/user-attachments/assets/cdfb0e55-0e49-49c4-a206-67b260dd5d2a" />
<img width="1880" height="751" alt="Image" src="https://github.com/user-attachments/assets/07583829-2034-46f0-adb3-512dac586f4e" />

<img width="1891" height="825" alt="Image" src="https://github.com/user-attachments/assets/f9df3f71-6c1f-4fdd-a640-00b93276b4bc" />
<img width="1517" height="705" alt="Image" src="https://github.com/user-attachments/assets/526d7b7d-fc1e-484a-9d6a-3ab952fef6f0" />
<img width="727" height="722" alt="Image" src="https://github.com/user-attachments/assets/1086077f-6d0c-43e3-b941-28f7e39d9dc4" />

<img width="1377" height="496" alt="Image" src="https://github.com/user-attachments/assets/2aec527d-3eb1-4a5b-9161-1bcb2bb51c2b" />

## 🏠 EcoVision Homepage
<img width="1887" height="902" alt="Image" src="https://github.com/user-attachments/assets/41302c6f-d26b-4769-8dd0-f1112cc623ba" />

## 📤 Waste Image Upload



## 🤖 AI Prediction Result
<img width="1517" height="705" alt="Image" src="https://github.com/user-attachments/assets/526d7b7d-fc1e-484a-9d6a-3ab952fef6f0" />




---

# ♻️ What Does EcoVision Do?

EcoVision allows users to upload an image of a waste item and uses a trained TensorFlow/Keras model to classify it into one of five categories:

| Category       | Example                          |
| -------------- | -------------------------------- |
| 🧴 **Plastic** | Bottles, containers, packaging   |
| 🍾 **Glass**   | Bottles, jars, glass objects     |
| 🥫 **Metal**   | Cans, tins, metal containers     |
| 🌱 **Organic** | Food and biodegradable waste     |
| 📄 **Paper**   | Paper, cardboard, paper products |

The application returns both the predicted category and the model's confidence score.

---

# 🧠 How EcoVision Works

```text
┌──────────────────────┐
│       User           │
│  Upload Waste Image  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   EcoVision Web App  │
│   Lovable / React    │
└──────────┬───────────┘
           │
           │ HTTPS POST
           │ multipart/form-data
           ▼
┌──────────────────────┐
│    FastAPI Backend   │
│      Render Cloud    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Image Preprocessing  │
│   Resize: 224×224    │
│   RGB Normalization  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ TensorFlow / Keras   │
│   Trained AI Model   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Prediction +         │
│ Confidence Score     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Result Displayed     │
│ in EcoVision UI      │
└──────────────────────┘
```

---

# 🏗️ System Architecture

```text
                  ECOVISION
                     │
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
  React / Lovable            GitHub Repository
   Frontend                       │
        │                         │
        │ HTTPS                   │
        ▼                         │
  Render FastAPI                  │
        │                         │
        ▼                         │
  TensorFlow Model ◄──────────────┘
        │
        ▼
  Waste Classification
        │
        ▼
Prediction + Confidence
```

### Deployment Architecture

| Layer      | Technology         | Platform |
| ---------- | ------------------ | -------- |
| Frontend   | React / Vite       | Lovable  |
| Backend    | FastAPI            | Render   |
| AI Model   | TensorFlow / Keras | Render   |
| Repository | Git                | GitHub   |

---

# 🛠️ Technology Stack

### 🤖 Artificial Intelligence




\


### ⚡ Backend

\


### 🌐 Frontend

\


### ☁️ Deployment & Development

\


---

# 📂 Project Structure

```text
Ecovision/
│
├── Dataset/
│
├── garbage_classification/
│
├── .streamlit/
│
├── api.py
├── app.py
│
├── ecovision_model.keras
│
├── prepare_dataset.py
├── train_model.py
├── test_model.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🧠 Model Information

The trained model accepts RGB images with the following input shape:

```text
224 × 224 × 3
```

### Preprocessing

Before prediction, each uploaded image is:

1. Converted to RGB
2. Resized to `224 × 224`
3. Converted into a NumPy array
4. Normalized by scaling pixel values
5. Passed to the trained TensorFlow/Keras model

### Output Classes

```text
Plastic
Glass
Metal
Organic
Paper
```

The model selects the class with the highest predicted probability.

---

# ⚡ API

EcoVision exposes a FastAPI endpoint for image classification.

### Endpoint

```http
POST /predict
```

### Request

```text
Content-Type: multipart/form-data
```

Form field:

```text
file
```

### Example Response

```json
{
  "prediction": "glass",
  "confidence": 90.88
}
```

### Test the API

Open:

[https://ecovision-67mp.onrender.com/docs](https://ecovision-67mp.onrender.com/docs)

You can use the interactive Swagger interface to upload an image and test the prediction endpoint.

---

# 💻 Run Locally

## 1. Clone the repository

```bash
git clone https://github.com/adityakanth28-svg/Ecovision.git
cd Ecovision
```

## 2. Create a virtual environment

```bash
python -m venv venv
```

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Start the FastAPI server

```bash
uvicorn api:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🎯 Project Objective

The goal of EcoVision is to explore how **deep learning and computer vision can be applied to automated waste classification**.

The project demonstrates an end-to-end AI application:

```text
Dataset
   ↓
Model Training
   ↓
Image Classification
   ↓
FastAPI API
   ↓
Cloud Deployment
   ↓
Web Application
```

---

# 🌍 Potential Applications

EcoVision can serve as a foundation for future applications such as:

- ♻️ Automated waste segregation
- 🗑️ Smart waste bins
- 🤖 Robotic waste-sorting systems
- 🏭 Industrial recycling systems
- 📱 Waste-identification applications
- 🌱 Environmental education
- 🏙️ Smart-city waste management

---

# 🔮 Future Roadmap

- [ ] Improve dataset quality and diversity
- [ ] Evaluate model using precision, recall and F1-score
- [ ] Generate confusion matrix
- [ ] Experiment with transfer learning
- [ ] Add real-time camera classification
- [ ] Add recycling/disposal recommendations
- [ ] Add mobile application
- [ ] Integrate with robotic waste-sorting systems
- [ ] Explore edge deployment for real-time classification


# ⭐ Support

If you find this project interesting, consider giving the repository a ⭐.

\<p align="center">

### 🌱 Smarter Waste. Cleaner Future.

\<a href="[https://eco-lens-project.lovable.app](https://eco-lens-project.lovable.app)">
\<img src="[https://img.shields.io/badge/TRY%20ECOVISION-22c55e?style=for-the-badge](https://img.shields.io/badge/TRY%20ECOVISION-22c55e?style=for-the-badge)" alt="Try EcoVision">
\</a>

\</p>
