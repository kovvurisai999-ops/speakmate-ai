import os
import django
import json
import re

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise
from ai_engine.gemini import gemini_ai

def get_ai_json(prompt, user_input, max_tokens=3000):
    response = gemini_ai.ask(prompt, user_input, max_tokens=max_tokens)
    # Extract JSON if wrapped in markdown
    json_match = re.search(r'\[\s*\{.*\}\s*\]', response, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group(0))
        except:
            pass
    try:
        return json.loads(response)
    except:
        return None

def populate_concept(topic_name):
    # Set encoding for print if needed, or just don't print complex objects
    print(f"--- Populating: {topic_name} ---")
    
    # Get or create Level 2 (Grammar Concepts)
    level2, _ = Level.objects.get_or_create(
        number=2, 
        defaults={'title': 'Grammar Concepts', 'description': 'Mastering Tenses and Sentence formation'}
    )
    
    slug = topic_name.lower().replace(' ', '-')
    concept, created = Concept.objects.get_or_create(
        slug=slug,
        defaults={'level': level2, 'name': topic_name}
    )
    
    # Phase 1: Theory
    print("Phase 1: Theory...")
    theory_prompt = f"You are a professional English Teacher. Provide a detailed Phase 1 concept learning markdown for '{topic_name}'. Include Definition, Structure, Rules (Positive/Negative/Question), and Real-life usage. Use professional yet simple formatting."
    concept.content = gemini_ai.ask(theory_prompt, "Generate theory.", max_tokens=2000)
    
    # Phase 2: 30 Examples
    print("Phase 2: Examples...")
    examples_prompt = (
        f"Generate 30 real-world examples for '{topic_name}' in English and Telugu. "
        "Include an AI explanation for why the sentence is formed this way. "
        "Categories to cover: home, office, interview, shopping, travel, friendship, social media, restaurant, meetings, phone calls. "
        "Format as a JSON list: [{\"en\": \"...\", \"te\": \"...\", \"explanation\": \"...\", \"category\": \"...\"}]"
    )
    examples_data = get_ai_json(examples_prompt, "Generate 30 examples.", max_tokens=4000)
    if examples_data:
        concept.examples = examples_data
    
    concept.save()

    # Phase 3: 30 Fill in the Blanks
    print("Phase 3: Fill Blanks...")
    fb_prompt = (
        f"Generate 30 Fill in the Blank questions for '{topic_name}'. "
        "Cover categories: office, college, travel, daily life, interview, shopping, family. "
        "Format as a JSON list: [{\"q\": \"She ___ (go) to college every day.\", \"a\": \"goes\", \"te\": \"...\", \"explanation\": \"...\", \"category\": \"...\"}]"
    )
    fb_data = get_ai_json(fb_prompt, "Generate 30 fill blanks.", max_tokens=4000)
    if fb_data:
        # Delete old ones
        Exercise.objects.filter(concept=concept, type='FILL_BLANK').delete()
        for item in fb_data:
            Exercise.objects.create(
                concept=concept,
                type='FILL_BLANK',
                question=item['q'],
                correct_answer=item['a'],
                telugu_meaning=item['te'],
                explanation=item['explanation'],
                category=item.get('category', 'General')
            )

    # Phase 4: 30 Speaking Practice
    print("Phase 4: Speaking...")
    sp_prompt = (
        f"Generate 30 real-world speaking practice sentences for '{topic_name}'. "
        "Focus on daily life English, easy pronunciation. "
        "Include difficulty levels: Beginner, Intermediate, Advanced. "
        "Format as a JSON list: [{\"s\": \"...\", \"d\": \"...\", \"category\": \"...\"}]"
    )
    sp_data = get_ai_json(sp_prompt, "Generate 30 speaking sentences.", max_tokens=3000)
    if sp_data:
        # Delete old ones
        Exercise.objects.filter(concept=concept, type='READ_ALOUD').delete()
        for item in sp_data:
            Exercise.objects.create(
                concept=concept,
                type='READ_ALOUD',
                question=item['s'],
                difficulty=item.get('d', 'Beginner'),
                category=item.get('category', 'General')
            )

    print(f"Successfully populated {topic_name}!")

if __name__ == "__main__":
    topics = [
        "Present Continuous"
    ]
    
    for t in topics:
        try:
            # Check if concept already has exercises to avoid redundant generation
            concept = Concept.objects.filter(name=t).first()
            if not concept or not concept.exercises.filter(type='FILL_BLANK').exists():
                populate_concept(t)
            else:
                print(f"{t} already populated with exercises, skipping.")
        except Exception as e:
            print(f"Error populating {t}: {e}")

