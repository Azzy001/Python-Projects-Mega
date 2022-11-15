from fpdf import FPDF
from prettytable import PrettyTable

article = PrettyTable(["Pros", "Cons"])
pdf = FPDF()
pdf = FPDF(orientation="p", format="A4")

# adds page to document
pdf.add_page()

"""
# adding images to document (with hyperlink)
pdf.image("", x=175, y=5, w=30, h=30, link="")
pdf.image("", x=175, y=37, w=30, h=30, link="")
pdf.image("", x=175, y=70, w=30, h=30, link="")
"""

pdf.set_font("Arial", size=17)
pdf.cell(w=0, h=5, txt="Why should you learn Python in 2022?", ln=1)

pdf.set_font("Arial", size=10)
pdf.cell(w=0, h=10, txt="By Arsalan Arref", ln=1)

# set position
pdf.set_xy(x=10, y=30)
pdf.set_font("Arial", style="B", size=10)
pdf.cell(w=0, h=5, txt="Temp", ln=1)

pdf.set_font("Arial", size=10)
pdf.multi_cell(w=0, h=5, txt="Python is the easiest programming language to learn,"+
                             " it is simple, easy to read, and it features english syntax. Therefore,"+
                             " If you are new to programming, then Python is your goto!")

pdf.set_xy(x=10, y=55)
pdf.set_font("Arial", style="B", size=10)
pdf.cell(w=0, h=5, txt="What can you do with Python?")

pdf.cell(w=0, h=5, txt="Temp", border=1, ln=1)

# name document and add its path
pdf.output("project.pdf")