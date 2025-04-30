# Resume Tailoring Agent (Powered by CrewAI)

This project is an AI-powered system designed to tailor resumes based on specific job postings. It uses modular agents defined via CrewAI to extract, analyze, and rewrite resume content so that it aligns with the key requirements of a job posting. The result is a highly personalized resume that increases the chances of landing interviews.

## Project Overview

The system takes as input:
- A user's resume (PDF, DOCX, or plain text)
- A LinkedIn job URL or raw job description text

It performs:
- Resume parsing and structuring
- Job description extraction and segmentation
- Keyword and skill matching
- Resume rewriting via LLMs

Technologies used include:
- Python
- CrewAI
- OpenAI LLMs
- Embeddings and semantic search

## Project Structure

```
resume_tailoring/
├── src/
│   └── resume_tailoring/
│       ├── tools/
│       │   ├── pdf_parser.py     # Resume PDF parsing
│       │   ├── job_parser.py     # Job description parsing
│       │   └── keyword_matcher.py # Skill matching logic
│       ├── crew.py              # CrewAI agent definitions
│       └── main.py             # Entry point
├── data/                      # Input data directory
├── output/                    # Generated resumes
└── tests/                     # Test cases
```

## Setup Instructions

1. Create and activate a virtual environment:
```bash
python -m venv agent-venv
source agent-venv/bin/activate  # On Windows: agent-venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory with:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Place your resume PDF in the `data` directory

2. Run the main script:
```bash
python -m resume_tailoring.main
```

3. Follow the prompts to:
   - Enter the path to your resume PDF
   - Paste the job description or provide a LinkedIn job URL

4. The system will generate two files in the `output` directory:
   - `tailored_resume.txt`: The tailored resume in text format
   - `tailored_resume.pdf`: A formatted PDF version of the tailored resume

## Features

- **PDF Parsing**: Extracts structured content from PDF resumes
- **Intelligent Job Analysis**: Segments job descriptions into skills, responsibilities, and qualifications
- **Keyword Matching**: Identifies matching and missing skills between resume and job posting
- **AI-Powered Rewriting**: Uses LLMs to optimize resume content for specific positions
- **PDF Export**: Generates professionally formatted PDF output

## Requirements

- Python 3.8+
- OpenAI API key
- Required packages listed in `requirements.txt`

## License

See the LICENSE file for details.

