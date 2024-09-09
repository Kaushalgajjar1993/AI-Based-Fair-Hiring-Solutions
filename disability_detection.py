
import re

def detect_disability(resume_text):
    disabilities = ['blind', 'deaf', 'ataxia', 'paralysis', 'disability']
    detected_disability = None
    for disability in disabilities:
        if re.search(disability, resume_text, re.IGNORECASE):
            detected_disability = disability.capitalize()
            break
    return detected_disability
