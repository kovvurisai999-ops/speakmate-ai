from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
import io

def generate_interview_pdf(position, questions_data):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=HexColor('#6366f1'),
        spaceAfter=30
    )
    
    question_style = ParagraphStyle(
        'QuestionStyle',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=HexColor('#1e1e1e'),
        spaceBefore=15,
        spaceAfter=5,
        bold=True
    )
    
    answer_style = ParagraphStyle(
        'AnswerStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#4b5563'),
        leftIndent=20,
        spaceAfter=15
    )

    elements = []
    
    # Header
    elements.append(Paragraph(f"SpeakMate AI: Interview Study Guide", title_style))
    elements.append(Paragraph(f"Target Role: {position}", styles['Heading2']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("This guide contains top interview questions and high-quality answers to help you prepare for your professional journey.", styles['Normal']))
    elements.append(Spacer(1, 24))

    # Questions and Answers
    for i, item in enumerate(questions_data, 1):
        q_text = item if isinstance(item, str) else item.get('q', 'No question')
        a_text = "Answer currently being populated. Use the AI Chat for real-time practice." if isinstance(item, str) else item.get('a', 'No answer provided')
        
        elements.append(Paragraph(f"{i}. {q_text}", question_style))
        elements.append(Paragraph(f"Ideal Answer: {a_text}", answer_style))

    doc.build(elements)
    
    buffer.seek(0)
    return buffer

def generate_session_report_pdf(session, questions):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    
    styles = getSampleStyleSheet()
    
    # Header Section
    title_style = ParagraphStyle('Title', fontSize=26, textColor=HexColor('#6366f1'), spaceAfter=10, bold=True)
    score_style = ParagraphStyle('Score', fontSize=18, textColor=HexColor('#10b981'), spaceAfter=20, alignment=1)
    meta_style = ParagraphStyle('Meta', fontSize=10, textColor=HexColor('#6b7280'), spaceAfter=5)
    
    elements = []
    
    # 1. Header
    elements.append(Paragraph("AI Interview Performance Report", title_style))
    elements.append(Paragraph(f"Candidate: {session.user.username} | Role: {session.position}", meta_style))
    elements.append(Paragraph(f"Date: {session.created_at.strftime('%Y-%m-%d %H:%M')}", meta_style))
    elements.append(Spacer(1, 20))
    
    # 2. Overall Score
    elements.append(Paragraph(f"OVERALL PERFORMANCE SCORE: {session.overall_score}%", score_style))
    elements.append(Spacer(1, 10))
    
    # 3. AI Summary Feedback
    elements.append(Paragraph("<b>AI Executive Summary:</b>", styles['Heading3']))
    elements.append(Paragraph(session.feedback, styles['Normal']))
    elements.append(Spacer(1, 24))
    
    # 4. Question Breakdown
    elements.append(Paragraph("<b>Question-by-Question Analysis:</b>", styles['Heading2']))
    elements.append(Spacer(1, 12))
    
    q_style = ParagraphStyle('Q', fontSize=11, spaceBefore=10, bold=True)
    ans_style = ParagraphStyle('A', fontSize=10, leftIndent=20, textColor=HexColor('#374151'))
    fb_style = ParagraphStyle('FB', fontSize=9, leftIndent=20, textColor=HexColor('#6366f1'), spaceAfter=10)
    
    for i, q in enumerate(questions, 1):
        elements.append(Paragraph(f"Q{i}: {q.question_text}", q_style))
        elements.append(Paragraph(f"Your Answer: {q.user_answer if q.user_answer else 'No answer recorded.'}", ans_style))
        elements.append(Paragraph(f"AI Evaluation: {q.ai_feedback if q.ai_feedback else 'Pending analysis.'}", fb_style))
        elements.append(Spacer(1, 5))

    doc.build(elements)
    buffer.seek(0)
    return buffer
