import re

def extract_keywords(text):
    """
    Extracts lowercase keywords (words/phrases) from a block of text.
    You can expand this later with NLP libraries or embedding-based matchers.
    """
    # Basic tokenizer — improves with domain knowledge or spaCy
    tokens = re.findall(r'\b[A-Za-z][A-Za-z0-9+.#-]{1,}\b', text)
    return set(token.lower() for token in tokens if len(token) > 1)


def match_keywords(resume_text, job_text):
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_text)

    common_skills = set(resume_keywords).intersection(set(job_keywords))
    missing_skills = set(job_keywords) - set(resume_keywords)

    return {
        "common_skills": list(common_skills),
        "missing_skills": list(missing_skills)
    }

