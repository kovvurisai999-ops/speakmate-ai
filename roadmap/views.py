from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Level, Concept, Exercise, UserConceptProgress
import markdown as md
import json
import difflib

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
        transcript = data.get('transcript', '').lower().strip()
        target_text = data.get('target_text', '').lower().strip()
        
        if not transcript:
            return JsonResponse({
                'pronunciation_score': 0,
                'fluency_score': 0,
                'results': [{'word': w, 'is_correct': False} for w in target_text.split()],
                'grammar_feedback': "No speech detected.",
                'correction': ""
            })

        # Remove punctuation for better matching
        import re
        def clean_text(text):
            return re.sub(r'[^\w\s]', '', text)

        clean_transcript = clean_text(transcript)
        clean_target = clean_text(target_text)
        
        transcript_words = clean_transcript.split()
        target_words_clean = clean_target.split()
        target_words_original = target_text.split()
        
        # 1. Advanced Sequence Matching
        matcher = difflib.SequenceMatcher(None, target_words_clean, transcript_words)
        results = []
        correct_count = 0
        
        # Initialize results with 'missing' status
        for word in target_words_original:
            results.append({'word': word, 'is_correct': False, 'status': 'missing'})

        # Update results based on matches
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == 'equal':
                for i in range(i1, i2):
                    results[i]['is_correct'] = True
                    results[i]['status'] = 'correct'
                    correct_count += 1
            elif tag == 'replace':
                for i in range(i1, i2):
                    results[i]['status'] = 'mispronounced'
            elif tag == 'delete':
                for i in range(i1, i2):
                    results[i]['status'] = 'missing'

        pronunciation_score = (correct_count / len(target_words_original)) * 100 if target_words_original else 0
        
        # 2. Fluency Score (Speed and filler words)
        fillers = ['um', 'uh', 'ah', 'like', 'actually']
        filler_count = sum(1 for w in transcript.split() if w in fillers)
        
        # Penalty for extra words (repetition or irrelevant speech)
        extra_words = len(transcript_words) - correct_count
        extra_penalty = max(0, extra_words * 2) 
        
        # Penalty for missing words
        missing_penalty = (len(target_words_original) - correct_count) * 3
        
        fluency_score = max(0, min(100, 100 - (filler_count * 15) - extra_penalty - missing_penalty))
        
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
