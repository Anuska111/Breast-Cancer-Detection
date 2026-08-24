# 🎗️ BreastCare AI — Breast Ultrasound Classification 

<p align="center">
  <b>Deep Learning Based Breast Ultrasound Image Classification</b>
</p>

<p align="center">
  🚀 <a href="https://breast-cancer-detection-j2qoy4gbm46kuhurpeblq9.streamlit.app/">Live Demo</a>
</p>

---

## 📌 Overview

**BreastCare AI** is a Deep Learning project that uses a **Convolutional Neural Network (CNN)** to classify breast ultrasound images into three categories:

- 🟢 Benign
- 🔴 Malignant
- 🔵 Normal

The project includes image preprocessing, CNN training, model evaluation, probability-based classification, model compression using TensorFlow Lite, and deployment using Streamlit.

---

## 🚀 Live Demo

👉 https://breast-cancer-detection-j2qoy4gbm46kuhurpeblq9.streamlit.app/

---

## ✨ Features

- Breast ultrasound image upload
- CNN-based image classification
- Three-class classification
- Class probability visualization
- Prediction confidence
- Confidence-level interpretation
- TensorFlow Lite model optimization
- Streamlit web application
- Streamlit Cloud deployment
- Python-based implementation

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/ANN-FF6F00?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/CNN-8A2BE2?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/TensorFlow_Lite-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
</p>

---

## 🧠 Deep Learning Workflow

```text
Breast Ultrasound Dataset
          ↓
Image Preprocessing
          ↓
Resize → 128 × 128
          ↓
Normalization
          ↓
Train / Validation Split
          ↓
CNN Training
          ↓
Model Evaluation
          ↓
ROC-AUC Evaluation
          ↓
TensorFlow Lite Compression
          ↓
Streamlit Deployment
```
📊 Dataset Distribution
| Dataset Split  | Number of Images | Percentage |
| -------------- | ---------------: | ---------: |
| Training Set   |            1,263 |        80% |
| Validation Set |              315 |        20% |
| Total          |        **1,578** |   **100%** |

### Class Distribution

| Class | Description |
|---|---|
| Benign | Benign breast ultrasound images |
| Malignant | Malignant breast ultrasound images |
| Normal | Normal breast ultrasound images |

## 🧠 Model Architecture

| Component | Details |
|---|---|
| Model Type | Convolutional Neural Network (CNN) |
| Input Size | 128 × 128 × 3 |
| Input Format | RGB |
| Number of Classes | 3 |
| Classes | Benign, Malignant, Normal |
| Activation | ReLU + Softmax |
| Loss Function | Categorical Crossentropy |
| Optimizer | Adam |
| Output | 3-Class Probability Distribution |

## 📈 Model Performance

| Metric | Score |
|---|---:|
| Validation Accuracy | **84.13%** |
| ROC-AUC Score | **0.91** |
| Validation Samples | **315** |

### Classification Report

| Class | Precision | Recall | F1-Score | Support |
|---|---:|---:|---:|---:|
| Benign | 0.81 | 0.92 | 0.86 | 168 |
| Malignant | 0.82 | 0.67 | 0.74 | 82 |
| Normal | 0.96 | 0.85 | 0.90 | 65 |
| **Accuracy** | — | — | **0.84** | **315** |
| **Macro Average** | **0.87** | **0.81** | **0.83** | **315** |
| **Weighted Average** | **0.85** | **0.84** | **0.84** | **315** |

## 🔬 Prediction Output

The CNN generates a probability distribution across all three classes.

| Class | Example Probability |
|---|---:|
| Benign | 12% |
| Malignant | **81%** |
| Normal | 7% |
| **Final Prediction** | **Malignant** |

## 🎯 Confidence Interpretation

| Model Confidence | Interpretation |
|---|---|
| 80% – 100% | High model confidence |
| 60% – 79% | Moderate model confidence |
| Below 60% | Lower model confidence |

> **Note:** Model confidence should not be interpreted as medical risk or diagnostic certainty.

## 📦 Model Optimization

| Model Version | Size |
|---|---:|
| Original CNN Model | ~37.87 MB |
| Float16 TFLite Model | **~6.31 MB** |
| Size Reduction | **~83%** |

The trained CNN was converted into a **TensorFlow Lite Float16 model** to reduce the model size and make deployment more lightweight.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Deep Learning | TensorFlow, Keras |
| Architecture | CNN |
| Numerical Computing | NumPy |
| Image Processing | Pillow |
| Web Application | Streamlit |
| Model Optimization | TensorFlow Lite |
| Development | Google Colab, PyCharm |
| Version Control | Git, GitHub |
| Deployment | Streamlit Community Cloud |

## 🗂️ Project Structure

```text
Breast-Cancer-Detection/
│
├── app.py
├── main.py
├── tumor_cnn_float16.tflite
├── best_tumor_cnn.keras
├── breast_cancer_cnn_model.keras
├── breast_cancer_model.keras
├── scaler.pkl
├── requirements.txt
├── pyproject.toml
├── .gitignore
└── README.md


###  End-to-End Pipeline

```markdown
## 🔄 End-to-End Pipeline

| Step | Process |
|---:|---|
| 1 | Dataset Collection |
| 2 | Image Preprocessing |
| 3 | Resize Images to 128 × 128 |
| 4 | Pixel Normalization |
| 5 | Train/Validation Split |
| 6 | CNN Model Training |
| 7 | Model Evaluation |
| 8 | Classification Report |
| 9 | ROC-AUC Evaluation |
| 10 | Model Compression |
| 11 | TensorFlow Lite Conversion |
| 12 | Streamlit Application |
| 13 | Cloud Deployment |
```
## 🚀 Deployment

The application is deployed using **Streamlit Community Cloud**.

### Live Demo

**[🎗️ Launch BreastCare AI](https://breast-cancer-detection-j2qoy4gbm46kuhurpeblq9.streamlit.app/)**

## ⚠️ Medical Disclaimer

**BreastCare AI is an educational and research project.**

The predictions generated by this application are **not a medical diagnosis** and should not replace professional medical examination, radiological interpretation, biopsy, or clinical decision-making.

The probabilities displayed by the application represent **CNN model output probabilities**, not actual medical risk percentages.

## 🔮 Future Improvements

| Improvement | Goal |
|---|---|
| Grad-CAM | Visual model explainability |
| Transfer Learning | Improve feature extraction |
| Data Augmentation | Improve generalization |
| Class Balancing | Handle class imbalance |
| External Test Set | More robust evaluation |
| Model Calibration | Improve probability reliability |
| Explainable AI | Better understand predictions |
| Clinical Validation | Evaluate real-world applicability |

## 👩‍💻 Author

### Anuska Biswas

**B.Tech — Mechanical Engineering**  
**IIT (BHU), Varanasi**

**Interests:** Data Science • Machine Learning • Deep Learning •

## ⭐ Project Highlights

**BreastCare AI** combines:

**CNN + TensorFlow + Keras + ANN + TensorFlow Lite + Streamlit**

to create an end-to-end breast ultrasound image classification application.

### 🚀 Try the Live Application

**[🎗️ BreastCare AI — Open Live Demo](https://breast-cancer-detection-j2qoy4gbm46kuhurpeblq9.streamlit.app/)**
