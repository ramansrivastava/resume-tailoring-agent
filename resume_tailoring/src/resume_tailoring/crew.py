from crewai import Agent, Task, Crew
import os
from pathlib import Path
from typing import Optional
from resume_tailoring.tools.pdf_parser import extract_resume_text
from resume_tailoring.tools.job_parser import extract_job_info
from resume_tailoring.tools.keyword_matcher import match_keywords

def get_resume_path() -> str:
    """Get resume path from user input with validation."""
    while True:
        resume_path = input("Please enter the path to your resume PDF file: ").strip()
        if os.path.exists(resume_path) and resume_path.lower().endswith('.pdf'):
            return resume_path
        print("Invalid path or file format. Please provide a valid PDF file path.")

def get_job_description() -> str:
    """Get job description from user with options."""
    print("\nHow would you like to input the job description?")
    print("1. Paste LinkedIn job URL")
    print("2. Paste job description text")
    
    while True:
        choice = input("Enter your choice (1 or 2): ").strip()
        if choice == "1":
            # TODO: Implement LinkedIn scraping
            url = input("Enter LinkedIn job posting URL: ").strip()
            return "LinkedIn scraping not implemented yet"  # Placeholder
        elif choice == "2":
            print("Paste the job description below (press Ctrl+Z on Windows or Ctrl+D on Unix and Enter when done):")
            lines = []
            try:
                while True:
                    line = input()
                    lines.append(line)
            except EOFError:
                return "\n".join(lines)
        else:
            print("Invalid choice. Please enter 1 or 2.")

def run_resume_tailor_crew():
    """Main function to run the resume tailoring crew."""
    # Get user inputs
    resume_path = get_resume_path()
    job_text = get_job_description()

    # Parse resume
    resume_data = extract_resume_text(resume_path)
    combined_text = "\n".join(
        f"{section}:\n{content}" for section, content in resume_data.items()
    )

    # Parse job
    job_data = extract_job_info(job_text)  

    # Now print job_data to check its structure
    print("Job Data:", job_data)

    # Keyword Matching
    resume_text = resume_data.get("Resume", "")
    job_text_flat = "\n".join([line for section in job_data.values() if isinstance(section, list) for line in section])
    keyword_matches = match_keywords(resume_text, job_text_flat)

    print("\n Keyword Matching Results:")
    print(" Common Skills:", keyword_matches["common_skills"])
    print(" Missing Skills:", keyword_matches["missing_skills"])

    # Define agents
    resume_agent = Agent(
        role="Resume Analyst",
        goal="Identify and extract the top skills and qualifications from the resume.",
        backstory="You are an expert at identifying key skills, experiences, and qualifications from resumes. Your goal is to identify the most important skills that match job descriptions.",
        verbose=True
    )
    
    job_agent = Agent(
        role="Job Matcher",
        goal="Match the resume with the job description and identify skills and qualifications the candidate might be missing.",
        backstory="You specialize in comparing resumes with job postings. Your task is to highlight common skills and qualifications, as well as skills that the resume is missing according to the job description.",
        verbose=True
    )

    tailoring_agent = Agent(
        role="TailoringExpert",
        goal="Create an optimized version of the resume that best matches the job requirements while maintaining authenticity.",
        backstory="You are an expert resume writer with years of experience in tailoring resumes to specific job descriptions. You know how to restructure content, emphasize relevant experiences, and phrase accomplishments to align with job requirements. You maintain truthfulness while presenting information in the most appealing way.",
        verbose=True
    )

    # Define tasks
    task1 = Task(
        description=f"Here is a candidate's resume:\n{combined_text}\n\nSummarize their top 5 skills.",
        expected_output="A bullet-point list of the candidate's top 5 skills.",
        agent=resume_agent
    )

    task2 = Task(
        description=f"Match this candidate's resume with the job description. Resume:\n{combined_text}\n\nJob Description:\n{job_data}",
        expected_output="A summary of the skills and qualifications that match between the job and resume.",
        agent=job_agent
    )

    task3 = Task(
        description=f"""Create an optimized version of the resume based on the job requirements. Use this information:
        
        Original Resume:
        {combined_text}
        
        Job Description:
        {job_data}
        
        Matching Keywords:
        {keyword_matches}
        
        Guidelines:
        1. Maintain the same sections as the original resume
        2. Emphasize experiences and skills that match the job requirements
        3. Rephrase achievements to highlight relevant competencies
        4. Maintain truthfulness while optimizing the presentation
        5. Include measurable results where possible
        6. Use industry-specific keywords from the job description
        """,
        expected_output="A complete, restructured resume optimized for the target job position.",
        agent=tailoring_agent
    )

    # Create and run the crew
    crew = Crew(
        agents=[resume_agent, job_agent, tailoring_agent],
        tasks=[task1, task2, task3],
        verbose=True
    )

    result = crew.kickoff()
    
    # Save the tailored resume
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    output_path = output_dir / "tailored_resume.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        # Access the output of the last task (task3) which contains the tailored resume
        tailored_resume = result.tasks_output[2]  # Index 2 corresponds to task3
        f.write(str(tailored_resume))
    
    print(f"\nTailored resume has been saved to: {output_path}")
    return result
