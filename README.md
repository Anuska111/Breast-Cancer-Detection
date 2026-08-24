
┌────────────────────────────────────────────────────────────┐
│                  END-TO-END WORKFLOW                       │
├────────────────────────────────────────────────────────────┤
│ 1️⃣ Data Collection : 1,578 images (Benign/Malignant/Normal) │
│ 2️⃣ Preprocessing   : Resize to 128x128 & normalize pixels  │
│ 3️⃣ Partitioning    : 80% Training / 20% Validation split    │
│ 4️⃣ CNN Training    : Feature extraction + Dropout + Adam   │
│ 5️⃣ Evaluation      : Classification report & ROC-AUC score │
│ 6️⃣ Compression     : Convert to TFLite Float16 (6.31 MB)   │
│ 7️⃣ Deployment      : Host live on Streamlit Cloud          │
└────────────────────────────────────────────────────────────┘
