from fpdf import FPDF

pdf = FPDF()
my_pdf = FPDF(orientation="p", format="A4")

# adds page to document
my_pdf = pdf.add_page()

image1 = pdf.image("shadow-of-war.png", x=85, y=10, w=40, h=40, link="https://www.shadowofwar.com/purchase/")

# name document and add its path
my_pdf = pdf.output("project.pdf")


