import json


def load_information():

    with open(
        "database/disease_information.json",
        "r"
    ) as file:

        return json.load(file)



def get_disease_info(disease):

    data = load_information()


    if disease in data:

        return data[disease]


    else:

        return {

            "Description":
            "Information will be updated soon.",

            "Causes":
            [],

            "Prevention":
            [],

            "Care":
            [],

            "Warning Signs":
            []

        }
