#! /usr/bin/env python3 (shebang)
# ToDO: allow my api to accept arguments from a file
# TODO: use selenium to hand in the task
# TODO: document and test the code

# dependencies
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
import sys
import os



# this is the init prodcecure 
def create_pdf(title:str, name:str, id:str, image_path:str, output_path:str) -> None:

    # validation
    if title == "" or name == "" or id == "" or image_path == "" or output_path == "":
        print("Error: Missing arguments")
        return

    # Create a PDF document
    doc = canvas.Canvas(output_path, pagesize=letter)
    row, col = doc._pagesize


    # Add title, name, and id
    doc.setFillColor(colors.ReportLabBlue)
    doc.setFont("Helvetica", 16)
    doc.drawString(row//3, col-100, title)
    doc.drawString(row//3, col-150, "Name: " + name)
    doc.drawString(row//3, col-200, "Id: " + id)


    # Add images on separate pages
    img_path = os.path.join(os.getcwd(), image_path)
    for image in os.listdir(img_path):
        doc.showPage() 
        doc.drawImage(img_path+image, 100, 100, width=400, height=500)

    # Save the PDF
    doc.save()



if __name__ == "__main__":
    
    title, name, id = sys.argv[1:]
    if title == "" or name == "" or id == "":
        print("Error: Missing arguments")
        exit(1)


    image_path = ".img/"
    output_path = f"{title}.pdf"

    create_pdf(title, name, id, image_path, output_path)
