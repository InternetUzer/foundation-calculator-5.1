from fpdf import FPDF

def generate_pdf_report(params, results):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Отчёт: Калькулятор плитного фундамента", ln=True)
    for k, v in {**params, **results}.items():
        pdf.cell(200, 10, txt=f"{k}: {v}", ln=True)
    return "foundation_report.pdf"
