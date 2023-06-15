from fpdf import FPDF
import sys
class PDF(FPDF):
    def header(self): 
    
      
      self.image(r"C:\Users\hp\Downloads\shirtificate.png", 10, 70, 190)
      self.set_font("helvetica", "", 48)
      
      self.cell(0,57,'shirtcertificate',align='C')
      self.ln(20)
    

def shirt(s):
       pdf=PDF()
       pdf.add_page(orientation="P", format="a4")
       pdf.set_font("helvetica", size=24)
       pdf.set_text_color(255,255,255)
       pdf.cell(0,250,f"{s} took cs50", align="C")
       pdf.output("shirtificate.pdf")
       sys.exit()




def main():
       name=input("enter name")
       shirt(name)
if __name__ == "__main__":
    main()