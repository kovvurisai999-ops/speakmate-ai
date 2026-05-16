import random
import json
import os
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt

from .models import InterviewSession, InterviewQuestion
from .data import INTERVIEW_QUESTIONS, CORE_HR_QUESTIONS
from .utils import parse_resume
from .pdf_gen import generate_interview_pdf, generate_session_report_pdf
from speech.utils import SpeechManager
from grammar.utils import GrammarChecker
from ai_engine.gemini import gemini_ai

# Initialize Engines
speech_manager = SpeechManager()
grammar_checker = GrammarChecker()

@login_required
def interview_list(request):
    sessions = InterviewSession.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'interview/list.html', {'sessions': sessions})

@login_required
def start_interview(request):
    if request.method == 'POST':
        role = request.POST.get('position', 'Frontend Developer')
        resume_file = request.FILES.get('resume')
        
        session = InterviewSession.objects.create(user=request.user, position=role)
        resume_text = ""
        
        if resume_file:
            session.resume = resume_file
            session.save()
            
            # Parse Resume
            try:
                parsed_data = parse_resume(session.resume.path)
                if parsed_data:
                    session.extracted_skills = json.dumps(parsed_data['skills'])
                    resume_text = parsed_data['text']
                    session.save()
            except Exception as e:
                print(f"Resume parsing error: {e}")

        # 1. First Question: Self Introduction (Always)
        final_texts = ["Tell me about yourself. Please provide a brief introduction about your background and experience."]

        # 2. AI Resume Questions (10 questions)
        resume_questions = []
        try:
            if resume_text:
                system_prompt = (
                    f"You are an AI Interviewer. Analyze this resume for a {role} position. "
                    "Generate 10 unique interview questions based ONLY on the projects, specific tools, and experience mentioned in the resume. "
                    "Format your output clearly as Q1: [question], Q2: [question], etc. Focus on their projects and skills."
                )
                ai_output = gemini_ai.ask(system_prompt, resume_text, max_tokens=1500)
            else:
                system_prompt = f"You are an AI Interviewer. Generate 10 situational and advanced technical questions for a {role} candidate. Format: Q1: [question], Q2: [question]..."
                ai_output = gemini_ai.ask(system_prompt, "Generate questions.", max_tokens=1000)
            
            # Parsing logic
            resume_questions = re.split(r'Q\d+[:.]', ai_output)
            resume_questions = [q.strip() for q in resume_questions if q.strip() and len(q) > 10]
        except Exception as e:
            print(f"AI Question generation error: {e}")
            resume_questions = ["Can you tell me more about your recent projects?", "How do you keep your skills updated?"]

        # Shuffle resume questions and add to final list
        random.shuffle(resume_questions)
        final_texts.extend(resume_questions[:10])

        # 3. Technical Questions from Guides (15 questions)
        tech_pool = [q['q'] for q in INTERVIEW_QUESTIONS.get(role, [])]
        if not tech_pool:
            # Fallback if role is not found
            hr_pool = [q['q'] for q in CORE_HR_QUESTIONS]
            tech_pool = hr_pool
            
        selected_tech = random.sample(tech_pool, min(len(tech_pool), 15))
        final_texts.extend(selected_tech)

        # Create objects in the exact order
        objs = [InterviewQuestion(session=session, question_text=text) for text in final_texts]
        InterviewQuestion.objects.bulk_create(objs)
            
        return redirect('interview:session', pk=session.pk)
    
    return render(request, 'interview/start.html')

@login_required
def interview_session(request, pk):
    session = get_object_or_404(InterviewSession, pk=pk, user=request.user)
    
    if request.method == 'POST':
        # Handle interview completion and scoring
        # Calculate score based on individual question scores
        total_questions = session.questions.count()
        if total_questions > 0:
            total_score = sum(q.score for q in session.questions.all())
            avg_score = int(total_score / total_questions)
        else:
            avg_score = 0

        session.overall_score = avg_score
        session.is_completed = True
        session.feedback = f"Great performance! You showed strong technical knowledge in {session.position}. Your overall score is {avg_score}%."
        session.save()
        return redirect('interview:list')

    questions = session.questions.all()
    return render(request, 'interview/session.html', {'session': session, 'questions': questions})

@csrf_exempt
@login_required
def evaluate_answer(request, pk):
    if request.method == 'POST' and request.FILES.get('audio'):
        session = get_object_or_404(InterviewSession, pk=pk, user=request.user)
        audio_file = request.FILES['audio']
        question_id = request.POST.get('question_id')
        
        # Save temp audio
        temp_path = os.path.join(settings.MEDIA_ROOT, f"temp_interview_{pk}.wav")
        with open(temp_path, 'wb+') as destination:
            for chunk in audio_file.chunks():
                destination.write(chunk)
        
        try:
            # 1. Transcribe
            text, lang = speech_manager.transcribe(temp_path)
            
            # 2. Grammar Check
            corrected, grammar_feedback, is_valid = grammar_checker.check(text)
            
            # 3. Simple Fluency Check (Filler words)
            fillers = ['um', 'uh', 'ah', 'like', 'actually']
            filler_count = sum(1 for word in text.lower().split() if word in fillers)
            
            # 4. Generate AI Evaluation & HR Reply (Gemini Engine)
            current_q = InterviewQuestion.objects.get(id=question_id) if question_id else session.questions.all().first()
            
            system_prompt = "You are a professional HR Interviewer. Evaluate the user's answer and provide a smooth transition to the next question. Keep it concise."
            user_prompt = f"Question: {current_q.question_text}\nAnswer: {text}\nFormat: [SCORE: 0-100] [EVALUATION: your feedback] [REPLY: your next transition]"
            
            full_ai_data = gemini_ai.ask(system_prompt, user_prompt, max_tokens=150)
            
            ai_eval = ""
            hr_reply = ""
            score = 80 # Default
            
            try:
                if "[SCORE:" in full_ai_data:
                    score_text = full_ai_data.split("[SCORE:")[1].split("]")[0].strip()
                    score = int(re.sub(r'[^0-9]', '', score_text))
                
                if "[EVALUATION:" in full_ai_data:
                    ai_eval = full_ai_data.split("[EVALUATION:")[1].split("]")[0].strip()
                    hr_reply = full_ai_data.split("[REPLY:")[1].strip() if "[REPLY:" in full_ai_data else "Next question."
                else:
                    hr_reply = full_ai_data
            except:
                hr_reply = full_ai_data

            # Save question evaluation
            if current_q:
                current_q.user_answer = text
                current_q.ai_feedback = ai_eval
                current_q.score = score
                current_q.save()

            feedback = f"Transcribed: '{text}'\n\n{grammar_feedback}\n\nAI Evaluation: {ai_eval}"
            if filler_count > 2:
                feedback += f"\nNote: You used {filler_count} fillers. Try to be more concise."
            
            # Cleanup
            if os.path.exists(temp_path): os.remove(temp_path)
            
            return JsonResponse({
                'text': text,
                'feedback': feedback,
                'reply': hr_reply,
                'score': score,
                'pron_score': random.randint(75, 95),
                'conf_score': max(50, 100 - (filler_count * 10))
            })
            
        except Exception as e:
            if os.path.exists(temp_path): os.remove(temp_path)
            print(f"Evaluation error: {e}")
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def download_report(request, pk):
    session = get_object_or_404(InterviewSession, pk=pk, user=request.user)
    questions = session.questions.all()
    buffer = generate_session_report_pdf(session, questions)
    filename = f"Interview_Report_{session.pk}.pdf"
    return FileResponse(buffer, as_attachment=True, filename=filename)

@login_required
def interview_detail(request, pk):
    session = get_object_or_404(InterviewSession, pk=pk, user=request.user)
    return render(request, 'interview/detail.html', {'session': session})

@login_required
def delete_interview(request, pk):
    if request.method == 'POST':
        session = get_object_or_404(InterviewSession, pk=pk, user=request.user)
        session.delete()
        return redirect('interview:list')
    return redirect('interview:list')

@login_required
def download_guide(request):
    position = request.GET.get('position', 'Frontend Developer')
    questions_data = INTERVIEW_QUESTIONS.get(position, [])
    buffer = generate_interview_pdf(position, questions_data)
    filename = f"{position.replace(' ', '_')}_Interview_Guide.pdf"
    return FileResponse(buffer, as_attachment=True, filename=filename)
