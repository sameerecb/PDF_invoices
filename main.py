import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

# print(filepaths)  Printing name to see which all file exists.

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # print(df)
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, invoice_date = filename.split("-")
    pdf.set_font(family="Times", size=15, style="B")
    pdf.cell(w=50, h=10, txt=f"invoice_nr.{invoice_nr}", ln=1)

# Enter date in pdf file
#    invoice_date = filename.split("-")[1]  Another way of entering date
    pdf.set_font(family="Times", size=15, style="B")
    pdf.cell(w=50, h=10, txt=f"Invoice date: {invoice_date}")

    pdf.output(f"PDFs/{filename}.pdf")
