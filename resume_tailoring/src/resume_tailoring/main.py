from resume_tailoring.crew import run_resume_tailor_crew
from resume_tailoring.tools.pdf_parser import extract_resume_text
from resume_tailoring.tools.job_parser import extract_job_info
from resume_tailoring.tools.pdf_export import convert_to_pdf
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    # Run the resume tailoring crew
    result = run_resume_tailor_crew()
    
    # Define output paths
    output_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'output')
    txt_path = os.path.join(output_dir, 'tailored_resume.txt')
    pdf_path = os.path.join(output_dir, 'tailored_resume.pdf')
    
    # If the tailored resume text exists, convert it to PDF
    if os.path.exists(txt_path):
        with open(txt_path, 'r', encoding='utf-8') as f:
            text_content = f.read()
        convert_to_pdf(text_content, pdf_path)
        print(f"\nPDF version saved to: {pdf_path}")

if __name__ == "__main__":
    main()

