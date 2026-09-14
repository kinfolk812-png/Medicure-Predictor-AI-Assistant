def get_safety_info(disease, severity):


    safety_database = {


        "High":
        {
            "Warning":
            "⚠ This condition may require medical supervision.",

            "Advice":
            "Do not self-medicate. Consult a qualified doctor.",

            "Medicine":
            "Take medicines only as prescribed by a healthcare professional."
        },


        "Emergency":
        {
            "Warning":
            "🚨 Emergency condition detected.",

            "Advice":
            "Seek immediate medical attention.",

            "Medicine":
            "Avoid taking unknown medicines without medical advice."
        },


        "Medium":
        {
            "Warning":
            "This condition may require monitoring.",

            "Advice":
            "Consult a doctor if symptoms continue or worsen.",

            "Medicine":
            "Do not start medicines without proper guidance."
        },


        "Low":
        {
            "Warning":
            "Usually manageable but monitor symptoms.",

            "Advice":
            "Maintain healthy habits and seek advice if needed.",

            "Medicine":
            "Avoid unnecessary medication."
        }

    }


    return safety_database.get(
        severity,
        {

            "Warning":
            "Consult a healthcare professional.",

            "Advice":
            "Monitor your health.",

            "Medicine":
            "Do not self-medicate."

        }
    )
