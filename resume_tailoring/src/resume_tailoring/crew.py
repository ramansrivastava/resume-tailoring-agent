from crewai import Agent, Task, Crew
from tools.pdf_parser import extract_resume_text
from tools.job_parser import extract_job_info

def run_resume_tailor_crew():
    resume_path = "data/sample_resume.pdf"
    job_text = """
    Responsibilities:
    - Build and deploy ML pipelines
    - Collaborate with cross-functional teams

    Skills:
    - Python
    - TensorFlow
    - Communication

    Qualifications:
    - Bachelor's in Computer Science
    - 2+ years experience in ML
    """

    # TOOL USAGE
    resume_text = extract_resume_text(resume_path)
    job_info = extract_job_info(job_text)

    # AGENT DEFINITIONS
    extractor_agent = Agent(
        role='Resume Extractor',
        goal='Understand the structure of the resume',
        backstory='You are a resume analyst.',
        verbose=True
    )

    analyzer_agent = Agent(
        role='Job Analyzer',
        goal='Match job requirements with resume content',
        backstory='You are skilled in aligning resumes with job descriptions.',
        verbose=True
    )

    # TASKS
    task1 = Task(
        description=f"Parse and analyze the resume text:\n{resume_text}",
        agent=extractor_agent
    )

    task2 = Task(
        description=f"Analyze the job description and match with the resume:\n{job_info}",
        agent=analyzer_agent
    )

    # CREW
    crew = Crew(
        agents=[extractor_agent, analyzer_agent],
        tasks=[task1, task2],
        verbose=True
    )

    crew.kickoff()
