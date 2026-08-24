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

The project covers image preprocessing, CNN training, model evaluation, probability-based classification, model compression using TensorFlow Lite, and deployment using Streamlit.

---

## 🚀 Live Demo

👉 https://breast-cancer-detection-j2qoy4gbm46kuhurpeblq9.streamlit.app/

---
---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/ANN-FF6F00?style=for-the-badge&logo=googlecloud&logoColor=white" />
  <img src="https://img.shields.io/badge/CNN-8A2BE2?style=for-the-badge&logo=tensorflow&logoColor=white" />
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" />
  <img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Pillow-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/TensorFlow_Lite-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
</p>

## ✨ Features

- 🩻 Breast ultrasound image upload
- 🧠 CNN-based image classification
- 🔬 Three-class classification
- 📊 Class probability visualization
- 🎯 Prediction confidence
- 💡 Confidence-level interpretation
- 📦 TensorFlow Lite model optimization
- 🌐 Streamlit web application
- ☁️ Streamlit Cloud deployment
- 🐍 Python-based implementation

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

# 🎗️ BreastCare AI — Ultrasound Breast Tumor Classification

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://breast-cancer-detection-j2qoy4gbm46kuhurpeblq9.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=flat&logo=github)](https://github.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An end-to-end deep learning pipeline and interactive web interface designed for the multi-class classification of breast ultrasound images into **Benign**, **Malignant**, and **Normal** tissue categories. The application leverages an optimized, quantized **TensorFlow Lite (Float16)** architecture deployed to the cloud for real-time edge inference.

---

## 🚀 Live Demo

Experience the production web application here:  
👉 **[Launch BreastCare AI Interactive Web App](https://breast-cancer-detection-j2qoy4gbm46kuhurpeblq9.streamlit.app/)**

---

## 📊 Dataset Overview

The dataset consists of high-resolution ultrasound scans categorized into three diagnostic classes.

### Dataset Distribution

| Split | Number of Images | Percentage |
| :--- | :---: | :---: |
| 🧠 **Training Set** | 1,263 | 80% |
| 🧪 **Validation Set** | 315 | 20% |
| 📦 **Total Dataset** | **1,578** | **100%** |

### Class Categorization

| Class | Diagnostic Description |
| :--- | :--- |
| 🟢 **Benign** | Non-cancerous lesions or structural fibroadenomas |
| 🔴 **Malignant** | Invasive or high-grade cancerous tissue requiring clinical intervention |
| 🔵 **Normal** | Healthy, non-pathological breast tissue architecture |

---

## 🧠 Model Architecture & Specifications

| Parameter | Configuration |
| :--- | :--- |
| **Architecture Type** | Deep Convolutional Neural Network (1D/2D CNN) |
| **Input Resolution** | `128 × 128 × 3` (RGB) |
| **Classification Strategy** | 3-Class Categorical Softmax |
| **Activation Functions** | Rectified Linear Unit (ReLU), Softmax |
| **Loss Function** | Categorical Crossentropy |
| **Optimizer** | Adam ($\beta_1=0.9, \beta_2=0.999$) |
| **Inference Output** | 3-Class Normalized Probability Distribution |

---

## 📈 Performance & Clinical Evaluation

The trained CNN achieved high precision and stability on unseen validation folds:

| Metric | Benchmark Score |
| :--- | :---: |
| **Overall Validation Accuracy** | **84.13%** |
| **Area Under ROC Curve (ROC-AUC)** | **0.91** |
| **Total Validation Samples** | **315** |

### Detailed Classification Report

| Diagnostic Class | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| 🟢 **Benign** | 0.81 | 0.92 | 0.86 | 168 |
| 🔴 **Malignant** | 0.82 | 0.67 | 0.74 | 82 |
| 🔵 **Normal** | 0.96 | 0.85 | 0.90 | 65 |
| **Overall Accuracy** | — | — | **0.84** | **315** |
| **Macro Average** | **0.87** | **0.81** | **0.83** | **315** |
| **Weighted Average** | **0.85** | **0.84** | **0.84** | **315** |

---

## 🔬 Sample Prediction & Output Logic

The network yields normalized output distributions across all label spaces:

| Class | Model Probability | Classification Status |
| :--- | :---: | :---: |
| 🟢 **Benign** | 12.0% | Negative |
| 🔴 **Malignant** | **81.0%** | **Positive (Primary)** |
| 🔵 **Normal** | 7.0% | Negative |
| **Final Diagnosis** | **81.0%** | 🔴 **Malignant** |

### Decision Confidence Matrix

| Confidence Bracket | Classification Category | Interpretation |
| :---: | :--- | :--- |
| 🟢 **80% – 100%** | High Confidence | Strong feature alignment with reference patterns |
| 🟡 **60% – 79%** | Moderate Confidence | Secondary review and feature correlation recommended |
| 🔴 **< 60%** | Inconclusive | Low certainty; manual histopathological validation required |

---

## 📦 Model Optimization & Edge Deployment

Post-training quantization was conducted via **TensorFlow Lite (Float16)** to minimize inference latency and maximize cloud portability.

| Artifact | Format | Binary Size | Compression Ratio |
| :--- | :---: | :---: | :---: |
| Native Keras Graph | `.keras` | ~37.87 MB | Baseline |
| **Float16 Quantized Model** | `.tflite` | **~6.31 MB** | **~83.3% Reduction** |

---

## 🛠️ Technology Stack

| Domain | Frameworks & Tools |
| :--- | :--- |
| **Core Environment** | Python 3.10+ |
| **Deep Learning & Inference** | TensorFlow 2.x, Keras, TensorFlow Lite Runtime |
| **Numerical & Matrix Operations** | NumPy, Pandas, Scikit-Learn |
| **Image Preprocessing** | Pillow (PIL), OpenCV |
| **Web Framework & UI** | Streamlit |
| **Deployment & Versioning** | Streamlit Community Cloud, Git, GitHub |

---

## 🗂️ Repository Structure

```text
Breast-Cancer-Detection/
│
├── app.py                          # Streamlit application UI and pipeline entry point
├── main.py                         # Training, validation, and serialization pipeline
├── tumor_cnn_float16.tflite        # Quantized production TFLite model (~6.31 MB)
├── best_tumor_cnn.keras            # Checkpointed full-precision Keras model
├── breast_cancer_cnn_model.keras   # Pre-trained 1D/2D CNN model weights
├── breast_cancer_model.keras       # Baseline neural network model artifact
├── scaler.pkl                      # Feature standardization parameters
├── requirements.txt                # Production dependency manifest
├── .gitignore                      # Git exclusion rules
└── README.md                       # Comprehensive project documentation
---

