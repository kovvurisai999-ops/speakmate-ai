import os
import django
import sys
import json
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise
from ai_engine.gemini import gemini_ai
from google.genai import types

def generate_data(prompt_type, concept_name, count):
    if prompt_type == 'examples':
        sys_prompt = f"You are an expert English-Telugu teacher. Generate EXACTLY {count} distinct real-life English examples for the grammar concept: '{concept_name}'."
        user_prompt = """Return ONLY a valid JSON array of objects. Do not include markdown formatting or backticks. Format:
[
  {
    "en": "English sentence here",
    "te": "Telugu translation in Telugu script",
    "explanation": "Short Telugu explanation of why this sentence structure was used based on the concept"
  }
]"""
    elif prompt_type == 'blanks':
        sys_prompt = f"You are an expert English teacher. Generate EXACTLY {count} real-life Fill in the Blanks exercises for the grammar concept: '{concept_name}'."
        user_prompt = """Return ONLY a valid JSON array of objects. Do not include markdown formatting or backticks. The question must contain '___' for the blank. Format:
[
  {
    "question": "English sentence with ___ blank",
    "correct_answer": "the missing word",
    "telugu_meaning": "Telugu translation of the full sentence",
    "explanation": "Short English explanation of why this is the correct answer",
    "options": ["wrong", "correct_answer", "wrong", "wrong"]
  }
]"""
    elif prompt_type == 'speaking':
        sys_prompt = f"You are an expert English teacher. Generate EXACTLY {count} real-life sentences for Speaking Practice (Read Aloud) for the grammar concept: '{concept_name}'."
        user_prompt = """Return ONLY a valid JSON array of objects. Do not include markdown formatting or backticks. Format:
[
  {
    "question": "English sentence to read aloud",
    "telugu_meaning": "Telugu translation of the sentence",
    "explanation": "Short English explanation of pronunciation or focus areas for this sentence"
  }
]"""
    
    config = types.GenerateContentConfig(
        system_instruction=sys_prompt,
        temperature=0.7,
        response_mime_type="application/json"
    )
    
    time.sleep(5) # Space out API calls to avoid RPM limits
    print(f"Generating {count} {prompt_type} for {concept_name}...")
    
    max_retries = 5
    retries = 0
    while retries < max_retries:
        try:
            response = gemini_ai.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_prompt,
                config=config
            )
            return json.loads(response.text)
        except Exception as e:
            if "429" in str(e):
                print(f"Rate limit hit. Sleeping for 45 seconds before retry...")
                time.sleep(45)
                retries += 1
            else:
                print(f"Error generation failed: {e}")
                return []
    print(f"Max retries reached for {concept_name} {prompt_type}.")
    return []

def populate_concept(concept):
    print(f"\nProcessing: {concept.name}")
    
    # Check Examples (Phase 2)
    current_examples_count = len(concept.examples) if isinstance(concept.examples, list) else 0
    if current_examples_count < 50:
        needed = 50 - current_examples_count
        new_examples = generate_data('examples', concept.name, needed)
        if new_examples:
            current_list = concept.examples if isinstance(concept.examples, list) else []
            current_list.extend(new_examples)
            concept.examples = current_list[:50]
            concept.save()
            print(f"  -> Added {len(new_examples)} examples. Total: {len(concept.examples)}")
    else:
        print("  -> Examples already 50. Skipped.")

    # Check Blanks (Phase 3)
    current_blanks = concept.exercises.filter(type='FILL_BLANK').count()
    if current_blanks < 30:
        needed = 30 - current_blanks
        new_blanks = generate_data('blanks', concept.name, needed)
        for item in new_blanks:
            Exercise.objects.create(
                concept=concept,
                type='FILL_BLANK',
                question=item.get('question', ''),
                correct_answer=item.get('correct_answer', ''),
                explanation=item.get('explanation', ''),
                telugu_meaning=item.get('telugu_meaning', ''),
                options=item.get('options', [])
            )
        print(f"  -> Added {len(new_blanks)} blanks. Total: {concept.exercises.filter(type='FILL_BLANK').count()}")
    else:
        print("  -> Blanks already 30. Skipped.")
        
    # Check Speaking (Phase 4)
    current_speaking = concept.exercises.filter(type='READ_ALOUD').count()
    if current_speaking < 30:
        needed = 30 - current_speaking
        new_speaking = generate_data('speaking', concept.name, needed)
        for item in new_speaking:
            Exercise.objects.create(
                concept=concept,
                type='READ_ALOUD',
                question=item.get('question', ''),
                telugu_meaning=item.get('telugu_meaning', ''),
                explanation=item.get('explanation', '')
            )
        print(f"  -> Added {len(new_speaking)} speaking exercises. Total: {concept.exercises.filter(type='READ_ALOUD').count()}")
    else:
        print("  -> Speaking exercises already 30. Skipped.")

if __name__ == '__main__':
    level_2 = Level.objects.filter(number=2).first()
    if not level_2:
        print("Level 2 not found.")
        sys.exit()

    concepts = level_2.concepts.all()
    for i, concept in enumerate(concepts):
        # We process one by one to avoid rate limits
        populate_concept(concept)
        if i < len(concepts) - 1:
            print("Sleeping for 15 seconds to avoid API rate limits...")
            time.sleep(15) # Delay to respect free tier RPM limits
