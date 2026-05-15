from fpdf import FPDF
def save_as_pdf(text,filename="report.pdf"):
    pdf=FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    for line in text.split("\n"):
        pdf.cell(0,10,line,ln=True)

    pdf.output(filename)

    return filename