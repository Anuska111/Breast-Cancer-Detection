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

---

## 📊 Dataset Distribution

| Dataset Split | Number of Images |
|---|---:|
| Total Images | **1,578** |
| Training Images | **1,263** |
| Validation Images | **315** |

### Class Distribution

| Class | Description |
|---|---|
| 🟢 Benign | Benign breast ultrasound images |
| 🔴 Malignant | Malignant breast ultrasound images |
| 🔵 Normal | Normal breast ultrasound images |

---

## 🧠 Model Architecture

| Component | Details |
|---|---|
| Model Type | Convolutional Neural Network (CNN) |
| Input Size | **128 × 128 × 3** |
| Input Type | RGB Image |
| Number of Classes | **3** |
| Classes | Benign, Malignant, Normal |
| Activation | ReLU + Softmax |
| Loss Function | Categorical Crossentropy |
| Optimizer | Adam |
| Output | 3-Class Probability Distribution |

---

## 📈 Model Performance

| Metric | Score |
|---|---:|
| Validation Accuracy | **84.13%** |
| ROC-AUC Score | **0.91** |
| Validation Samples | **315** |

### Classification Report

| Class | Precision | Recall | F1-Score | Support |
|---|---:|---:|---:|---:|
| 🟢 Benign | 0.81 | 0.92 | 0.86 | 168 |
| 🔴 Malignant | 0.82 | 0.67 | 0.74 | 82 |
| 🔵 Normal | 0.96 | 0.85 | 0.90 | 65 |
| **Overall Accuracy** | **0.84** | | **0.84** | **315** |
| **Macro Average** | **0.87** | **0.81** | **0.83** | **315** |
| **Weighted Average** | **0.85** | **0.84** | **0.84** | **315** |

---

## 🔬 Prediction Output

The CNN generates a probability for each class.

| Class | Example Probability |
|---|---:|
| 🟢 Benign | 12% |
| 🔴 Malignant | **81%** |
| 🔵 Normal | 7% |
| **Final Prediction** | **🔴 Malignant** |

> The final prediction is the class with the highest model probability.

---

## 🎯 Confidence Interpretation

| Model Confidence | Interpretation |
|---|---|
| 🟢 **80% – 100%** | High model confidence |
| 🟡 **60% – 79%** | Moderate model confidence |
| 🔴 **Below 60%** | Lower model confidence |

> **Note:** These values represent model confidence and are not medical risk percentages.

---

## 📦 Model Optimization

| Model Version | Size |
|---|---:|
| Original CNN Model | **~37.87 MB** |
| Float16 TFLite Model | **~6.31 MB** |
| Size Reduction | **~83%** |

The trained CNN was converted into a **TensorFlow Lite Float16 model** to significantly reduce the model size and make deployment more lightweight.

---

## 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Programming Language | **Python** |
| Deep Learning | **TensorFlow / Keras** |
| Model | **CNN** |
| Numerical Computing | **NumPy** |
| Image Processing | **Pillow** |
| Web Framework | **Streamlit** |
| Model Optimization | **TensorFlow Lite** |
| Development Environment | **Google Colab / PyCharm** |
| Version Control | **Git & GitHub** |
| Deployment | **Streamlit Community Cloud** |

---

## 🗂️ Project Structure

| File | Purpose |
|---|---|
| `app.py` | Streamlit web application |
| `main.py` | Main Python project/model code |
| `tumor_cnn_float16.tflite` | Compressed CNN model |
| `best_tumor_cnn.keras` | Best trained CNN model |
| `breast_cancer_cnn_model.keras` | CNN model |
| `breast_cancer_model.keras` | Trained model |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Files excluded from GitHub |
| `README.md` | Project documentation |

---

## 🔄 End-to-End Pipeline

| Stage | Process |
|---|---|
| 1️⃣ | Dataset Collection |
| 2️⃣ | Image Preprocessing |
| 3️⃣ | Image Resizing to **128 × 128** |
| 4️⃣ | Pixel Normalization |
| 5️⃣ | Train/Validation Split |
| 6️⃣ | CNN Model Training |
| 7️⃣ | Model Evaluation |
| 8️⃣ | Classification Report |
| 9️⃣ | ROC-AUC Evaluation |
| 🔟 | CNN Model Compression |
| 1️⃣1️⃣ | TensorFlow Lite Conversion |
| 1️⃣2️⃣ | Streamlit Application |
| 1️⃣3️⃣ | Cloud Deployment |

---

## ⚠️ Medical Disclaimer

> **BreastCare AI is an educational and research project.**
>
> The predictions generated by this application are **not a medical diagnosis** and should not replace professional medical examination, radiological interpretation, biopsy, or clinical decision-making.
>
> The percentages displayed by the application represent **CNN model probabilities**, not actual medical risk percentages.

---

## 🔮 Future Improvements

| Planned Improvement | Purpose |
|---|---|
| Grad-CAM | Visual model explainability |
| Transfer Learning | Improve feature extraction |
| Data Augmentation | Improve model generalization |
| Class Balancing | Reduce class imbalance |
| External Test Set | Better performance validation |
| Model Calibration | Improve probability reliability |
| Explainable AI | Understand model decisions |
| Clinical Validation | Evaluate real-world applicability |

---

## 👩‍💻 Author

**Anuska Biswas**

**B.Tech — Mechanical Engineering**  
**IIT (BHU), Varanasi**

**Interests:** Data Science • Machine Learning • Deep Learning •

---

## 🚀 Live Demo

**Try the application:**  
https://breast-cancer-detection-j2qoy4gbm46kuhurpeblq9.streamlit.app/

---

⭐ **If you found this project interesting, feel free to explore the repository and try the live demo.**
