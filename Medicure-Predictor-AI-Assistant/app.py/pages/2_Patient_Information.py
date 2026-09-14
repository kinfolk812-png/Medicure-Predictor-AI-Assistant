import streamlit as st

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
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Patient Information",
    page_icon="👤",
    layout="wide"
)

set_medical_background()


# -----------------------------------
# Functions
# -----------------------------------

def calculate_bmi(height, weight):

    if height > 0 and weight > 0:

        height_meter = height / 100

        bmi = weight / (height_meter ** 2)

        return round(bmi, 2)

    return None



def bmi_category(bmi):

    if bmi is None:
        return "Not Calculated"

    elif bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal Weight"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obesity"



def age_group(age):

    if age < 13:
        return "Child"

    elif age < 20:
        return "Teenager"

    elif age < 60:
        return "Adult"

    else:
        return "Senior Citizen"



# -----------------------------------
# Title
# -----------------------------------

st.title("👤 Patient Information")

st.write(
    "Please enter your basic details before starting symptom analysis."
)


st.divider()


# -----------------------------------
# Patient Form
# -----------------------------------

col1, col2 = st.columns(2)


with col1:

    name = st.text_input(
        "Name (Optional)"
    )


    age = st.number_input(
        "Age *",
        min_value=1,
        max_value=120,
        value=18
    )


    gender = st.selectbox(
        "Gender *",
        [
            "Male",
            "Female",
            "Other"
        ]
    )


with col2:

    height = st.number_input(
        "Height (cm) Optional",
        min_value=0,
        max_value=250,
        value=0
    )


    weight = st.number_input(
        "Weight (kg) Optional",
        min_value=0,
        max_value=300,
        value=0
    )



# -----------------------------------
# BMI Calculation
# -----------------------------------

st.subheader("📊 Health Summary")


bmi = calculate_bmi(
    height,
    weight
)


col3, col4, col5 = st.columns(3)


with col3:

    st.metric(
        "BMI",
        bmi if bmi else "Not Entered"
    )


with col4:

    st.metric(
        "BMI Category",
        bmi_category(bmi)
    )


with col5:

    st.metric(
        "Age Group",
        age_group(age)
    )



st.divider()


# -----------------------------------
# Save Data
# -----------------------------------

if st.button(
    "💾 Save & Continue",
    use_container_width=True
):

    if age <= 0:

        st.error(
            "Please enter valid age"
        )

    else:

        st.session_state.patient = {

            "Name": name,

            "Age": age,

            "Gender": gender,

            "Height": height,

            "Weight": weight,

            "BMI": bmi,

            "BMI Category": bmi_category(bmi),

            "Age Group": age_group(age)

        }


        st.success(
            "Patient information saved successfully!"
        )


        st.switch_page(
            "pages/3_Symptoms.py"
        )



# -----------------------------------
# Back Button
# -----------------------------------

if st.button("⬅ Back"):

    st.switch_page(
        "Medi_Home.py"
    )
