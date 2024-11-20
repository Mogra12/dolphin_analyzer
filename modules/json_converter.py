from fpdf import FPDF

def json_to_pdf(json_data, output_pdf):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.add_font("Arial", "", "font/arial.ttf", uni=True)
    pdf.set_font("Arial", size=10)

    def add_data(data, indent=0):
        if isinstance(data, dict):
            for key, value in data.items():
                pdf.cell(200, 10, txt=" " * indent + f'"{key}": ', ln=True)
                add_data(value, indent + 4)  
        elif isinstance(data, list):
            for item in data:
                pdf.cell(200, 10, txt=" " * indent + "-="*50, ln=False)
                add_data(item, indent + 4) 
        else:
            pdf.cell(200, 10, txt=f'"{str(data)}"', ln=True)

    add_data(json_data)
    pdf.output(output_pdf)