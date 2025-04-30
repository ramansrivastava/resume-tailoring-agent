from fpdf import FPDF
import os

def convert_to_pdf(text: str, output_path: str) -> None:
    """
    Convert text content to a PDF file
    
    Args:
        text (str): The text content to convert
        output_path (str): Path where the PDF should be saved
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Split text into lines and write to PDF
    lines = text.split('\n')
    for line in lines:
        if line.strip().startswith('#'):  # Handle markdown headers
            pdf.set_font("Arial", 'B', 14)
            pdf.cell(0, 10, line.replace('#', '').strip(), ln=True)
            pdf.set_font("Arial", size=12)
        else:
            pdf.multi_cell(0, 10, line.strip())
    
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf.output(output_path)