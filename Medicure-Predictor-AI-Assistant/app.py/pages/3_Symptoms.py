import streamlit as st
import json

from modules.background import set_medical_background
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

# -----------------------------------
# Page Setup
# -----------------------------------

st.set_page_config(
    page_title="Symptoms",
    page_icon="🩺",
    layout="wide"
)

set_medical_background()

# -----------------------------------
# Load JSON File
# -----------------------------------

def load_symptoms():

    with open(
        "database/symptoms.json",
        "r"
    ) as file:

        return json.load(file)



symptom_data = load_symptoms()



# -----------------------------------
# Title
# -----------------------------------

st.title(
    "🩺 Select Your Symptoms"
)


st.write(
    "Select the symptoms you are experiencing."
)



st.divider()



# -----------------------------------
# Search Feature
# -----------------------------------

search = st.text_input(
    "🔍 Search Symptom"
)



selected_symptoms = []



# -----------------------------------
# Display Symptoms
# -----------------------------------

st.subheader(
    "Symptom Categories"
)



for category, symptoms in symptom_data.items():


    with st.expander(
        "📂 " + category
    ):


        for symptom in symptoms:


            if search.lower() in symptom.lower():


                checked = st.checkbox(
                    symptom
                )


                if checked:

                    selected_symptoms.append(
                        symptom
                    )



st.divider()



# -----------------------------------
# Buttons
# -----------------------------------


col1, col2 = st.columns(2)



with col1:

    if st.button(
        "🧹 Clear Selection"
    ):

        st.rerun()



with col2:

    if st.button(
        "💾 Save Symptoms & Continue",
        use_container_width=True
    ):


        if len(selected_symptoms) == 0:

            st.error(
                "Please select at least one symptom."
            )

        else:


            st.session_state.symptoms = selected_symptoms


            st.success(
                "Symptoms saved!"
            )


            st.switch_page(
                "pages/4_Prediction.py"
            )



# -----------------------------------
# Show Selected Symptoms
# -----------------------------------


if selected_symptoms:


    st.subheader(
        "Selected Symptoms"
    )


    for s in selected_symptoms:

        st.success(
            "✔ " + s
        )



# -----------------------------------
# Back Button
# -----------------------------------

if st.button(
    "⬅ Back"
):

    st.switch_page(
        "pages/2_Patient_Information.py"
    )
