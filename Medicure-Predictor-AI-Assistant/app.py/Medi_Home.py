import streamlit as st

from modules.background import set_medical_background


st.set_page_config(
    page_title="Medicure Predictor",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
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


# =========================================================
# HERO SECTION
# =========================================================

st.markdown(
    """
    <div style="
        background: linear-gradient(135deg, #0077b6, #00b4d8);
        padding: 25px;
        border-radius: 35px;
        color: White;
        text-align: center;
        box-shadow: 0px 8px 25px rgba(0,119,182,0.55);
    ">

            🩺 Welcome to Medicure Predictor
        
            An AI-powered healthcare assistance system
            designed to analyze symptoms and provide useful
            health guidance.
        
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# MEDICAL IMAGE
# =========================================================

try:

    st.image(
        "assets/medical_banner.jpg",
        use_container_width=True
    )

except:

    st.info(
        "Add your medical_banner.jpg inside the assets folder."
    )


st.write("")


# =========================================================
# INTRODUCTION
# =========================================================

st.markdown(
    """
    <div class="main-title">
    Medicure Predictor
    </div>

    <div class="subtitle">
    Your Intelligent Health Prediction Companion
    </div>
    """,
    unsafe_allow_html=True
)


st.write(
    """
    Medicure Predictor uses symptom-based analysis to
    identify possible health conditions and provide
    general health information.
    """
)


# =========================================================
# FEATURES
# =========================================================

st.header("✨ What Medicure Predictor Offers")


col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        """
        <div class="feature-card">
            🧠
            
            AI Prediction
            
            Analyze symptoms and identify
            possible health conditions.
            
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
        <div class="feature-card">
            ❤️
            
            Health Analysis
            
            Check BMI and receive
            general health recommendations.

        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        """
        <div class="feature-card">
            🚨
            
            Safety Detection
            
            Identify potentially serious
            symptoms and seek appropriate care.
            
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# SECOND ROW
# =========================================================

st.write("")


col4, col5, col6 = st.columns(3)


with col4:

    st.markdown(
        """
        <div class="feature-card">
            👨‍⚕️
            
            Specialist Guidance

            Receive general guidance about
            which type of healthcare specialist
            may be appropriate.

        </div>
        """,
        unsafe_allow_html=True
    )


with col5:

    st.markdown(
        """
        <div class="feature-card">
            📄
            
            Health Report

            Create a report containing
            your entered information and results.

        </div>
        """,
        unsafe_allow_html=True
    )


with col6:

    st.markdown(
        """
        <div class="feature-card">
            💊
            
            Medicine Safety
            
            Provides safety reminders and
            discourages self-medication.

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# HOW IT WORKS
# =========================================================

st.write("")

st.header("⚙️ How It Works")


c1, c2, c3, c4 = st.columns(4)


steps = [
    ("01", "👤", "Enter Details"),
    ("02", "🩺", "Select Symptoms"),
    ("03", "🧠", "AI Analysis"),
    ("04", "📄", "View Results")
]


for column, step in zip(
    [c1, c2, c3, c4],
    steps
):

    number, icon, title = step

    with column:

        st.markdown(
            f"""
            <div class="step-card">
                {number}
                
                {icon}
                {title}

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# PRIVACY
# =========================================================

st.write("")

st.header("🔐 Privacy & Anonymous Use")

st.info(
    """
    Medicure Predictor is designed for anonymous use.
    Users do not need to create a username or password
    to use the prediction system.
    """
)


# =========================================================
# MEDICAL DISCLAIMER
# =========================================================

st.write("")

st.warning(
    """
    ⚠️ Medical Disclaimer

    Medicure Predictor is an educational and health-assistance
    application. Its predictions and recommendations should
    not be considered a medical diagnosis or a substitute
    for professional healthcare.

    Do not self-prescribe medicines based on the application.
    For serious, persistent or emergency symptoms, contact
    a qualified healthcare professional.
    """
)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

        🩺 Medicure Predictor AI

        AI-Based Healthcare Assistance System

        Built for educational purposes

    </div>
    """,
    unsafe_allow_html=True
)
