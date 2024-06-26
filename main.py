import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

# print(filepaths)  Printing name to see which all file exists.

for filepath in filepaths:
    # print(df)
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, invoice_date = filename.split("-")
    pdf.set_font(family="Times", size=15, style="B")
    pdf.cell(w=50, h=10, txt=f"invoice_nr.{invoice_nr}", ln=1)

    # Enter date in pdf file
    # invoice_date = filename.split("-")[1]  Another way of entering date
    pdf.set_font(family="Times", size=15, style="B")
    pdf.cell(w=50, h=10, txt=f"Invoice date: {invoice_date}", ln=1)

# Reading excel file to update pdf file
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # print(df)
    # Add a header
    columns = df.columns
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=50, h=8, txt=columns[1], border=1)
    pdf.cell(w=35, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    for index, row in df.iterrows():
        # print(index, row)
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=50, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=35, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    pdf.output(f"PDFs/{filename}.pdf")
