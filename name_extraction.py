
import re

def extract_name(resume_text):
    name_match = re.search(r'Name:\s*(\w+\s\w+)', resume_text)
    if name_match:
        return name_match.group(1)
    return "Name not found"
