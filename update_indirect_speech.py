import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- INDIRECT SPEECH DATA ---
content = "Indirect Speech means reporting someone’s words without using the exact same sentence. Quotation marks are not used in indirect speech."
rules = """
- Quotation marks are removed
- Tense may change
- Pronouns may change
- Reporting verbs like said, told, asked are used
- Meaning should stay same
- Formula: Subject + Reporting Verb + that + Reported Speech
"""

examples = [
    {"en": "She said that she was learning English.", "te": "ఆమె తాను ఇంగ్లీష్ నేర్చుకుంటున్నానని చెప్పింది.", "explanation": "Direct speech lo unna 'I am' indirect speech lo 'she was' ayindi."},
    {"en": "My teacher said that we should complete our homework.", "te": "మా టీచర్ హోంవర్క్ పూర్తి చేయాలని చెప్పారు.", "explanation": "Teacher exact words kakunda meaning ni indirect ga cheppam."},
    {"en": "He said that he would call me tomorrow.", "te": "అతను నాకు రేపు కాల్ చేస్తానని చెప్పాడు.", "explanation": "'Will' indirect speech lo 'would' ayindi."},
    {"en": "The manager said that we had a meeting at 10 AM.", "te": "మేనేజర్ 10 గంటలకు మీటింగ్ ఉందని చెప్పారు.", "explanation": "Quotation marks remove chesi indirect format use chesam."},
    {"en": "Mother said that I should drink milk daily.", "te": "అమ్మ నేను ప్రతిరోజూ పాలు తాగాలని చెప్పింది.", "explanation": "Advice ni indirect ga report chesam."},
    {"en": "The doctor said that I should take tablets after food.", "te": "డాక్టర్ భోజనం తర్వాత టాబ్లెట్స్ తీసుకోవాలని చెప్పారు.", "explanation": "Indirect report of advice."},
    {"en": "My friend said that we should play cricket.", "te": "నా ఫ్రెండ్ మనం క్రికెట్ ఆడాలని చెప్పాడు.", "explanation": "Indirect report of invitation."},
    {"en": "The trainer said that we should practice spoken English daily.", "te": "ట్రైనర్ ప్రతిరోజూ spoken English practice చేయాలని చెప్పారు.", "explanation": "Indirect instruction."},
    {"en": "Father said that I should switch off the lights.", "te": "నాన్న లైట్లు ఆఫ్ చేయాలని చెప్పారు.", "explanation": "Indirect report of command."},
    {"en": "The student said that he had completed the project.", "te": "విద్యార్థి ప్రాజెక్ట్ పూర్తి చేశానని చెప్పాడు.", "explanation": "Indirect speech past perfect."},
    {"en": "She said that she loved reading books.", "te": "ఆమెకు పుస్తకాలు చదవడం ఇష్టమని చెప్పింది.", "explanation": "Indirect speech feelings."},
    {"en": "The HR said that my interview was scheduled tomorrow.", "te": "HR నా ఇంటర్వ్యూ రేపు ఉందని చెప్పారు.", "explanation": "Indirect info."},
    {"en": "My brother said that he had bought a new phone.", "te": "నా అన్న కొత్త ఫోన్ కొనుగోలు చేశానని చెప్పాడు.", "explanation": "Indirect speech past perfect."},
    {"en": "The coach said that we should work hard for success.", "te": "కోచ్ విజయం కోసం కష్టపడాలని చెప్పారు.", "explanation": "Indirect encouragement."},
    {"en": "The customer said that he needed help with the product.", "te": "కస్టమర్ ప్రొడక్ట్ విషయంలో సహాయం కావాలని చెప్పారు.", "explanation": "Indirect request."},
    {"en": "She said that she was preparing for exams.", "te": "ఆమె పరీక్షలకు సిద్ధమవుతున్నానని చెప్పింది.", "explanation": "Indirect speech."},
    {"en": "The child said that he wanted chocolate.", "te": "పిల్లాడికి చాక్లెట్ కావాలని చెప్పాడు.", "explanation": "Indirect speech."},
    {"en": "The teacher said that we should read the chapter carefully.", "te": "టీచర్ చాప్టర్ జాగ్రత్తగా చదవాలని చెప్పారు.", "explanation": "Indirect instruction."},
    {"en": "The driver said that the bus would arrive soon.", "te": "డ్రైవర్ బస్ త్వరలో వస్తుందని చెప్పారు.", "explanation": "Indirect speech 'would'."},
    {"en": "My sister said that she was watching a movie.", "te": "నా సిస్టర్ సినిమా చూస్తున్నానని చెప్పింది.", "explanation": "Indirect speech."},
    {"en": "The boss said that I should submit the report that day.", "te": "బాస్ ఆ రోజే రిపోర్ట్ సమర్పించాలని చెప్పారు.", "explanation": "Indirect command."},
    {"en": "He said that he had forgotten his password.", "te": "అతను తన పాస్వర్డ్ మర్చిపోయానని చెప్పాడు.", "explanation": "Indirect speech."},
    {"en": "The student said that he needed extra practice.", "te": "విద్యార్థికి అదనపు practice కావాలని చెప్పాడు.", "explanation": "Indirect speech."},
    {"en": "My uncle said that they were going to Hyderabad.", "te": "నా మామ వాళ్లు హైదరాబాద్ వెళ్తున్నారని చెప్పారు.", "explanation": "Indirect speech."},
    {"en": "The singer said that music was his passion.", "te": "సంగీతం తన అభిరుచి అని గాయకుడు చెప్పారు.", "explanation": "Indirect speech."},
    {"en": "The receptionist said that I should wait there.", "te": "రిసెప్షనిస్ట్ అక్కడ వేచి ఉండాలని చెప్పారు.", "explanation": "Indirect request."},
    {"en": "My friend said that my English was improving.", "te": "నా ఇంగ్లీష్ మెరుగవుతోందని నా ఫ్రెండ్ చెప్పాడు.", "explanation": "Indirect compliment."},
    {"en": "The police officer said that we should follow traffic rules.", "te": "పోలీస్ అధికారి ట్రాఫిక్ నియమాలు పాటించాలని చెప్పారు.", "explanation": "Indirect instruction."},
    {"en": "The engineer said that the software was updated.", "te": "సాఫ్ట్వేర్ అప్డేట్ చేయబడిందని ఇంజనీర్ చెప్పారు.", "explanation": "Indirect info."},
    {"en": "She said that she enjoyed speaking English.", "te": "ఆమెకు ఇంగ్లీష్ మాట్లాడటం ఇష్టమని చెప్పింది.", "explanation": "Indirect speech."},
    {"en": "The farmer said that the crops were good that year.", "te": "ఆ సంవత్సరం పంటలు బాగున్నాయని రైతు చెప్పారు.", "explanation": "Indirect speech."},
    {"en": "The customer said that the service was excellent.", "te": "సర్వీస్ చాలా బాగుందని కస్టమర్ చెప్పారు.", "explanation": "Indirect compliment."},
    {"en": "My cousin said that he had joined a new company.", "te": "తాను కొత్త కంపెనీలో చేరానని నా cousin చెప్పారు.", "explanation": "Indirect speech."},
    {"en": "The waiter said that my order was ready.", "te": "నా ఆర్డర్ సిద్ధంగా ఉందని వెయిటర్ చెప్పారు.", "explanation": "Indirect info."},
    {"en": "The principal said that students should maintain discipline.", "te": "విద్యార్థులు క్రమశిక్షణ పాటించాలని ప్రిన్సిపల్ చెప్పారు.", "explanation": "Indirect instruction."},
    {"en": "The actor said that he loved his fans.", "te": "తన అభిమానులు అంటే ఇష్టమని నటుడు చెప్పారు.", "explanation": "Indirect speech."},
    {"en": "My mother said that I should wake up early.", "te": "నేను త్వరగా లేవాలని అమ్మ చెప్పింది.", "explanation": "Indirect advice."},
    {"en": "The guide said that the place was historical.", "te": "ఆ ప్రదేశం చారిత్రాత్మకమని గైడ్ చెప్పారు.", "explanation": "Indirect info."},
    {"en": "The programmer said that he had fixed the bug.", "te": "తాను bug fix చేశానని ప్రోగ్రామర్ చెప్పారు.", "explanation": "Indirect statement."},
    {"en": "The player said that they had practiced very hard.", "te": "వాళ్లు చాలా కష్టపడి practice చేశారని ఆటగాడు చెప్పారు.", "explanation": "Indirect speech."},
    {"en": "The chef said that dinner was ready.", "te": "డిన్నర్ సిద్ధంగా ఉందని షెఫ్ చెప్పారు.", "explanation": "Indirect info."},
    {"en": "The student said that he had passed the exam.", "te": "తాను పరీక్షలో పాస్ అయ్యానని విద్యార్థి చెప్పారు.", "explanation": "Indirect statement."},
    {"en": "My father said that I should work honestly.", "te": "నేను నిజాయితీగా పని చేయాలని నాన్న చెప్పారు.", "explanation": "Indirect advice."},
    {"en": "The doctor said that I should exercise daily.", "te": "నేను ప్రతిరోజూ వ్యాయామం చేయాలని డాక్టర్ చెప్పారు.", "explanation": "Indirect advice."},
    {"en": "The employee said that he had completed the task.", "te": "తాను పని పూర్తి చేశానని ఉద్యోగి చెప్పారు.", "explanation": "Indirect statement."},
    {"en": "She said that she was feeling tired.", "te": "ఆమె అలసిపోయానని చెప్పింది.", "explanation": "Indirect speech."},
    {"en": "The librarian said that we should return books on time.", "te": "పుస్తకాలు సమయానికి తిరిగి ఇవ్వాలని లైబ్రేరియన్ చెప్పారు.", "explanation": "Indirect instruction."},
    {"en": "My friend said that we should go for tea.", "te": "టీకి వెల్దామని నా ఫ్రెండ్ చెప్పాడు.", "explanation": "Indirect invitation."},
    {"en": "The teacher said that we should practice grammar daily.", "te": "ప్రతిరోజూ grammar practice చేయాలని టీచర్ చెప్పారు.", "explanation": "Indirect instruction."},
    {"en": "The manager said that my performance was excellent.", "te": "నా performance చాలా బాగుందని మేనేజర్ చెప్పారు.", "explanation": "Indirect report of compliment."}
]

blanks = [
    {"question": "She said that she ___ learning English.", "correct_answer": "was", "telugu_meaning": "ఆమె తాను ఇంగ్లీష్ నేర్చుకుంటున్నానని చెప్పింది.", "explanation": "Indirect 'was' for past continuous report.", "options": ["is", "was", "am", "been"]},
    {"question": "He said that he ___ call me tomorrow.", "correct_answer": "would", "telugu_meaning": "అతను నాకు రేపు కాల్ చేస్తానని చెప్పాడు.", "explanation": "Indirect 'would' for future report.", "options": ["will", "would", "shall", "can"]},
    {"question": "Mother said that I ___ drink milk daily.", "correct_answer": "should", "telugu_meaning": "అమ్మ నేను ప్రతిరోజూ పాలు తాగాలని చెప్పింది.", "explanation": "Indirect 'should' for advice.", "options": ["must", "should", "shall", "will"]},
    {"question": "The doctor said that I should ___ tablets after food.", "correct_answer": "take", "telugu_meaning": "డాక్టర్ భోజనం తర్వాత టాబ్లెట్స్ తీసుకోవాలని చెప్పారు.", "explanation": "Verb after should.", "options": ["take", "took", "takes", "taking"]},
    {"question": "The student said that he had ___ the project.", "correct_answer": "completed", "telugu_meaning": "విద్యార్థి ప్రాజెక్ట్ పూర్తి చేశానని చెప్పాడు.", "explanation": "Past participle after had.", "options": ["complete", "completed", "completing", "completes"]},
    {"question": "The trainer said that we should practice English ___.", "correct_answer": "daily", "telugu_meaning": "ట్రైనర్ ప్రతిరోజూ spoken English practice చేయాలని చెప్పారు.", "explanation": "Adverb of frequency.", "options": ["daily", "weekly", "yearly", "never"]},
    {"question": "Father said that I should switch ___ the lights.", "correct_answer": "off", "telugu_meaning": "నాన్న లైట్లు ఆఫ్ చేయాలని చెప్పారు.", "explanation": "Phrasal verb.", "options": ["off", "on", "up", "down"]},
    {"question": "The driver said that the bus would ___ soon.", "correct_answer": "arrive", "telugu_meaning": "డ్రైవర్ బస్ త్వరలో వస్తుందని చెప్పారు.", "explanation": "Verb after would.", "options": ["arrive", "arrived", "arrives", "arriving"]},
    {"question": "The engineer said that the software ___ updated.", "correct_answer": "was", "telugu_meaning": "సాఫ్ట్వేర్ అప్డేట్ చేయబడిందని ఇంజనీర్ చెప్పారు.", "explanation": "Past state report.", "options": ["is", "was", "been", "be"]},
    {"question": "The teacher said that we should ___ grammar daily.", "correct_answer": "practice", "telugu_meaning": "ప్రతిరోజూ grammar practice చేయాలని టీచర్ చెప్పారు.", "explanation": "Verb after should.", "options": ["practice", "practiced", "practices", "practicing"]}
]

# Generate more blanks
for i in range(10, 30):
    ex = examples[i]
    if "had" in ex['en']:
        target = "had"
    elif "was" in ex['en']:
        target = "was"
    elif "should" in ex['en']:
        target = "should"
    elif "would" in ex['en']:
        target = "would"
    else:
        target = "that"
        
    question = ex['en'].replace(target, "___")
    blanks.append({
        "question": question,
        "correct_answer": target,
        "telugu_meaning": ex['te'],
        "explanation": "Indirect speech transformation.",
        "options": ["was", "were", "would", "should", "had"] if target != "that" else ["that", "this", "these", "those"]
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
    concept = Concept.objects.filter(name='Indirect Speech').first()
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
        print("Indirect Speech updated successfully.")
    else:
        print("Concept 'Indirect Speech' not found.")

update_concept_data()
