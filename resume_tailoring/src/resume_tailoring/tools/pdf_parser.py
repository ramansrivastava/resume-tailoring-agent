import pdfplumber

def extract_resume_text(path):
    with pdfplumber.open(path) as pdf:
        full_text = ""
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"
        return full_text.strip()
