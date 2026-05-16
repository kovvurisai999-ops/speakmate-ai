import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- DAILY VOCABULARY DATA ---
daily_content = "Daily Vocabulary refers to the common words and phrases we use in our everyday lives. It includes words related to routines, household items, family, friends, and general activities."
daily_rules = """
- Focus on words you use most often in your native language.
- Learn phrases rather than single words (e.g., 'brush my teeth' instead of just 'brush').
- Practice using these words in your daily routine.
- Common categories: greetings, time, daily chores, weather, feelings.
"""

daily_examples = [
    {"en": "I wake up at 6 AM every day.", "te": "నేను ప్రతిరోజూ ఉదయం 6 గంటలకు నిద్రలేస్తాను.", "explanation": "Routine action."},
    {"en": "She is brushing her teeth.", "te": "ఆమె పళ్ళు తోముకుంటోంది.", "explanation": "Morning routine."},
    {"en": "Let's have breakfast.", "te": "మనం అల్పాహారం తీసుకుందాం.", "explanation": "Daily meal."},
    {"en": "He goes to work by bus.", "te": "అతను బస్సులో పనికి వెళ్తాడు.", "explanation": "Daily commute."},
    {"en": "I need to wash the clothes.", "te": "నేను బట్టలు ఉతకాలి.", "explanation": "Household chore."},
    {"en": "Please turn off the lights.", "te": "దయచేసి లైట్లు కట్టేయండి.", "explanation": "Everyday command."},
    {"en": "The weather is very hot today.", "te": "ఈరోజు వాతావరణం చాలా వేడిగా ఉంది.", "explanation": "Talking about weather."},
    {"en": "I am feeling tired.", "te": "నేను అలసిపోయినట్లుగా భావిస్తున్నాను.", "explanation": "Expressing daily feelings."},
    {"en": "Can you pass me the salt?", "te": "నాకు ఉప్పు అందించగలరా?", "explanation": "Common dining phrase."},
    {"en": "It is time to go to bed.", "te": "ఇది పడుకునే సమయం.", "explanation": "Night routine."}
]
daily_examples = (daily_examples * 5)[:50]

daily_blanks = [
    {"question": "I usually ___ up at 7 AM.", "correct_answer": "wake", "telugu_meaning": "నేను సాధారణంగా ఉదయం 7 గంటలకు నిద్రలేస్తాను.", "explanation": "Common routine verb.", "options": ["sleep", "wake", "run", "jump"]},
    {"question": "We have ___ at 8 AM.", "correct_answer": "breakfast", "telugu_meaning": "మేము ఉదయం 8 గంటలకు అల్పాహారం తీసుకుంటాము.", "explanation": "Morning meal.", "options": ["dinner", "lunch", "breakfast", "snack"]},
    {"question": "Please ___ the door when you leave.", "correct_answer": "close", "telugu_meaning": "నువ్వు వెళ్ళేటప్పుడు దయచేసి తలుపు మూసివేయి.", "explanation": "Daily action.", "options": ["open", "close", "break", "paint"]},
    {"question": "I need to take a ___.", "correct_answer": "shower", "telugu_meaning": "నేను స్నానం చేయాలి.", "explanation": "Daily hygiene.", "options": ["shower", "book", "car", "table"]},
    {"question": "The ___ is shining brightly today.", "correct_answer": "sun", "telugu_meaning": "ఈరోజు సూర్యుడు ప్రకాశవంతంగా మెరుస్తున్నాడు.", "explanation": "Weather word.", "options": ["moon", "stars", "sun", "cloud"]}
]
daily_blanks = (daily_blanks * 6)[:30]

daily_speaking = [
    {"question": "I wake up early in the morning.", "telugu_meaning": "నేను ఉదయాన్నే త్వరగా నిద్రలేస్తాను.", "explanation": "Speak with a natural rhythm."},
    {"question": "I am having my breakfast.", "telugu_meaning": "నేను నా అల్పాహారం తీసుకుంటున్నాను.", "explanation": "Emphasize 'breakfast'."},
    {"question": "It is very hot outside.", "telugu_meaning": "బయట చాలా వేడిగా ఉంది.", "explanation": "Express the feeling of heat."},
    {"question": "I need to clean my room.", "telugu_meaning": "నేను నా గదిని శుభ్రం చేసుకోవాలి.", "explanation": "Common daily chore."},
    {"question": "Good night, sleep well.", "telugu_meaning": "శుభరాత్రి, బాగా నిద్రపోండి.", "explanation": "Common night greeting."}
]
daily_speaking = (daily_speaking * 6)[:30]


# --- BUSINESS VOCABULARY DATA ---
business_content = "Business Vocabulary consists of formal words and expressions used in professional settings, workplaces, meetings, emails, and corporate communication."
business_rules = """
- Use formal language (e.g., 'assist' instead of 'help', 'inform' instead of 'tell').
- Be clear, concise, and polite in business emails.
- Learn common idioms used in business (e.g., 'touch base', 'think outside the box').
- Pay attention to specific terminology related to your industry.
"""

business_examples = [
    {"en": "We need to schedule a meeting.", "te": "మనం ఒక సమావేశాన్ని ఏర్పాటు చేయాలి.", "explanation": "Corporate planning."},
    {"en": "Please send me the report by EOD.", "te": "దయచేసి రోజు ముగిసేలోపు రిపోర్ట్ పంపండి.", "explanation": "EOD means End of Day."},
    {"en": "I look forward to your reply.", "te": "మీ ప్రత్యుత్తరం కోసం నేను ఎదురుచూస్తున్నాను.", "explanation": "Formal email closing."},
    {"en": "The company made a huge profit this year.", "te": "ఈ సంవత్సరం కంపెనీ భారీ లాభాన్ని ఆర్జించింది.", "explanation": "Financial term."},
    {"en": "Let's discuss this matter offline.", "te": "మనం ఈ విషయాన్ని ఆఫ్‌లైన్‌లో చర్చిద్దాం.", "explanation": "Business idiom meaning outside this meeting."},
    {"en": "He is the manager of the sales department.", "te": "అతను సేల్స్ డిపార్ట్‌మెంట్ మేనేజర్.", "explanation": "Job title."},
    {"en": "We have to meet the deadline.", "te": "మనం గడువుకు చేరుకోవాలి.", "explanation": "Project management term."},
    {"en": "Please find the attached document.", "te": "దయచేసి జతచేయబడిన పత్రాన్ని చూడండి.", "explanation": "Email phrase."},
    {"en": "Our CEO gave a presentation today.", "te": "మా CEO ఈరోజు ఒక ప్రెజెంటేషన్ ఇచ్చారు.", "explanation": "Corporate event."},
    {"en": "I agree with your proposal.", "te": "మీ ప్రతిపాదనతో నేను ఏకీభవిస్తున్నాను.", "explanation": "Professional agreement."}
]
business_examples = (business_examples * 5)[:50]

business_blanks = [
    {"question": "Please find the ___ file in this email.", "correct_answer": "attached", "telugu_meaning": "దయచేసి ఈ ఇమెయిల్‌లో జతచేయబడిన ఫైల్‌ను చూడండి.", "explanation": "Standard email terminology.", "options": ["glued", "attached", "sticked", "joined"]},
    {"question": "We must complete the project before the ___.", "correct_answer": "deadline", "telugu_meaning": "గడువు కంటే ముందే మనం ప్రాజెక్టును పూర్తి చేయాలి.", "explanation": "Time limit for a task.", "options": ["timeline", "deadline", "finish", "end"]},
    {"question": "The manager called a ___ at 10 AM.", "correct_answer": "meeting", "telugu_meaning": "మేనేజర్ ఉదయం 10 గంటలకు మీటింగ్‌ని పిలిచారు.", "explanation": "Business gathering.", "options": ["party", "meeting", "show", "game"]},
    {"question": "Our company made a huge ___ this quarter.", "correct_answer": "profit", "telugu_meaning": "మా కంపెనీ ఈ త్రైమాసికంలో భారీ లాభాన్ని ఆర్జించింది.", "explanation": "Financial gain.", "options": ["loss", "profit", "debt", "loan"]},
    {"question": "I look ___ to hearing from you soon.", "correct_answer": "forward", "telugu_meaning": "త్వరలో మీ నుండి వినడానికి నేను ఎదురుచూస్తున్నాను.", "explanation": "Formal closing phrase 'look forward to'.", "options": ["backward", "forward", "up", "down"]}
]
business_blanks = (business_blanks * 6)[:30]

business_speaking = [
    {"question": "We need to schedule a meeting.", "telugu_meaning": "మనం ఒక మీటింగ్‌ని షెడ్యూల్ చేయాలి.", "explanation": "Speak with a professional tone."},
    {"question": "Please send the report by tomorrow.", "telugu_meaning": "దయచేసి రేపటికల్లా రిపోర్ట్ పంపండి.", "explanation": "Professional request."},
    {"question": "I look forward to your reply.", "telugu_meaning": "మీ రిప్లై కోసం నేను ఎదురుచూస్తున్నాను.", "explanation": "Standard formal closing."},
    {"question": "Let's discuss the project details.", "telugu_meaning": "ప్రాజెక్ట్ వివరాలను చర్చిద్దాం.", "explanation": "Professional suggestion."},
    {"question": "Thank you for your cooperation.", "telugu_meaning": "మీ సహకారానికి ధన్యవాదాలు.", "explanation": "Formal appreciation."}
]
business_speaking = (business_speaking * 6)[:30]

def insert_level3_data(concept_name, content, rules, examples, blanks, speaking):
    concept = Concept.objects.filter(name=concept_name).first()
    if concept:
        concept.content = content.strip()
        concept.grammar_rules = rules.strip()
        concept.examples = examples
        concept.save()
        
        Exercise.objects.filter(concept=concept, type='FILL_BLANK').delete()
        Exercise.objects.filter(concept=concept, type='READ_ALOUD').delete()
        
        for item in blanks:
            Exercise.objects.create(
                concept=concept, type='FILL_BLANK', question=item['question'],
                correct_answer=item['correct_answer'], explanation=item['explanation'],
                telugu_meaning=item['telugu_meaning'], options=item['options']
            )
        for item in speaking:
            Exercise.objects.create(
                concept=concept, type='READ_ALOUD', question=item['question'],
                telugu_meaning=item['telugu_meaning'], explanation=item['explanation']
            )
        print(f"{concept_name} completed successfully.")
    else:
        print(f"Concept '{concept_name}' not found.")

insert_level3_data('Daily Vocabulary', daily_content, daily_rules, daily_examples, daily_blanks, daily_speaking)
insert_level3_data('Business Vocabulary', business_content, business_rules, business_examples, business_blanks, business_speaking)
