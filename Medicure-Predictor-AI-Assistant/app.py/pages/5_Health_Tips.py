import streamlit as st

from modules.background import set_medical_background


st.set_page_config(
    page_title="Health Tips - Medicure Predictor",
    page_icon="❤️",
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

.tip-card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 18px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.12);
}

h1 {
    color: #0077b6;
}

</style>
""",
unsafe_allow_html=True
)


st.title("❤️ Healthy Lifestyle Tips")

st.write(
"Simple general health practices that can support a healthy lifestyle."
)


col1, col2 = st.columns(2)


with col1:

    st.markdown(
    """
    <div class="tip-card">

    <h2>🥗 Healthy Diet</h2>

    <p>
    Eat a balanced variety of vegetables, fruits,
    whole grains and protein-rich foods.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )


with col2:

    st.markdown(
    """
    <div class="tip-card">

    <h2>💧 Stay Hydrated</h2>

    <p>
    Drink adequate water throughout the day
    according to your individual needs.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )


col3, col4 = st.columns(2)


with col3:

    st.markdown(
    """
    <div class="tip-card">

    <h2>🏃 Physical Activity</h2>

    <p>
    Maintain regular physical activity appropriate
    for your age and fitness level.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )


with col4:

    st.markdown(
    """
    <div class="tip-card">

    <h2>😴 Good Sleep</h2>

    <p>
    Maintain a consistent sleep schedule and
    give your body enough time to rest.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )


st.markdown(
"""
<div class="tip-card">

<h2>🧘 Manage Stress</h2>

<p>
Take regular breaks, maintain social connections
and use healthy methods to manage stress.
</p>

</div>
""",
unsafe_allow_html=True
)


st.info(
"""
These are general health tips and are not intended
to diagnose or treat a medical condition.
"""
)
