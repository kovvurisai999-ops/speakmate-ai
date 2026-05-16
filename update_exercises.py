from roadmap.models import Concept, Exercise

def add_exercises():
    # 1. Alphabets
    alphabets = Concept.objects.get(slug='alphabets')
    Exercise.objects.filter(concept=alphabets).delete()
    alphabets_ex = [
        {"q": "What comes after 'B'?", "a": "C", "type": "FILL_BLANK"},
        {"q": "How many vowels are there in English?", "a": "5", "type": "FILL_BLANK"},
        {"q": "Is 'Y' always a consonant?", "a": "No", "type": "FILL_BLANK"},
    ]
    for ex in alphabets_ex:
        Exercise.objects.create(concept=alphabets, question=ex['q'], correct_answer=ex['a'], type=ex['type'])

    # 2. Greetings
    greetings = Concept.objects.get(slug='greetings')
    Exercise.objects.filter(concept=greetings).delete()
    greetings_ex = [
        {"q": "Which greeting is used for a boss?", "a": "Good morning", "type": "FILL_BLANK"},
        {"q": "Is 'What's up' formal or informal?", "a": "Informal", "type": "FILL_BLANK"},
    ]
    for ex in greetings_ex:
        Exercise.objects.create(concept=greetings, question=ex['q'], correct_answer=ex['a'], type=ex['type'])

    # 3. Simple Present
    sp = Concept.objects.get(slug='simple-present')
    Exercise.objects.filter(concept=sp).delete()
    sp_ex = [
        {"q": "He ____ (eat) an apple every day.", "a": "eats", "type": "FILL_BLANK"},
        {"q": "I ____ (like) music.", "a": "like", "type": "FILL_BLANK"},
        {"q": "They ____ (play) cricket.", "a": "play", "type": "FILL_BLANK"},
    ]
    for ex in sp_ex:
        Exercise.objects.create(concept=sp, question=ex['q'], correct_answer=ex['a'], type=ex['type'])

    print("Exercises added successfully for core modules!")

if __name__ == "__main__":
    add_exercises()
