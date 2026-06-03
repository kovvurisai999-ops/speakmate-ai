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
        experience = request.POST.get('experience', 'Fresher')
        resume_file = request.FILES.get('resume')
        
        session = InterviewSession.objects.create(user=request.user, position=role, experience_level=experience)
        resume_text = ""
        
        if resume_file:
            session.resume = resume_file
            session.save()
            try:
                parsed_data = parse_resume(session.resume.path)
                if parsed_data:
                    session.extracted_skills = json.dumps(parsed_data['skills'])
                    resume_text = parsed_data['text']
                    session.save()
            except Exception as e:
                print(f"Resume parsing error: {e}")

        # Start with the first question
        intro_q = "Tell me about yourself. Please provide a brief introduction about your background and experience."
        InterviewQuestion.objects.create(session=session, question_text=intro_q)
            
        return redirect('interview:session', pk=session.pk)
    
    return render(request, 'interview/start.html')

@login_required
def interview_session(request, pk):
    session = get_object_or_404(InterviewSession, pk=pk, user=request.user)
    
    if request.method == 'POST':
        return redirect('interview:detail', pk=session.pk)

    questions = session.questions.all().order_by('id')
    return render(request, 'interview/session.html', {'session': session, 'questions': questions})

@csrf_exempt
@login_required
def evaluate_answer(request, pk):
    if request.method == 'POST' and request.FILES.get('audio'):
        session = get_object_or_404(InterviewSession, pk=pk, user=request.user)
        audio_file = request.FILES['audio']
        question_id = request.POST.get('question_id')
        
        temp_path = os.path.join(settings.MEDIA_ROOT, f"temp_interview_{pk}.wav")
        with open(temp_path, 'wb+') as destination:
            for chunk in audio_file.chunks():
                destination.write(chunk)
        
        try:
            # 1. Transcribe (Fastest step)
            text, lang = speech_manager.transcribe(temp_path)
            
            fillers = ['um', 'uh', 'ah', 'like', 'actually']
            filler_count = sum(1 for word in text.lower().split() if word in fillers)
            
            # 2. Extract Covered Topics from History for Memory
            covered_topics = []
            history = session.questions.all().order_by('id')
            history_text = ""
            for q in history:
                if q.user_answer:
                    history_text += f"Interviewer: {q.question_text}\nCandidate: {q.user_answer}\n"
                    # Simple heuristic to identify topics (e.g., proper nouns or technical terms mentioned)
                    # For CA, we can look for keywords like GST, Audit, Tax, etc.
                    for topic in ["GST", "Audit", "Taxation", "Accounting", "Excel", "Compliance", "ITC", "Materiality"]:
                        if topic.lower() in q.user_answer.lower() and topic not in covered_topics:
                            covered_topics.append(topic)
                else:
                    current_q = q

            # 3. Robust Role-Play Logic (Enforcing Strict CA Persona)
            system_prompt = (
                f"You are a Senior {session.position} Interviewer with a {session.user.ai_personality} personality. "
                f"Current Interviewee Level: {session.user.ai_difficulty}. "
                f"Preferred Language for minor clarifications: {session.user.preferred_language}.\n\n"
                "STRICT INTERVIEWER RULES:\n"
                "1. ROLE-PLAY: Act exactly like a real professional interviewer. No 'AI' talk.\n"
                "2. DYNAMIC FOLLOW-UPS: Analyze the candidate's LAST answer and ask a logical follow-up question. "
                "Do NOT use a fixed list of questions. Dig deeper into mentioned topics.\n"
                "3. ONE AT A TIME: Ask ONLY one question per turn.\n"
                "4. TECHNICAL CHALLENGE: If the candidate mentions a topic (e.g., GST), ask about specifics (e.g., ITC, filing).\n"
                "5. NO SPOILERS: Do not reveal correct answers or give full feedback during the conversation. Maintain the heat.\n"
                "6. CLARIFICATION: If the answer is vague (e.g., 'I know Excel'), ask for practical examples or details.\n"
                "7. POLITE CHALLENGE: If technically incorrect, challenge them politely (e.g., 'Are you sure about that calculation?').\n"
                "8. CONCISE: Next question must be MAX 40 words.\n"
                "9. TOPICS TRACKER: Avoid repeating yourself. Current covered topics: " + (", ".join(covered_topics) if covered_topics else "General Intro") + ".\n"
                "10. TERMINATION: Use [END_INTERVIEW] after 10-15 rounds or if the interview naturally concludes.\n\n"
                "OUTPUT FORMAT (STRICT):\n"
                "[SCORE: 0-100]\n"
                "[GRAMMAR: concise correction or 'Perfect']\n"
                "[EVALUATION: brief technical/confidence feedback for backend use]\n"
                "[REPLY: Your next professional follow-up question]"
            )
            
            user_prompt = f"Interview History:\n{history_text}\nLast Question: {current_q.question_text}\nCandidate's Answer: {text}"
            
            # Combine everything into one call
            full_ai_data = gemini_ai.ask(system_prompt, user_prompt, max_tokens=500)
            
            # Robust Parsing with Multi-Fallbacks
            score = 80
            score_match = re.search(r'\[SCORE:\s*(\d+)\]', full_ai_data)
            if score_match: score = int(score_match.group(1))
            
            grammar_match = re.search(r'\[GRAMMAR:\s*(.*?)\]', full_ai_data, re.DOTALL | re.IGNORECASE)
            grammar_feedback = grammar_match.group(1).strip() if grammar_match else "Grammar check complete."
            
            eval_match = re.search(r'\[EVALUATION:\s*(.*?)\]', full_ai_data, re.DOTALL | re.IGNORECASE)
            ai_eval = eval_match.group(1).strip() if eval_match else "Good progress."
            
            # Focused Reply Extraction
            reply_match = re.search(r'\[REPLY:\s*(.*)', full_ai_data, re.DOTALL | re.IGNORECASE)
            if reply_match:
                hr_reply = reply_match.group(1).split(']')[0].strip()
            else:
                # Fallback: If no tag, take the last paragraph that doesn't look like evaluation
                lines = [l.strip() for l in full_ai_data.split('\n') if l.strip()]
                hr_reply = lines[-1] if lines else "Next question."
            
            # Final sanity check to avoid generic "Next question"
            if len(hr_reply) < 5 or hr_reply.lower() == "next question.":
                # Emergency dynamic fallback if AI fails parsing tags
                hr_reply = f"That's interesting. Could you tell me more about your experience with some of the technical aspects of {session.position}?"

            # Update current question
            current_q.user_answer = text
            current_q.ai_feedback = ai_eval
            current_q.score = score
            current_q.save()

            # 4. Check for Interview End
            is_finished = "[END_INTERVIEW]" in full_ai_data or session.questions.count() >= 20
            
            next_q_id = None
            if not is_finished:
                # Create the next question dynamically
                next_q_text = hr_reply.replace("[END_INTERVIEW]", "").strip()
                next_q = InterviewQuestion.objects.create(session=session, question_text=next_q_text)
                next_q_id = next_q.id
                final_reply = next_q_text
            else:
                # Conclude
                session.is_completed = True
                final_reply = "Thank you. That conclude our interview. I will now generate your final feedback report."
                
                # Generate Comprehensive Feedback
                summary_prompt = (
                    "Evaluate the candidate like a real Senior Professional Interviewer.\n\n"
                    "### SUB_SCORES ###\n"
                    "Technical Score: [Score]/10\n"
                    "Communication Score: [Score]/10\n"
                    "Confidence Score: [Score]/10\n"
                    "Grammar Score: [Score]/10\n\n"
                    "### STRENGTHS ###\n"
                    "[List the candidate's core strengths]\n\n"
                    "### IMPROVEMENTS ###\n"
                    "[Areas for improvement and specific examples]\n\n"
                    "### SUGGESTED_ANSWERS ###\n"
                    "[Provide better ways to answer some of the difficult questions asked]\n\n"
                    "### HIRING_DECISION ###\n"
                    "[Final Recommendation: Hire/No Hire and professional reasoning]"
                )
                session.feedback = gemini_ai.ask(summary_prompt, history_text, max_tokens=1500)
                
                # Calculate overall score (average of all questions)
                total_qs = session.questions.count()
                if total_qs > 0:
                    avg_score = sum(q.score for q in session.questions.all()) // total_qs
                    session.overall_score = avg_score
                
                session.save()

            feedback_display = f"Transcribed: '{text}'\n\n{grammar_feedback}\n\nAI Evaluation: {ai_eval}"
            
            if os.path.exists(temp_path): os.remove(temp_path)
            
            return JsonResponse({
                'text': text,
                'feedback': feedback_display,
                'reply': final_reply,
                'is_finished': is_finished,
                'next_q_id': next_q_id,
                'score': score,
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
    
    # Parse Structured Feedback
    fb = session.feedback
    report = {
        'sub_scores': {},
        'strengths': "",
        'improvements': "",
        'suggested_answers': "",
        'hiring_decision': fb
    }
    
    try:
        sections = re.split(r'###\s*(.*?)\s*###', fb)
        for i in range(1, len(sections), 2):
            key = sections[i].strip()
            val = sections[i+1].strip()
            if key == 'SUB_SCORES':
                scores = {}
                for line in val.split('\n'):
                    if ':' in line:
                        s_name, s_val = line.split(':')
                        scores[s_name.strip()] = s_val.strip().replace('/10', '')
                report['sub_scores'] = scores
            elif key == 'STRENGTHS': report['strengths'] = val
            elif key == 'IMPROVEMENTS': report['improvements'] = val
            elif key == 'SUGGESTED_ANSWERS': report['suggested_answers'] = val
            elif key == 'HIRING_DECISION': report['hiring_decision'] = val
    except Exception as e:
        print(f"Report parsing error: {e}")

    return render(request, 'interview/detail.html', {'session': session, 'report': report})

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
