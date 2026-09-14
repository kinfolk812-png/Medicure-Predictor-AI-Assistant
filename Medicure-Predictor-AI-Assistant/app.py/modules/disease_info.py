import json
from pathlib import Path


def load_information():

    base_dir = Path(__file__).resolve().parent.parent

    information_file = base_dir / "database" / "disease_information.json"

    with open(
        information_file,
        "r",
        encoding="utf-8"
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
