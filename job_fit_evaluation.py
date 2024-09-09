
def evaluate_job_fit(resume_text):
    required_skills = ['Python', 'Java', 'C++', 'SQL']
    has_required_skills = all(skill in resume_text for skill in required_skills)
    return "Good fit" if has_required_skills else "Not a good fit"
