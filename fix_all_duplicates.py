import os
import django
import json
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept, Exercise
from ai_engine.gemini import GeminiEngine

engine = GeminiEngine()

def fix_concept(concept_name):
    concept = Concept.objects.filter(name=concept_name).first()
    if not concept:
        print(f"Concept {concept_name} not found.")
        return False

    print(f"\n[{time.strftime('%H:%M:%S')}] Fixing {concept_name}...")

    # Check if already fixed (more than 10 unique examples)
    current_examples = concept.examples or []
    unique_en = {ex.get('en', '') for ex in current_examples if isinstance(ex, dict)}
    if len(unique_en) >= 50:
        print(f"Skipping {concept_name}, already has {len(unique_en)} unique examples.")
        return True

    # Keep the first 10 unique examples
    unique_examples = []
    seen_en = set()
    for ex in current_examples:
        en_text = ex.get('en', '')
        if en_text not in seen_en:
            unique_examples.append(ex)
            seen_en.add(en_text)
        if len(unique_examples) == 10:
            break

    # Keep the first 6 unique blanks
    blanks = Exercise.objects.filter(concept=concept, type='FILL_BLANK')
    unique_blanks = []
    seen_bq = set()
    for b in blanks:
        if b.question not in seen_bq:
            unique_blanks.append(b)
            seen_bq.add(b.question)
        if len(unique_blanks) == 6:
            break

    # Keep the first 6 unique speaking
    speaking = Exercise.objects.filter(concept=concept, type='READ_ALOUD')
    unique_speaking = []
    seen_sq = set()
    for s in speaking:
        if s.question not in seen_sq:
            unique_speaking.append(s)
            seen_sq.add(s.question)
        if len(unique_speaking) == 6:
            break

    prompt = f"""
    You are an expert English teacher. I need you to generate NEW, UNIQUE, real-life conversational practice data for the concept: '{concept_name}'.
    DO NOT duplicate any sentences. Make them varied, using different subjects, verbs, and contexts.
    
    Output exactly valid JSON with the following structure:
    {{
        "examples": [
            {{
                "en": "English sentence",
                "te": "Telugu translation",
                "explanation": "Short explanation"
            }}
            // Generate EXACTLY 40 unique items
        ],
        "blanks": [
            {{
                "question": "Sentence with a ___ blank.",
                "correct_answer": "answer",
                "telugu_meaning": "Telugu translation of sentence",
                "explanation": "Why this answer is correct",
                "options": ["option1", "option2", "option3", "option4"]
            }}
            // Generate EXACTLY 24 unique items
        ],
        "speaking": [
            {{
                "question": "English sentence to read aloud",
                "telugu_meaning": "Telugu meaning",
                "explanation": "Pronunciation tip"
            }}
            // Generate EXACTLY 24 unique items
        ]
    }}
    
    Return ONLY the JSON. No markdown formatting. No ```json. Just raw valid JSON.
    """

    try:
        response_text = engine.ask(system_prompt="You are a helpful assistant.", user_input=prompt, max_tokens=8000)
        
        if response_text.startswith("I'm having a bit of trouble"):
            print("API Error:", response_text)
            return False

        # Clean up response
        response_text = response_text.strip()
        if response_text.startswith('```json'):
            response_text = response_text[7:]
        if response_text.endswith('```'):
            response_text = response_text[:-3]

        data = json.loads(response_text)

        new_examples = data.get('examples', [])
        new_blanks = data.get('blanks', [])
        new_speaking = data.get('speaking', [])

        print(f"Generated {len(new_examples)} examples, {len(new_blanks)} blanks, {len(new_speaking)} speaking.")

        if len(new_examples) > 0:
            concept.examples = unique_examples + new_examples
            concept.save()

        if len(new_blanks) > 0:
            kept_blank_ids = [b.id for b in unique_blanks]
            Exercise.objects.filter(concept=concept, type='FILL_BLANK').exclude(id__in=kept_blank_ids).delete()
            for b in new_blanks:
                Exercise.objects.create(
                    concept=concept, type='FILL_BLANK', question=b['question'],
                    correct_answer=b['correct_answer'], explanation=b['explanation'],
                    telugu_meaning=b['telugu_meaning'], options=b['options']
                )

        if len(new_speaking) > 0:
            kept_speaking_ids = [s.id for s in unique_speaking]
            Exercise.objects.filter(concept=concept, type='READ_ALOUD').exclude(id__in=kept_speaking_ids).delete()
            for s in new_speaking:
                Exercise.objects.create(
                    concept=concept, type='READ_ALOUD', question=s['question'],
                    telugu_meaning=s['telugu_meaning'], explanation=s['explanation']
                )

        print(f"Successfully fixed data for {concept_name}")
        return True

    except Exception as e:
        print(f"Error fixing {concept_name}: {e}")
        return False

if __name__ == '__main__':
    duplicated_concepts = [
        'Present Perfect', 'Present Perfect Continuous', 'Simple Future', 
        'Daily Vocabulary', 'Business Vocabulary', 'Travel Vocabulary', 
        'Food Vocabulary', 'Emotional Vocabulary', 'Fluency', 'Pronunciation', 
        'Accent', 'Voice Clarity', 'Confidence', 'Daily Conversation', 'Shopping', 
        'Office', 'Travel', 'Presentation', 'Silent Letters', 'Word Stress', 
        'Tongue Twisters', 'Difficult Words', 'Interjections', 'Active Voice', 
        'Passive Voice', 'Direct Speech', 'Indirect Speech', 'Modals', 
        'Question Tags', 'Conditional Sentences'
    ]
    
    for c in duplicated_concepts:
        success = fix_concept(c)
        if success:
            print("Sleeping for 60 seconds to avoid rate limits...")
            time.sleep(60)
