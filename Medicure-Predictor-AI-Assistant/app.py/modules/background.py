import streamlit as st


def set_medical_background():

    st.markdown(
        """
        <style>

        /* =========================================
           MEDICAL BACKGROUND
        ========================================= */

        .stApp {

            background-image:
                linear-gradient(
                    rgba(255, 255, 255, 0.78),
                    rgba(255, 255, 255, 0.78)
                ),
                url("assets/medical_background.jpg");

            background-size: cover;

            background-position: center;

            background-attachment: fixed;

            min-height: 100vh;
        }


        /* =========================================
           MAIN CONTENT
        ========================================= */

        .main .block-container {

            background: rgba(255, 255, 255, 0.35);

            border-radius: 20px;

            padding: 2rem;

        }


        /* =========================================
           WHITE CARDS
        ========================================= */

        .medical-card {

            background: rgba(255, 255, 255, 0.92);

            padding: 25px;

            border-radius: 20px;

            box-shadow:
                0px 5px 20px
                rgba(0, 0, 0, 0.12);

            margin-bottom: 20px;

        }


        /* =========================================
           HEADINGS
        ========================================= */

        h1, h2, h3 {

            color: #006994;

        }


        /* =========================================
           SIDEBAR
        ========================================= */

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
