import json


def load_diseases():

    files = [
        "database/diseases.json",

        "database/diseases_extra.json",

        "database/diseases_part3.json",

        "database/diseases_part4.json"

    ]

    all_diseases = {}


    for file in files:

        with open(file,"r") as f:

            data = json.load(f)

            all_diseases.update(data)


    return all_diseases



def predict_disease(selected_symptoms):


    diseases = load_diseases()


    results=[]


    for disease,data in diseases.items():


        score=0

        total=0


        for symptom,weight in data["Weights"].items():

            total += weight


            if symptom in selected_symptoms:

                score += weight



        confidence = 0


        if total > 0:

            confidence = (score/total)*100



        results.append({

            "Disease":disease,

            "Confidence":round(confidence,2)

        })



    results.sort(
        key=lambda x: x["Confidence"],
        reverse=True
    )


    return results[:5]
