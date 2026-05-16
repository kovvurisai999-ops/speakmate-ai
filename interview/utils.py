import PyPDF2
import docx
import spacy
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return "\n".join(text)

def parse_resume(file_path):
    if file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        text = extract_text_from_docx(file_path)
    else:
        return None
    
    # Simple Skill Extraction using NLP
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    # Common tech skills list (Can be expanded)
    SKILLS_DB = [
        "Python", "Django", "JavaScript", "React", "HTML", "CSS", "SQL", 
        "Machine Learning", "AI", "Data Science", "C++", "Java", "Flutter",
        "Node.js", "Express", "PostgreSQL", "Git", "Docker", "Kubernetes"
    ]
    
    found_skills = []
    for skill in SKILLS_DB:
        if re.search(r'\b' + re.escape(skill) + r'\b', text, re.IGNORECASE):
            found_skills.append(skill)
            
    return {
        "text": text[:4000], # Preview
        "skills": found_skills
    }
