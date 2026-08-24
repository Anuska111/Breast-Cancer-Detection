
import streamlit as st
import tflite_runtime.interpreter as tflite
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="BreastCare AI",
    page_icon="🎗️",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
.result-box {
    padding: 20px;
    border-radius: 15px;
    background: rgba(255,255,255,0.05);
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.title("🎗️ BreastCare AI")
st.caption("Breast Ultrasound Classification using Deep Learning")
st.divider()

section = st.radio(
    "Select Section",
    ["🩻 AI Diagnosis", "📊 Result Guide"],
    horizontal=True
)

st.divider()


@st.cache_resource
def load_model():
    interpreter = tflite.Interpreter(
    model_path="tumor_cnn_float16.tflite"
)
    interpreter.allocate_tensors()

    return (
        interpreter,
        interpreter.get_input_details(),
        interpreter.get_output_details()
    )


try:
    interpreter, input_details, output_details = load_model()
except Exception as e:
    st.error("CNN model could not be loaded.")
    st.code(str(e))
    st.stop()


def predict(image):

    image = image.convert("RGB")
    image = image.resize((128, 128))

    image = np.array(image).astype(np.float32)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    interpreter.set_tensor(
        input_details[0]["index"],
        image
    )

    interpreter.invoke()

    prediction = interpreter.get_tensor(
        output_details[0]["index"]
    )[0]

    predicted_index = int(np.argmax(prediction))

    return predicted_index, prediction


if section == "🩻 AI Diagnosis":

    st.header("🩻 Ultrasound Image Analysis")

    left, right = st.columns(2)

    with left:

        st.subheader("📤 Upload Image")

        uploaded_file = st.file_uploader(
            "Choose ultrasound image",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded_file:

            image = Image.open(uploaded_file)

            st.image(
                image,
                caption="Uploaded Ultrasound",
                use_container_width=True
            )

    with right:

        st.subheader("🧠 CNN Prediction")

        if uploaded_file:

            if st.button(
                "🔍 Analyze Image",
                use_container_width=True
            ):

                with st.spinner("Running CNN inference..."):

                    predicted_index, probabilities = predict(
                        image
                    )

                classes = [
                    "Benign",
                    "Malignant",
                    "Normal"
                ]

                prediction = classes[predicted_index]

                confidence = (
                    float(probabilities[predicted_index])
                    * 100
                )

                st.markdown(
                    '<div class="result-box">',
                    unsafe_allow_html=True
                )

                st.subheader("AI Classification")

                if prediction == "Benign":
                    st.success("🟢 BENIGN")

                elif prediction == "Malignant":
                    st.error("🔴 MALIGNANT")

                else:
                    st.info("🔵 NORMAL")

                st.metric(
                    "Model Confidence",
                    f"{confidence:.2f}%"
                )

                st.markdown("</div>", unsafe_allow_html=True)

                st.write("### 📊 Class Probabilities")

                for i, class_name in enumerate(classes):

                    probability = (
                        float(probabilities[i]) * 100
                    )

                    st.write(
                        f"**{class_name}** — "
                        f"{probability:.2f}%"
                    )

                    st.progress(
                        float(probabilities[i])
                    )

                st.write("### 💡 Model Interpretation")

                if confidence >= 80:

                    st.success(
                        f"The model strongly favors "
                        f"**{prediction}** "
                        f"({confidence:.2f}%)."
                    )

                elif confidence >= 60:

                    st.warning(
                        f"The model moderately favors "
                        f"**{prediction}** "
                        f"({confidence:.2f}%)."
                    )

                else:

                    st.warning(
                        f"The model has relatively low "
                        f"confidence in **{prediction}** "
                        f"({confidence:.2f}%)."
                    )

        else:

            st.info(
                "Upload an image to start prediction."
            )

    st.divider()

    st.warning(
        "⚠️ This application is for educational and "
        "research purposes only. It should not be used "
        "as a medical diagnosis."
    )


else:

    st.header("📊 CNN Result Guide")

    st.write(
        "These percentages represent the CNN model's "
        "classification probabilities."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("🟢 High Confidence")
        st.write("80% – 100%")
        st.write(
            "The CNN strongly favors the predicted class."
        )

    with col2:
        st.warning("🟡 Moderate Confidence")
        st.write("60% – 79%")
        st.write(
            "The CNN moderately favors the predicted class."
        )

    with col3:
        st.error("🔴 Low Confidence")
        st.write("Below 60%")
        st.write(
            "The model is less certain."
        )

    st.divider()

    st.subheader("🔬 Classification Categories")

    tab1, tab2, tab3 = st.tabs(
        ["🟢 Benign", "🔴 Malignant", "🔵 Normal"]
    )

    with tab1:

        st.success("### 🟢 Benign")

        st.write(
            "The CNN assigns the highest probability "
            "to the Benign class."
        )

        st.info(
            "Example: Benign 85% | Malignant 10% | Normal 5%"
        )

    with tab2:

        st.error("### 🔴 Malignant")

        st.write(
            "The CNN assigns the highest probability "
            "to the Malignant class."
        )

        st.info(
            "Example: Benign 8% | Malignant 87% | Normal 5%"
        )

    with tab3:

        st.info("### 🔵 Normal")

        st.write(
            "The CNN assigns the highest probability "
            "to the Normal class."
        )

        st.info(
            "Example: Benign 5% | Malignant 7% | Normal 88%"
        )

    st.divider()

    st.subheader("⚠️ Important")

    st.warning(
        "CNN probabilities are model outputs, not "
        "medical risk percentages or clinical diagnoses."
    )

    st.write("Example CNN output:")

    st.code("""
Benign      : 12%
Malignant   : 81%
Normal      :  7%
""")

    st.write(
        "The predicted class is **Malignant** because "
        "it has the highest probability."
    )

st.divider()

st.caption(
    "🎗️ BreastCare AI | Python • Streamlit • CNN • Deep Learning"
)

