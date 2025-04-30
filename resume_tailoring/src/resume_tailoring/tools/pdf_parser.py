from docling.document_converter import DocumentConverter

def extract_resume_text(file_path: str) -> dict:
    # Initialize the DocumentConverter
    converter = DocumentConverter()
    
    # Convert the document to a structured format
    result = converter.convert(file_path)
    
    # Extract the text content from the result
    text = result.document.export_to_text()
    
    return {"Resume": text.strip()}
