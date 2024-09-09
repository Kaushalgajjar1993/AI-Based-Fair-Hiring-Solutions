
def display_results(name, resume_text, disability_details, job_fit_result=None):
    print(f"\n---- Analysis Results for Name: {name} ----")
    print(f"Disability Detected: {disability_details}")
    print(f"\nResume Details:\n{resume_text[:100]}...")  # Displaying the first 100 chars of resume for brevity
    if job_fit_result:
        print(f"Job Fit Result: {job_fit_result}")
