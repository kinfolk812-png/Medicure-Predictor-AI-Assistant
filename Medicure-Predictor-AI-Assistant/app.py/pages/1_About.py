import streamlit as st

from modules.background import set_medical_background

st.set_page_config(
    page_title="About - Medicure Predictor",
    page_icon="🩺",
    layout="wide"
)

set_medical_background()

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

st.markdown(
"""
<style>

.about-card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.12);
}

.title {
    color: #0077b6;
    text-align: center;
    font-size: 40px;
    font-weight: bold;
}

.subtitle {
    color: #023e8a;
    text-align: center;
    font-size: 20px;
}

</style>
""",
unsafe_allow_html=True
)


st.markdown(
"""
<div class="title">
🩺 Medicure Predictor
</div>

<div class="subtitle">
AI-Powered Healthcare Assistance System
</div>
""",
unsafe_allow_html=True
)


st.write("")


st.markdown(
"""
<div class="about-card">

<h2>🤖 What is Medicure Predictor?</h2>

<p>
Medicure Predictor is an AI-based healthcare assistance
application designed to analyze user-provided symptoms
and identify possible health conditions.
</p>

<p>
The system also provides health information, BMI analysis,
safety guidance and recommendations for seeking professional
medical assistance.
</p>

</div>
""",
unsafe_allow_html=True
)


st.markdown(
"""
<div class="about-card">

<h2>🎯 Objectives</h2>

<ul>

<li>Analyze user-selected symptoms.</li>

<li>Identify possible diseases.</li>

<li>Provide useful health information.</li>

<li>Calculate BMI when height and weight are provided.</li>

<li>Identify potentially urgent symptoms.</li>

<li>Generate a health report.</li>

</ul>

</div>
""",
unsafe_allow_html=True
)


st.markdown(
"""
<div class="about-card">

<h2>⚙️ Main Features</h2>

<ul>

<li>🧠 AI Disease Prediction</li>

<li>📊 Confidence Score</li>

<li>❤️ BMI Analysis</li>

<li>🚨 Emergency Risk Detection</li>

<li>👨‍⚕️ Specialist Recommendation</li>

<li>💊 Medicine Safety Guidance</li>

<li>📄 Health Report Generation</li>

</ul>

</div>
""",
unsafe_allow_html=True
)


st.warning(
"""
⚠️ Medical Disclaimer

Medicure Predictor is an educational and health-assistance
system. It does not replace a qualified doctor or medical
diagnosis.

Do not use the system to self-prescribe medicines.
For serious, persistent or emergency symptoms, seek
professional medical care.
"""
)
