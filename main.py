from fpdf import FPDF
from prettytable import PrettyTable

article = PrettyTable(["Pros", "Cons"])
pdf = FPDF()
pdf = FPDF(orientation="p", format="A4")

# adds page to document
pdf.add_page()

# adding images to document (with hyperlink)
pdf.image("shadow-of-war.png", x=175, y=5, w=30, h=30, link="https://www.shadowofwar.com/purchase/")
pdf.image("shadow-of-war2.png", x=175, y=35, w=30, h=30, link="")
pdf.image("shadow-of-war3.png", x=175, y=65, w=30, h=30, link="")

pdf.set_font("Arial", size=17)
pdf.cell(5, 10, txt="Why you should play Shadow of war in 2022!")

pdf.set_font("Arial", size=10)
pdf.text(5, 18, txt="By Arsalan Arref")



pdf.cell(w=0, h=5, txt="Test", border=1, align="C", ln=1)

pdf.multi_cell(w=0, h=5, txt="In this article, I will be sharing my opinion on why I think that this game still rocks, \neven though its over 5 years old.", border=1)

# name document and add its path
pdf.output("project.pdf")