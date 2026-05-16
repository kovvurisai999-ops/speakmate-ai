import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- MODALS DATA ---
content = "Modals are helping verbs used to express: Ability, Permission, Possibility, Advice, Necessity, Request, Suggestion. Common Modals: can, could, may, might, should, must, will, would, shall."
rules = """
- Modal verb taruvata base verb vastundi
- 'to' use cheyyaru
- Modals helping verbs laga work chestayi
- Sentence meaning ni strong ga change chestayi
- Formula: Subject + Modal Verb + Base Verb + Object
"""

examples = [
    {"en": "I can speak English fluently.", "te": "నేను ఇంగ్లీష్ fluently మాట్లాడగలను.", "explanation": "'can' ability ni show chestundi."},
    {"en": "You should practice daily.", "te": "నువ్వు ప్రతిరోజూ practice చేయాలి.", "explanation": "'should' advice ivvadam kosam use chesam."},
    {"en": "May I come in, sir?", "te": "సర్, నేను లోపలికి రావచ్చా?", "explanation": "'may' permission kosam use chesam."},
    {"en": "She can solve this problem.", "te": "ఆమె ఈ సమస్యను పరిష్కరించగలదు.", "explanation": "Ability ni express chestundi."},
    {"en": "We must follow traffic rules.", "te": "మనం ట్రాఫిక్ నియమాలు తప్పకుండా పాటించాలి.", "explanation": "'must' strong necessity ni chupistundi."},
    {"en": "He will attend the interview tomorrow.", "te": "అతను రేపు ఇంటర్వ్యూకు హాజరవుతాడు.", "explanation": "Future action with 'will'."},
    {"en": "Could you help me please?", "te": "దయచేసి మీరు నాకు సహాయం చేయగలరా?", "explanation": "'could' for polite request."},
    {"en": "You should improve your pronunciation.", "te": "నువ్వు pronunciation మెరుగుపరచాలి.", "explanation": "Advice with 'should'."},
    {"en": "I might visit Hyderabad next week.", "te": "నేను వచ్చే వారం హైదరాబాద్ వెళ్లవచ్చు.", "explanation": "'might' for possibility."},
    {"en": "Students must wear uniforms.", "te": "విద్యార్థులు తప్పనిసరిగా యూనిఫాం ధరించాలి.", "explanation": "Necessity with 'must'."},
    {"en": "She will call you later.", "te": "ఆమె తర్వాత నీకు కాల్ చేస్తుంది.", "explanation": "Future action."},
    {"en": "Can you open the door?", "te": "నువ్వు తలుపు తెరవగలవా?", "explanation": "Ability/Request."},
    {"en": "You should drink more water.", "te": "నువ్వు ఎక్కువ నీళ్లు తాగాలి.", "explanation": "Advice."},
    {"en": "He could run very fast in childhood.", "te": "అతను చిన్నప్పుడు చాలా వేగంగా పరుగెత్తగలిగేవాడు.", "explanation": "Past ability."},
    {"en": "May I use your phone?", "te": "నేను మీ ఫోన్ ఉపయోగించవచ్చా?", "explanation": "Permission."},
    {"en": "The team will win the match.", "te": "జట్టు మ్యాచ్ గెలుస్తుంది.", "explanation": "Prediction."},
    {"en": "You must complete the project today.", "te": "నువ్వు ఈరోజే ప్రాజెక్ట్ పూర్తి చేయాలి.", "explanation": "Strong necessity."},
    {"en": "Would you like some coffee?", "te": "మీకు కొంచెం కాఫీ కావాలా?", "explanation": "Polite offer."},
    {"en": "I can understand Telugu easily.", "te": "నేను తెలుగు సులభంగా అర్థం చేసుకోగలను.", "explanation": "Ability."},
    {"en": "We should respect our parents.", "te": "మనం మన తల్లిదండ్రులను గౌరవించాలి.", "explanation": "Advice/Obligation."},
    {"en": "She may join the meeting online.", "te": "ఆమె online లో meeting join కావచ్చు.", "explanation": "Possibility."},
    {"en": "Can I ask one question?", "te": "నేను ఒక ప్రశ్న అడగవచ్చా?", "explanation": "Permission."},
    {"en": "You should speak confidently.", "te": "నువ్వు confident గా మాట్లాడాలి.", "explanation": "Advice."},
    {"en": "He might come late today.", "te": "అతను ఈరోజు ఆలస్యంగా రావచ్చు.", "explanation": "Possibility."},
    {"en": "I would love to work in a multinational company.", "te": "నేను multinational company లో పని చేయాలని ఇష్టపడతాను.", "explanation": "Preference."},
    {"en": "You must submit the assignment.", "te": "నువ్వు assignment తప్పకుండా submit చేయాలి.", "explanation": "Compulsion."},
    {"en": "Could you repeat the sentence?", "te": "మీరు sentence మళ్లీ చెప్పగలరా?", "explanation": "Polite request."},
    {"en": "She can dance very well.", "te": "ఆమె చాలా బాగా డ్యాన్స్ చేయగలదు.", "explanation": "Ability."},
    {"en": "We may travel tomorrow.", "te": "మేము రేపు ప్రయాణం చేయవచ్చు.", "explanation": "Possibility."},
    {"en": "Students should ask questions freely.", "te": "విద్యార్థులు స్వేచ్ఛగా ప్రశ్నలు అడగాలి.", "explanation": "Suggestion."},
    {"en": "He will become a software engineer.", "te": "అతను software engineer అవుతాడు.", "explanation": "Future intent."},
    {"en": "Can you explain this topic?", "te": "ఈ topic explain చేయగలవా?", "explanation": "Ability/Request."},
    {"en": "We should save money.", "te": "మనం డబ్బు save చేయాలి.", "explanation": "Advice."},
    {"en": "You must wear a helmet.", "te": "నువ్వు helmet తప్పనిసరిగా ధరించాలి.", "explanation": "Necessity."},
    {"en": "Would you join our team?", "te": "మీరు మా టీమ్లో join అవుతారా?", "explanation": "Polite request."},
    {"en": "I can complete this work quickly.", "te": "నేను ఈ పని త్వరగా పూర్తి చేయగలను.", "explanation": "Ability."},
    {"en": "You should sleep early.", "te": "నువ్వు త్వరగా నిద్రపోవాలి.", "explanation": "Advice."},
    {"en": "She may not attend the class.", "te": "ఆమె క్లాస్కు రాకపోవచ్చు.", "explanation": "Possibility."},
    {"en": "Could I borrow your laptop?", "te": "నేను మీ laptop తీసుకోవచ్చా?", "explanation": "Polite request."},
    {"en": "We will start the session soon.", "te": "మేము session త్వరలో ప్రారంభిస్తాము.", "explanation": "Future action."},
    {"en": "You must learn communication skills.", "te": "నువ్వు communication skills తప్పకుండా నేర్చుకోవాలి.", "explanation": "Necessity."},
    {"en": "He can repair computers.", "te": "అతను computers repair చేయగలడు.", "explanation": "Ability."},
    {"en": "Would you like to join the interview?", "te": "మీరు interview join అవుతారా?", "explanation": "Polite offer."},
    {"en": "You should avoid negative thinking.", "te": "నువ్వు negative thinking నివారించాలి.", "explanation": "Advice."},
    {"en": "She might become a doctor.", "te": "ఆమె doctor కావచ్చు.", "explanation": "Possibility."},
    {"en": "Can we start the class now?", "te": "మనం ఇప్పుడు class ప్రారంభించవచ్చా?", "explanation": "Permission."},
    {"en": "The company will hire new employees.", "te": "కంపెనీ కొత్త ఉద్యోగులను hire చేస్తుంది.", "explanation": "Future action."},
    {"en": "You must respect time.", "te": "నువ్వు సమయాన్ని గౌరవించాలి.", "explanation": "Necessity."},
    {"en": "I could understand the lesson easily.", "te": "నేను పాఠాన్ని సులభంగా అర్థం చేసుకోగలిగాను.", "explanation": "Past ability."},
    {"en": "We should help others.", "te": "మనం ఇతరులకు సహాయం చేయాలి.", "explanation": "'should' advice and moral suggestion ni express chestundi."}
]

blanks = [
    {"question": "I ___ speak English fluently.", "correct_answer": "can", "telugu_meaning": "నేను ఇంగ్లీష్ fluently మాట్లాడగలను.", "explanation": "Ability.", "options": ["can", "may", "must", "might"]},
    {"question": "You ___ practice daily.", "correct_answer": "should", "telugu_meaning": "నువ్వు ప్రతిరోజూ practice చేయాలి.", "explanation": "Advice.", "options": ["should", "could", "would", "can"]},
    {"question": "___ I come in, sir?", "correct_answer": "May", "telugu_meaning": "సర్, నేను లోపలికి రావచ్చా?", "explanation": "Permission.", "options": ["May", "Can", "Must", "Will"]},
    {"question": "We ___ follow traffic rules.", "correct_answer": "must", "telugu_meaning": "మనం ట్రాఫిక్ నియమాలు తప్పకుండా పాటించాలి.", "explanation": "Strong necessity.", "options": ["must", "may", "might", "could"]},
    {"question": "Could you ___ me please?", "correct_answer": "help", "telugu_meaning": "దయచేసి మీరు నాకు సహాయం చేయగలరా?", "explanation": "Base verb after could.", "options": ["help", "helps", "helped", "helping"]},
    {"question": "She ___ solve this problem.", "correct_answer": "can", "telugu_meaning": "ఆమె ఈ సమస్యను పరిష్కరించగలదు.", "explanation": "Ability.", "options": ["can", "will", "should", "must"]},
    {"question": "You ___ improve your pronunciation.", "correct_answer": "should", "telugu_meaning": "నువ్వు pronunciation మెరుగుపరచాలి.", "explanation": "Advice.", "options": ["should", "could", "may", "will"]},
    {"question": "He ___ attend the interview tomorrow.", "correct_answer": "will", "telugu_meaning": "అతను రేపు ఇంటర్వ్యూకు హాజరవుతాడు.", "explanation": "Future action.", "options": ["will", "can", "should", "must"]},
    {"question": "Students ___ wear uniforms.", "correct_answer": "must", "telugu_meaning": "విద్యార్థులు తప్పనిసరిగా యూనిఫాం ధరించాలి.", "explanation": "Compulsion.", "options": ["must", "may", "should", "could"]},
    {"question": "Would you ___ some coffee?", "correct_answer": "like", "telugu_meaning": "మీకు కొంచెం కాఫీ కావాలా?", "explanation": "Polite offer verb.", "options": ["like", "likes", "liked", "liking"]}
]

# Add 20 more blanks
for i in range(10, 30):
    ex = examples[i]
    modal = next((m for m in ["can", "could", "may", "might", "should", "must", "will", "would"] if m in ex['en'].lower()), "can")
    question = ex['en'].replace(modal, "___").replace(modal.capitalize(), "___")
    blanks.append({
        "question": question,
        "correct_answer": modal,
        "telugu_meaning": ex['te'],
        "explanation": "Modal verb usage.",
        "options": ["can", "could", "may", "might", "should", "must", "will", "would"]
    })

speaking = []
for i in range(30):
    ex = examples[i]
    speaking.append({
        "question": ex['en'],
        "telugu_meaning": ex['te'],
        "explanation": "Speak clearly: " + ex['en']
    })

def update_concept_data():
    concept = Concept.objects.filter(name='Modals').first()
    if concept:
        concept.content = content
        concept.grammar_rules = rules
        concept.examples = examples
        concept.save()
        
        Exercise.objects.filter(concept=concept).delete()
        for b in blanks:
            Exercise.objects.create(
                concept=concept, type='FILL_BLANK', question=b['question'],
                correct_answer=b['correct_answer'], explanation=b['explanation'],
                telugu_meaning=b['telugu_meaning'], options=b['options']
            )
        for s in speaking:
            Exercise.objects.create(
                concept=concept, type='READ_ALOUD', question=s['question'],
                telugu_meaning=s['telugu_meaning'], explanation=s['explanation']
            )
        print("Modals updated successfully.")
    else:
        print("Concept 'Modals' not found.")

update_concept_data()
