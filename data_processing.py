
import PyPDF2

def read_resume(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        resume_text = ""
        for page in range(len(reader.pages)):
            resume_text += reader.pages[page].extract_text()
    return resume_text
