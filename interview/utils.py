import re

def extract_text_from_pdf(pdf_path):
    try:
        import PyPDF2
        text = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""
        return text
    except Exception as e:
        print(f"PDF extraction error: {e}")
        return ""

def extract_text_from_docx(docx_path):
    try:
        import docx
        doc = docx.Document(docx_path)
        text = []
        for para in doc.paragraphs:
            text.append(para.text)
        return "\n".join(text)
    except Exception as e:
        print(f"DOCX extraction error: {e}")
        return ""

def parse_resume(file_path):
    if file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        text = extract_text_from_docx(file_path)
    else:
        return None

    # Common tech skills list (simple regex-based matching, no spacy needed)
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
        "text": text[:4000],  # Preview
        "skills": found_skills
    }
