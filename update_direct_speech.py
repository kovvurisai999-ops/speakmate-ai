import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- DIRECT SPEECH DATA ---
content = "Direct Speech means repeating the exact words spoken by a person using quotation marks. The speaker's original words are written exactly as spoken."
rules = """
- Use quotation marks " "
- Exact words should be written
- Reporting verb used before speech
- Comma used before quotation sometimes
- Formula: Subject + Reporting Verb + "," + Quotation Marks
"""

examples = [
    {"en": 'She said, "I am learning English."', "te": 'ఆమె చెప్పింది, "నేను ఇంగ్లీష్ నేర్చుకుంటున్నాను."', "explanation": "Speaker exact words quotation marks lo unnayi."},
    {"en": 'My teacher said, "Complete your homework."', "te": 'నా టీచర్ చెప్పారు, "మీ హోంవర్క్ పూర్తి చేయండి."', "explanation": "Teacher direct command exact ga mention chesam."},
    {"en": 'He said, "I will call you tomorrow."', "te": 'అతను చెప్పాడు, "నేను రేపు నీకు కాల్ చేస్తాను."', "explanation": "Future action ni exact words tho direct ga cheppam."},
    {"en": 'The manager said, "Attend the meeting at 10 AM."', "te": 'మేనేజర్ చెప్పారు, "10 గంటలకు మీటింగ్ attend అవ్వండి."', "explanation": "Manager instruction direct speech lo undi."},
    {"en": 'Mother said, "Drink milk every day."', "te": 'అమ్మ చెప్పింది, "ప్రతి రోజు పాలు తాగు."', "explanation": "Mother advice ni direct ga quotation marks lo rasam."},
    {"en": 'The doctor said, "Take these tablets after food."', "te": 'డాక్టర్ చెప్పారు, "ఈ టాబ్లెట్స్ భోజనం తర్వాత తీసుకోండి."', "explanation": "Direct speech for advice."},
    {"en": 'My friend said, "Let\'s play cricket."', "te": 'నా ఫ్రెండ్ చెప్పాడు, "మనము క్రికెట్ ఆడుదాం."', "explanation": "Direct invitation."},
    {"en": 'The trainer said, "Practice spoken English daily."', "te": 'ట్రైనర్ చెప్పారు, "ప్రతిరోజూ spoken English practice చేయండి."', "explanation": "Direct instruction."},
    {"en": 'Father said, "Switch off the lights."', "te": 'నాన్న చెప్పారు, "లైట్లు ఆఫ్ చేయి."', "explanation": "Direct command."},
    {"en": 'The student said, "I completed the project."', "te": 'విద్యార్థి చెప్పాడు, "నేను ప్రాజెక్ట్ పూర్తి చేశాను."', "explanation": "Direct statement."},
    {"en": 'She said, "I love reading books."', "te": 'ఆమె చెప్పింది, "నాకు పుస్తకాలు చదవడం ఇష్టం."', "explanation": "Direct speech for feelings."},
    {"en": 'The HR said, "Your interview is scheduled tomorrow."', "te": 'HR చెప్పారు, "మీ ఇంటర్వ్యూ రేపు షెడ్యూల్ చేయబడింది."', "explanation": "Direct information."},
    {"en": 'My brother said, "I bought a new phone."', "te": 'నా అన్న చెప్పాడు, "నేను కొత్త ఫోన్ కొనుగోలు చేశాను."', "explanation": "Direct statement."},
    {"en": 'The coach said, "Work hard for success."', "te": 'కోచ్ చెప్పారు, "విజయం కోసం కష్టపడండి."', "explanation": "Direct encouragement."},
    {"en": 'The customer said, "I need help with this product."', "te": 'కస్టమర్ చెప్పారు, "ఈ ప్రొడక్ట్ విషయంలో నాకు సహాయం కావాలి."', "explanation": "Direct request."},
    {"en": 'She said, "I am preparing for exams."', "te": 'ఆమె చెప్పింది, "నేను పరీక్షలకు సిద్ధమవుతున్నాను."', "explanation": "Direct speech."},
    {"en": 'The child said, "I want chocolate."', "te": 'పిల్లాడు చెప్పాడు, "నాకు చాక్లెట్ కావాలి."', "explanation": "Direct desire."},
    {"en": 'The teacher said, "Read the chapter carefully."', "te": 'టీచర్ చెప్పారు, "చాప్టర్ జాగ్రత్తగా చదవండి."', "explanation": "Direct instruction."},
    {"en": 'The driver said, "The bus will arrive soon."', "te": 'డ్రైవర్ చెప్పారు, "బస్ త్వరలో వస్తుంది."', "explanation": "Direct information."},
    {"en": 'My sister said, "I am watching a movie."', "te": 'నా సిస్టర్ చెప్పింది, "నేను సినిమా చూస్తున్నాను."', "explanation": "Direct speech."},
    {"en": 'The boss said, "Submit the report today."', "te": 'బాస్ చెప్పారు, "రిపోర్ట్ ఈరోజే సమర్పించండి."', "explanation": "Direct command."},
    {"en": 'He said, "I forgot my password."', "te": 'అతను చెప్పాడు, "నేను నా పాస్వర్డ్ మర్చిపోయాను."', "explanation": "Direct statement."},
    {"en": 'The student said, "I need extra practice."', "te": 'విద్యార్థి చెప్పాడు, "నాకు అదనపు practice కావాలి."', "explanation": "Direct request."},
    {"en": 'My uncle said, "We are going to Hyderabad."', "te": 'నా మామ చెప్పారు, "మేము హైదరాబాద్ వెళ్తున్నాం."', "explanation": "Direct speech."},
    {"en": 'The singer said, "Music is my passion."', "te": 'గాయకుడు చెప్పారు, "సంగీతం నా అభిరుచి."', "explanation": "Direct speech."},
    {"en": 'The receptionist said, "Please wait here."', "te": 'రిసెప్షనిస్ట్ చెప్పారు, "దయచేసి ఇక్కడ వేచి ఉండండి."', "explanation": "Direct request."},
    {"en": 'My friend said, "Your English is improving."', "te": 'నా ఫ్రెండ్ చెప్పాడు, "నీ ఇంగ్లీష్ మెరుగవుతోంది."', "explanation": "Direct compliment."},
    {"en": 'The police officer said, "Follow traffic rules."', "te": 'పోలీస్ అధికారి చెప్పారు, "ట్రాఫిక్ నియమాలు పాటించండి."', "explanation": "Direct instruction."},
    {"en": 'The engineer said, "This software is updated."', "te": 'ఇంజనీర్ చెప్పారు, "ఈ సాఫ్ట్వేర్ అప్డేట్ చేయబడింది."', "explanation": "Direct information."},
    {"en": 'She said, "I enjoy speaking English."', "te": 'ఆమె చెప్పింది, "నాకు ఇంగ్లీష్ మాట్లాడటం ఇష్టం."', "explanation": "Direct speech."},
    {"en": 'The farmer said, "This year crops are good."', "te": 'రైతు చెప్పారు, "ఈ సంవత్సరం పంటలు బాగున్నాయి."', "explanation": "Direct statement."},
    {"en": 'The customer said, "The service is excellent."', "te": 'కస్టమర్ చెప్పారు, "సర్వీస్ చాలా బాగుంది."', "explanation": "Direct compliment."},
    {"en": 'My cousin said, "I joined a new company."', "te": 'నా cousin చెప్పారు, "నేను కొత్త కంపెనీలో చేరాను."', "explanation": "Direct speech."},
    {"en": 'The waiter said, "Your order is ready."', "te": 'వెయిటర్ చెప్పారు, "మీ ఆర్డర్ సిద్ధంగా ఉంది."', "explanation": "Direct information."},
    {"en": 'The principal said, "Maintain discipline."', "te": 'ప్రిన్సిపల్ చెప్పారు, "క్రమశిక్షణ పాటించండి."', "explanation": "Direct instruction."},
    {"en": 'The actor said, "I love my fans."', "te": 'నటుడు చెప్పారు, "నాకు నా అభిమానులు అంటే ఇష్టం."', "explanation": "Direct speech."},
    {"en": 'My mother said, "Wake up early."', "te": 'అమ్మ చెప్పింది, "త్వరగా లేవు."', "explanation": "Direct advice."},
    {"en": 'The guide said, "This place is historical."', "te": 'గైడ్ చెప్పారు, "ఈ ప్రదేశం చారిత్రాత్మకమైనది."', "explanation": "Direct info."},
    {"en": 'The programmer said, "I fixed the bug."', "te": 'ప్రోగ్రామర్ చెప్పారు, "నేను bug fix చేశాను."', "explanation": "Direct statement."},
    {"en": 'The player said, "We practiced very hard."', "te": 'ఆటగాడు చెప్పారు, "మేము చాలా కష్టపడి practice చేశాం."', "explanation": "Direct speech."},
    {"en": 'The chef said, "Dinner is ready."', "te": 'షెఫ్ చెప్పారు, "డిన్నర్ సిద్ధంగా ఉంది."', "explanation": "Direct info."},
    {"en": 'The student said, "I passed the exam."', "te": 'విద్యార్థి చెప్పారు, "నేను పరీక్షలో పాస్ అయ్యాను."', "explanation": "Direct statement."},
    {"en": 'My father said, "Work honestly."', "te": 'నాన్న చెప్పారు, "నిజాయితీగా పని చేయి."', "explanation": "Direct advice."},
    {"en": 'The doctor said, "Exercise daily."', "te": 'డాక్టర్ చెప్పారు, "ప్రతిరోజూ వ్యాయామం చేయండి."', "explanation": "Direct advice."},
    {"en": 'The employee said, "I completed the task."', "te": 'ఉద్యోగి చెప్పారు, "నేను పని పూర్తి చేశాను."', "explanation": "Direct statement."},
    {"en": 'She said, "I am feeling tired."', "te": 'ఆమె చెప్పింది, "నేను అలసిపోయాను."', "explanation": "Direct speech."},
    {"en": 'The librarian said, "Return the books on time."', "te": 'లైబ్రేరియన్ చెప్పారు, "పుస్తకాలు సమయానికి తిరిగి ఇవ్వండి."', "explanation": "Direct instruction."},
    {"en": 'My friend said, "Let\'s go for tea."', "te": 'నా ఫ్రెండ్ చెప్పారు, "టీకి వెల్దాం."', "explanation": "Direct invitation."},
    {"en": 'The teacher said, "Practice grammar daily."', "te": 'టీచర్ చెప్పారు, "ప్రతిరోజూ grammar practice చేయండి."', "explanation": "Direct instruction."},
    {"en": 'The manager said, "Your performance is excellent."', "te": 'మేనేజర్ చెప్పారు, "మీ performance చాలా బాగుంది."', "explanation": "Manager exact words ni direct ga quotation marks lo use chesam."}
]

blanks = [
    {"question": 'She said, "I ___ learning English."', "correct_answer": "am", "telugu_meaning": 'ఆమె చెప్పింది, "నేను ఇంగ్లీష్ నేర్చుకుంటున్నాను."', "explanation": "Direct speech present tense.", "options": ["am", "is", "are", "be"]},
    {"question": 'The teacher said, "___ your homework."', "correct_answer": "Complete", "telugu_meaning": 'టీచర్ చెప్పారు, "మీ హోంవర్క్ పూర్తి చేయండి."', "explanation": "Direct command.", "options": ["Complete", "Completes", "Completing", "Completed"]},
    {"question": 'He said, "I will ___ you tomorrow."', "correct_answer": "call", "telugu_meaning": 'అతను చెప్పాడు, "నేను రేపు నీకు కాల్ చేస్తాను."', "explanation": "Direct speech future action.", "options": ["call", "calling", "called", "calls"]},
    {"question": 'Mother said, "___ milk every day."', "correct_answer": "Drink", "telugu_meaning": 'అమ్మ చెప్పింది, "ప్రతి రోజు పాలు తాగు."', "explanation": "Direct advice.", "options": ["Drink", "Drinks", "Drinking", "Drank"]},
    {"question": 'The doctor said, "___ these tablets after food."', "correct_answer": "Take", "telugu_meaning": 'డాక్టర్ చెప్పారు, "ఈ టాబ్లెట్స్ భోజనం తర్వాత తీసుకోండి."', "explanation": "Direct advice.", "options": ["Take", "Takes", "Taking", "Took"]},
    {"question": 'The trainer said, "Practice spoken English ___."', "correct_answer": "daily", "telugu_meaning": 'ట్రైనర్ చెప్పారు, "ప్రతిరోజూ spoken English practice చేయండి."', "explanation": "Direct instruction.", "options": ["daily", "weekly", "yearly", "monthly"]},
    {"question": 'Father said, "Switch ___ the lights."', "correct_answer": "off", "telugu_meaning": 'నాన్న చెప్పారు, "లైట్లు ఆఫ్ చేయి."', "explanation": "Direct command.", "options": ["off", "on", "up", "down"]},
    {"question": 'The student said, "I ___ the project."', "correct_answer": "completed", "telugu_meaning": 'విద్యార్థి చెప్పాడు, "నేను ప్రాజెక్ట్ పూర్తి చేశాను."', "explanation": "Direct statement past action.", "options": ["completed", "complete", "completing", "completes"]},
    {"question": 'The HR said, "Your interview is ___ tomorrow."', "correct_answer": "scheduled", "telugu_meaning": 'HR చెప్పారు, "మీ ఇంటర్వ్యూ రేపు షెడ్యూల్ చేయబడింది."', "explanation": "Direct information.", "options": ["scheduled", "scheduling", "schedule", "schedules"]},
    {"question": 'My brother said, "I bought a new ___."', "correct_answer": "phone", "telugu_meaning": 'నా అన్న చెప్పాడు, "నేను కొత్త ఫోన్ కొనుగోలు చేశాను."', "explanation": "Direct statement object.", "options": ["phone", "car", "book", "bag"]}
]
# Add 20 more blanks
for i in range(10, 30):
    ex = examples[i]
    words = ex['en'].split('"')[1].split(' ')
    target_word = words[0] if len(words[0]) > 2 else words[1]
    question = ex['en'].replace(target_word, "___")
    blanks.append({
        "question": question,
        "correct_answer": target_word,
        "telugu_meaning": ex['te'],
        "explanation": ex['explanation'],
        "options": [target_word, "was", "is", "the"]
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
    concept = Concept.objects.filter(name='Direct Speech').first()
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
        print("Direct Speech updated successfully.")
    else:
        print("Concept 'Direct Speech' not found.")

update_concept_data()
