import streamlit as st

from modules.predictor import predict_disease

from modules.disease_info import get_disease_info

from modules.report_generator import create_report

from modules.health_advice import (
    calculate_bmi,
    bmi_category,
    health_recommendation
)

from modules.emergency_check import check_emergency

from modules.medicine_safety import get_safety_info

from modules.background import set_medical_background

st.set_page_config(

    page_title="Prediction",

    page_icon="🤖",

    layout="wide"

)

set_medical_background()


st.title(
    "🤖 Medicure Predictor AI Analysis"
)



st.write(
    "Analyzing your selected symptoms..."
)

# =========================================================
# CUSTOM DESIGN
# =========================================================

st.markdown(
    """
    <style>

    /* Main background */

    .stApp {
        background:
        linear-gradient(
            135deg,
            #e0f7ff 0%,
            #f8fbff 45%,
            #fff3e8 100%
        );
    }


    /* Main title */

    .main-title {
        text-align: center;
        font-size: 48px;
        font-weight: 800;
        color: #0066cc;
        margin-top: 10px;
        margin-bottom: 5px;
    }


    .subtitle {
        text-align: center;
        font-size: 21px;
        color: #555555;
        margin-bottom: 30px;
    }


    /* Hero card */

    .hero {
        background:
        linear-gradient(
            135deg,
            #0077b6,
            #00b4d8
        );

        padding: 35px;

        border-radius: 25px;

        color: white;

        box-shadow:
        0px 8px 25px
        rgba(0, 119, 182, 0.25);

        margin-bottom: 30px;
    }


    .hero h1 {
        color: white;
        font-size: 36px;
    }


    .hero p {
        font-size: 18px;
    }


    /* Feature cards */

    .feature-card {

        background: white;

        padding: 25px;

        border-radius: 20px;

        text-align: center;

        min-height: 190px;

        box-shadow:
        0px 5px 18px
        rgba(0,0,0,0.10);

        border-top: 5px solid #00b4d8;
    }


    .feature-icon {
        font-size: 42px;
    }


    .feature-title {
        font-size: 22px;
        font-weight: bold;
        color: #0077b6;
    }


    .feature-text {
        color: #555555;
        font-size: 15px;
    }


    /* How it works */

    .step-card {

        background: white;

        padding: 20px;

        border-radius: 18px;

        box-shadow:
        0px 4px 15px
        rgba(0,0,0,0.08);

        text-align: center;
    }


    .step-number {

        font-size: 30px;

        font-weight: bold;

        color: #ff7b00;
    }


    /* Footer */

    .footer {

        text-align: center;

        padding: 25px;

        margin-top: 40px;

        color: #555555;

        font-size: 14px;
    }


    /* Sidebar */

    section[data-testid="stSidebar"] {

        background:
        linear-gradient(
            180deg,
            #023e8a,
            #0077b6,
            #00b4d8
        );
    }


    section[data-testid="stSidebar"] * {

        color: white !important;
    }


    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <h1 style="text-align:center;">
        🩺
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h2 style="text-align:center;">
        Medicure Predictor
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.write(
        "🧠 AI Disease Prediction"
    )

    st.write(
        "❤️ BMI Analysis"
    )

    st.write(
        "🚨 Emergency Detection"
    )

    st.write(
        "👨‍⚕️ Doctor Recommendation"
    )

    st.write(
        "📄 Health Reports"
    )

    st.write(
        "💊 Medicine Safety"
    )

# Get symptoms

symptoms = st.session_state.get(

    "symptoms",

    []

)



if len(symptoms)==0:


    st.warning(
        "No symptoms selected."
    )


else:


    st.subheader(
        "Selected Symptoms"
    )


    for s in symptoms:

        st.write(
            "✔",
            s
        )



    st.divider()

    st.subheader("👤 Patient Details")


    name = st.text_input(
        "Enter Name"
    )


    age = st.number_input(
        "Enter Age",
        min_value=1,
        max_value=120
    )


    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female",
            "Other"
        ]
    )


    height = st.number_input(
        "Height (cm) Optional",
        min_value=0
    )


    weight = st.number_input(
        "Weight (kg) Optional",
        min_value=0
    )

    # BMI CALCULATION START

    bmi = calculate_bmi(
        height,
        weight
    )


    if bmi is not None:


        category = bmi_category(
            bmi
        )


        st.info(
            f"""
            📊 BMI Result

            BMI: {bmi}

            Category: {category}

            """
        )


        advice = health_recommendation(
            category
        )


        with st.expander(
            "❤️ Health Recommendations"
        ):


            st.write(
                "🥗 Diet:"
            )

            st.write(
                advice["Diet"]
            )


            st.write(
                "🏃 Exercise:"
            )

            st.write(
                advice["Exercise"]
            )


            st.write(
                "💡 Advice:"
            )

            st.write(
                advice["Advice"]
            )

# BMI CALCULATION END


    predictions = predict_disease(

        symptoms

    )

    emergency = check_emergency(symptoms)


    if emergency:


        st.error(
            """
            🚨 EMERGENCY WARNING

            Some symptoms may require immediate medical attention.

            Please consult a doctor.
            """
        )


        for risk in emergency:

            st.warning(
                "Possible Risk: "
                +
                risk
            )

            doctor = {

        "Heart Emergency":
        "Cardiologist",

        "Stroke Risk":
        "Neurologist",

        "Severe Infection":
        "General Physician",

        "Breathing Emergency":
        "Pulmonologist"

    }


    if emergency:


        st.info(
            "Recommended Specialist:"
        )


        for risk in emergency:

            st.write(
                "👨‍⚕️",
                doctor.get(
                    risk,
                    "Doctor"
                )
            )



        st.subheader(
            "Top Possible Conditions"
        )


    for i, result in enumerate(predictions):

        disease = result["Disease"]

        confidence = result.get(
            "Symptom Match Score",
            result.get("Confidence", 0)
        )

        severity = result.get(
            "Severity",
            "Medium"
        )


        safety = get_safety_info(
            disease,
            severity
        )


        with st.expander(
            "⚕️ Medicine Safety & Advice"
        ):


            st.warning(
                safety["Warning"]
            )


            st.info(
                safety["Advice"]
            )


            st.write(
                "💊 Medicine Safety:"
            )


            st.write(
                safety["Medicine"]
            )


        st.success(
            f"""
            ### 🩺 Possible Disease {i+1}

            Disease: {disease}

            Symptom Match Score: {confidence}%

            """
        )


        info = get_disease_info(disease)


        with st.expander("📖 View Disease Information"):

            st.write("### Description")

            st.write(
                info["Description"]
            )


            st.write("### Causes")

            for item in info["Causes"]:

                st.write(
                    "•",
                    item
                )


            st.write("### Prevention")

            for item in info["Prevention"]:

                st.write(
                    "•",
                    item
                )


            st.write("### Basic Care")

            for item in info["Care"]:

                st.write(
                    "•",
                    item
                )


            st.write("### Warning Signs")

            for item in info["Warning Signs"]:

                st.write(
                    "⚠",
                    item
                )
    

    st.divider()


    if st.button("📄 Generate Health Report"):


        report = create_report(

            name,

            age,

            gender,

            height,

            weight,

            predictions

        )


        with open(report,"rb") as file:


            st.download_button(

                label="Download PDF Report",

                data=file,

                file_name="Medicure_Report.pdf",

                mime="application/pdf"

            )


if st.button(
    "⬅ Back to Symptoms"
):

    st.switch_page(

        "pages/3_Symptoms.py"

    )
