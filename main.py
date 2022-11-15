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
pdf.cell(w=0, h=5, txt="What can you do with Python?", ln=1)

pdf.set_font("Arial", size=10)
pdf.multi_cell(w=0, h=5, txt="The things you can do with Python are endless! you can create softwares, "+
                        " websites, automation, data visualization, games, and so much more. "+
                        " In this article, I will give examples of 5 real-world applications, used by Python.")

# 1. healthcare
pdf.set_xy(x=10, y=75)
pdf.set_font("Arial", style="B", size=10)
pdf.cell(w=0, h=5, txt="        1. Healthcare", ln=1)

pdf.set_font("Arial", size=10)
pdf.multi_cell(w=0, h=5, txt="The medical industries are able to make better decisions with accurate predictions "+
                             "by using Python-powered applications, "+
                             "for example, using Python for image diagnostics or detecting and classifying tumors. "+
                             "Check out this link for more information: "+
                             "https://www.datacamp.com/blog/python-in-healthcare-ai-applications-in-hospitals")

# healthcare image
pdf.image("healthcare.jpg", x=10, y=100, w=75, h=45)

pdf.set_xy(x=90, y=100)
pdf.multi_cell(w=0, h=5, txt="Examples of Python applications used in Healthcare:\n"+
                                       "* Parkinson's disease detection\n"+
                                       "* Heart disease detection\n"+
                                       "* Diabetes prediction\n"+
                                       "* Breast cancer detection")


pdf.set_xy(x=10, y=150)
pdf.set_font("Arial", style="B", size=10)
pdf.cell(w=0, h=5, txt="        2. Data Visualization", ln=1)

pdf.set_font("Arial", size=10)
pdf.multi_cell(w=0, h=5, txt="Using libraries like Matplotlib, you can create graphs, plots, maps and "+
                                        "many more to better summarize and visualize your data."+
                                        "A few examples of using Matplotlib library is that you can make accurate decisions,"+
                                        "identify and compare multiple data sets to find results much faster. "+
                                        "Examples of data visualization:\n"+
                                        "https://www.tableau.com/learn/articles/best-beautiful-data-visualization-examples")

pdf.image("data-visualization.png", x=10, y=180, w=90, h=50)

pdf.set_xy(x=10, y=235)
pdf.set_font("Arial", style="B", size=10)
pdf.cell(w=0, h=5, txt="        3. Game Development")

pdf.set_font("Arial", size=10)
pdf.multi_cell(w=0, h=5, txt="You can use PyGame library to create your very own 2D games, for example, "+
                             "Flappy Bird, Snake, Chess, World of Tanks and so much more!.")


# name document and add its path
pdf.output("project.pdf")