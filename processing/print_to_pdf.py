
import fpdf

pdf = fpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.write(5, "Hello!\n")
pdf.write(5, "My name is Ivan Leon.\n")
pdf.write(5, "I'm a Software Developer and I have 30 years old.")
pdf.output("ivan_data.pdf")
print("Done!")
