from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Level, Concept, Exercise, UserConceptProgress
import markdown as md
import json

@login_required
def index(request):
    levels = Level.objects.prefetch_related('concepts').order_by('number')
    return render(request, 'roadmap/index.html', {'levels': levels})

@login_required
def concept_detail(request, slug):
    concept = get_object_or_404(Concept, slug=slug)
    exercises = concept.exercises.all()
    progress, created = UserConceptProgress.objects.get_or_create(
        user=request.user, concept=concept
    )
    
    content_html = md.markdown(
        concept.content,
        extensions=['fenced_code', 'tables', 'nl2br']
    )
    
    return render(request, 'roadmap/detail.html', {
        'concept': concept,
        'exercises': exercises,
        'progress': progress,
        'content_html': content_html,
    })

@login_required
def analyze_speaking(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        transcript = data.get('transcript', '')
        target_text = data.get('target_text', '')
        
        transcript_words = transcript.lower().strip().split()
        target_words = target_text.lower().strip().split()
        
        # 1. Word Highlight & Pronunciation Score
        results = []
        correct_count = 0
        clean_transcript_words = [''.join(e for e in w if e.isalnum()) for w in transcript_words]
        
        for word in target_words:
            # Clean punctuation for comparison
            clean_word = ''.join(e for e in word if e.isalnum())
            is_correct = clean_word in clean_transcript_words
                
            results.append({
                'word': word,
                'is_correct': is_correct
            })
            if is_correct:
                correct_count += 1
        
        pronunciation_score = (correct_count / len(target_words)) * 100 if target_words else 0
        
        # 2. Fluency Score (Basic estimation based on length match and filler words)
        fillers = ['um', 'uh', 'ah', 'like']
        filler_count = sum(1 for w in transcript_words if w in fillers)
        length_penalty = abs(len(target_words) - len(transcript_words)) * 5
        fluency_score = max(0, min(100, 100 - (filler_count * 10) - length_penalty))
        
        # 3. Grammar Detection
        from grammar.utils import GrammarChecker
        checker = GrammarChecker()
        correction, grammar_feedback, is_grammar_valid = checker.check(transcript)
        
        return JsonResponse({
            'pronunciation_score': round(pronunciation_score, 1),
            'fluency_score': round(fluency_score, 1),
            'results': results,
            'grammar_feedback': grammar_feedback if not is_grammar_valid else "Perfect grammar!",
            'correction': correction
        })

@csrf_exempt
def get_exercises(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            slug = data.get('slug')
            exercise_type = data.get('type', 'FILL_BLANK')
            
            concept = Concept.objects.get(slug=slug)
            exercises = Exercise.objects.filter(concept=concept, type=exercise_type)
            
            exercise_list = []
            for ex in exercises:
                exercise_list.append({
                    'question': ex.question,
                    'correct_answer': ex.correct_answer,
                    'explanation': ex.explanation or "No explanation available.",
                    'hint': ex.hint
                })
            
            return JsonResponse({'exercises': exercise_list})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@login_required
def analyze_writing(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        full_text = data.get('text', '').strip()
        slug = data.get('slug', '')
        
        if not full_text:
            return JsonResponse({'is_valid': False, 'correction': "Please write something."})

        lines = [line.strip() for line in full_text.split('\n') if line.strip()]
        all_results = []
        overall_valid = True
        
        from grammar.utils import GrammarChecker
        from textblob import TextBlob
        checker = GrammarChecker()

        for text in lines:
            if len(text) < 5:
                all_results.append({'text': text, 'is_valid': False, 'feedback': "This line is too short."})
                overall_valid = False
                continue

            # 1. Grammar Tool Check
            correction, feedback, is_line_valid = checker.check(text)
            
            # 2. Custom Strict Checks for 'Missing Words'
            blob = TextBlob(text)
            tags = blob.tags
            lower_text = text.lower()
            
            # Check for missing helping verbs (e.g., 'I learning' -> 'I am learning')
            if ' i ' in lower_text or lower_text.startswith('i '):
                if ' am ' not in lower_text and 'ing' in lower_text:
                    is_line_valid = False
                    feedback = "Missing 'am'. You should say 'I **am** learning' or 'I **am** going'."

            # Check for missing 'you' in questions
            if lower_text.startswith(('did ', 'do ', 'have ', 'are ')):
                if ' you ' not in lower_text and ' i ' not in lower_text and ' we ' not in lower_text:
                    is_line_valid = False
                    feedback = "Missing subject. Please add 'you' (e.g., 'Did **you** have lunch?')."

            # Check for missing prepositions/articles
            for i in range(len(tags)):
                word, tag = tags[i]
                if tag in ['NN', 'NNS'] and i > 0:
                    prev_word, _ = tags[i-1]
                    if prev_word.lower() in ['to', 'at', 'welcome']:
                        if word.lower() in ['office', 'college', 'school', 'market', 'lunch']:
                             if word.lower() not in ['home']:
                                 is_line_valid = False
                                 feedback = f"Missing word before '{word}'. Try using 'the {word}' or 'our {word}'."

            all_results.append({
                'text': text,
                'is_valid': is_line_valid,
                'feedback': feedback
            })
            if not is_line_valid:
                overall_valid = False

        return JsonResponse({
            'is_valid': overall_valid,
            'results': all_results,
            'correction': all_results[0]['feedback'] if all_results else ""
        })

@csrf_exempt
@login_required
def get_exercises(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        slug = data.get('slug')
        ex_type = data.get('type')
        
        concept = get_object_or_404(Concept, slug=slug)
        exercises = concept.exercises.filter(type=ex_type)
        
        ex_list = []
        for ex in exercises:
            ex_list.append({
                'id': ex.id,
                'question': ex.question,
                'hint': ex.hint,
                'answer': ex.correct_answer,
                'category': ex.category,
                'telugu_meaning': ex.telugu_meaning,
                'explanation': ex.explanation
            })
            
        return JsonResponse({'exercises': ex_list})
    return JsonResponse({'error': 'Invalid request'})
