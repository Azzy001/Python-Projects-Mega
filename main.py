from fpdf import FPDF

my_pdf = FPDF(orientation="p", format="A4")

# adds page to document
my_pdf.add_page()

# name document and add its path
my_pdf.output("project.pdf")