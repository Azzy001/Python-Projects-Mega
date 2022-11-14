from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.output("test1.pdf")

print("Test")
print("test 2")
print("Test 3")