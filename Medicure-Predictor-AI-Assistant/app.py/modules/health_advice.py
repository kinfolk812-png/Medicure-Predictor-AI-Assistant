def calculate_bmi(height, weight):

    if height == 0 or weight == 0:

        return None


    height_m = height / 100


    bmi = weight / (height_m * height_m)


    return round(bmi, 2)



def bmi_category(bmi):

    if bmi is None:

        return "Not Available"


    if bmi < 18.5:

        return "Underweight"


    elif bmi < 25:

        return "Normal Weight"


    elif bmi < 30:

        return "Overweight"


    else:

        return "Obese"



def health_recommendation(category):


    advice = {


        "Underweight":
        {
            "Diet":
            "Increase protein intake, healthy fats, milk, nuts and balanced meals.",

            "Exercise":
            "Do strength training and light exercises.",

            "Advice":
            "Increase calorie intake with nutritious foods."
        },


        "Normal Weight":
        {
            "Diet":
            "Maintain a balanced diet with fruits, vegetables and proteins.",

            "Exercise":
            "Continue regular physical activity.",

            "Advice":
            "Maintain current healthy lifestyle."
        },


        "Overweight":
        {
            "Diet":
            "Reduce excess sugar and oily foods. Eat more vegetables.",

            "Exercise":
            "Do walking, jogging and cardio exercises.",

            "Advice":
            "Maintain calorie control and active lifestyle."
        },


        "Obese":
        {
            "Diet":
            "Follow a controlled diet plan with medical guidance.",

            "Exercise":
            "Start with walking and gradually increase activity.",

            "Advice":
            "Consult a healthcare professional for weight management."
        }

    }


    return advice.get(
        category,
        {}
    )
