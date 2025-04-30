def extract_job_info(job_text):
    # Basic segmentation (can improve later with LLM or regex)
    lines = job_text.strip().split("\n")
    sections = {
        "Responsibilities": [],
        "Skills": [],
        "Qualifications": [],
        "Other": []
    }

    current = "Other"
    for line in lines:
        l = line.lower()
        if "responsibilit" in l:
            current = "Responsibilities"
        elif "skill" in l:
            current = "Skills"
        elif "qualification" in l:
            current = "Qualifications"

        sections[current].append(line.strip())

    return sections


