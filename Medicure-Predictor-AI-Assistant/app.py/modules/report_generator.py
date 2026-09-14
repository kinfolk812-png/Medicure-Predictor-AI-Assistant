from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime



def create_report(
        name,
        age,
        gender,
        height,
        weight,
        predictions
):

    filename = "Medicure_Report.pdf"


    pdf = canvas.Canvas(
        filename,
        pagesize=letter
    )


    y = 750


    pdf.setFont(
        "Helvetica-Bold",
        18
    )


    pdf.drawString(
        50,
        y,
        "Medicure Predictor AI Report"
    )


    y -= 40


    pdf.setFont(
        "Helvetica",
        12
    )


    pdf.drawString(
        50,
        y,
        "Generated Date: "
        +
        str(datetime.now())
    )


    y -= 40


    pdf.drawString(
        50,
        y,
        "Patient Name: "
        +
        name
    )


    y -= 25


    pdf.drawString(
        50,
        y,
        "Age: "
        +
        str(age)
    )


    y -= 25


    pdf.drawString(
        50,
        y,
        "Gender: "
        +
        gender
    )


    y -= 25


    if height:

        pdf.drawString(
            50,
            y,
            "Height: "
            +
            str(height)
            +
            " cm"
        )

        y -= 25



    if weight:

        pdf.drawString(
            50,
            y,
            "Weight: "
            +
            str(weight)
            +
            " kg"
        )

        y -= 25



    y -= 20


    pdf.drawString(
        50,
        y,
        "Predicted Diseases:"
    )


    y -= 30


    for result in predictions:

        pdf.drawString(

            70,

            y,

            result["Disease"]
            +
            " - "
            +
            str(result["Confidence"])
            +
            "%"

        )

        y -= 25



    pdf.save()


    return filename
