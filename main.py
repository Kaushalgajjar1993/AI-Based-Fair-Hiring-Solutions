
from data_processing import read_resume
from name_extraction import extract_name
from disability_detection import detect_disability
from job_fit_evaluation import evaluate_job_fit
from display import display_results

def main(file_path):
    resume_text = read_resume(file_path)
    name = extract_name(resume_text)
    disability_details = detect_disability(resume_text)
    job_fit_result = evaluate_job_fit(resume_text) if disability_details else None
    display_results(name, resume_text, disability_details, job_fit_result)

if __name__ == "__main__":
    file_path = "path_to_resume.pdf"  # Replace with the actual file path
    main(file_path)
