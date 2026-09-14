def check_emergency(symptoms):


    emergency_conditions = {


        "Heart Emergency":
        [
            "Chest Pain",
            "Difficulty Breathing",
            "Rapid Heartbeat",
            "Fainting"
        ],


        "Stroke Risk":
        [
            "Weakness",
            "Slurred Speech",
            "Dizziness",
            "Loss of Balance"
        ],


        "Severe Infection":
        [
            "High Fever",
            "Confusion",
            "Extreme Weakness"
        ],


        "Breathing Emergency":
        [
            "Difficulty Breathing",
            "Chest Tightness",
            "Blue Lips"
        ]

    }



    warnings = []


    for condition, signs in emergency_conditions.items():


        count = 0


        for symptom in symptoms:


            if symptom in signs:

                count += 1



        if count >= 2:

            warnings.append(condition)



    return warnings
