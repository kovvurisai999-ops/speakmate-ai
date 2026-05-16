import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- PASSIVE VOICE DATA ---
content = "In Passive Voice, the action is more important than the doer. The object of the active sentence becomes the subject in passive voice."
rules = """
- Object receives the action
- Focus is on action
- 'by' is used for doer sometimes
- Be verb + past participle used
- Formula: Object + Be Verb + Past Participle + by Subject
"""

examples = [
    {"en": "The homework is completed by the students.", "te": "హోంవర్క్ విద్యార్థులచే పూర్తి చేయబడింది.", "explanation": "Focus 'homework' meeda undi kabatti passive voice use chesam."},
    {"en": "The food is prepared by my mother.", "te": "ఆహారం నా అమ్మ చేత తయారు చేయబడుతుంది.", "explanation": "Food important kabatti passive structure use chesam."},
    {"en": "The lesson is explained by the teacher.", "te": "పాఠం టీచర్ ద్వారా వివరించబడుతుంది.", "explanation": "Lesson main focus kabatti passive voice use chesam."},
    {"en": "The car is driven by my father.", "te": "కారు నా నాన్న చేత నడపబడుతుంది.", "explanation": "Object 'car' importance meeda focus undi."},
    {"en": "The match was won by our team.", "te": "మ్యాచ్ మా జట్టు చేత గెలవబడింది.", "explanation": "Match result important kabatti passive voice use chesam."},
    {"en": "The project is submitted by the employees.", "te": "ప్రాజెక్ట్ ఉద్యోగులచే సమర్పించబడుతుంది.", "explanation": "Passive focus on project."},
    {"en": "The room is cleaned by the workers.", "te": "గది కార్మికులచే శుభ్రం చేయబడుతుంది.", "explanation": "Passive focus on room."},
    {"en": "The patient is checked by the doctor.", "te": "రోగి డాక్టర్ చేత పరీక్షించబడుతాడు.", "explanation": "Passive focus on patient."},
    {"en": "The documents are verified by the manager.", "te": "డాక్యుమెంట్లు మేనేజర్ చేత పరిశీలించబడతాయి.", "explanation": "Passive focus on documents."},
    {"en": "The story was written by my friend.", "te": "కథ నా ఫ్రెండ్ చేత రాయబడింది.", "explanation": "Passive focus on story."},
    {"en": "The email is sent by the HR team.", "te": "ఈమెయిల్ HR టీమ్ చేత పంపబడుతుంది.", "explanation": "Email sent action focus."},
    {"en": "The meeting is conducted by the manager.", "te": "మీటింగ్ మేనేజర్ చేత నిర్వహించబడుతుంది.", "explanation": "Meeting conduct action focus."},
    {"en": "The plants are watered by the gardener.", "te": "మొక్కలు మాలి చేత నీరు పోయబడతాయి.", "explanation": "Plants receiving action."},
    {"en": "The books are arranged by the librarian.", "te": "పుస్తకాలు లైబ్రేరియన్ చేత సర్దబడతాయి.", "explanation": "Books receiving action."},
    {"en": "The house was painted by the workers.", "te": "ఇల్లు కార్మికులచే రంగు వేయబడింది.", "explanation": "House receiving action."},
    {"en": "The questions are answered by the students.", "te": "ప్రశ్నలకు విద్యార్థులు సమాధానం ఇస్తారు.", "explanation": "Questions focus."},
    {"en": "The report is prepared by the assistant.", "te": "రిపోర్ట్ అసిస్టెంట్ చేత తయారు చేయబడుతుంది.", "explanation": "Report focus."},
    {"en": "The festival is celebrated by the villagers.", "te": "పండుగ గ్రామస్తులచే జరుపబడుతుంది.", "explanation": "Festival focus."},
    {"en": "The software is developed by engineers.", "te": "సాఫ్ట్వేర్ ఇంజనీర్లచే అభివృద్ధి చేయబడుతుంది.", "explanation": "Software focus."},
    {"en": "The movie was directed by a famous director.", "te": "సినిమా ప్రముఖ దర్శకుడు చేత దర్శకత్వం వహించబడింది.", "explanation": "Movie focus."},
    {"en": "The roads are repaired by the workers.", "te": "రోడ్లు కార్మికులచే మరమ్మత్తు చేయబడతాయి.", "explanation": "Roads focus."},
    {"en": "The tickets are booked online.", "te": "టికెట్లు ఆన్లైన్లో బుక్ చేయబడతాయి.", "explanation": "Tickets focus."},
    {"en": "The files are uploaded by the employee.", "te": "ఫైళ్ళు ఉద్యోగి చేత అప్లోడ్ చేయబడతాయి.", "explanation": "Files focus."},
    {"en": "The baby is cared for by the nurse.", "te": "బేబీ నర్స్ చేత చూసుకోబడుతుంది.", "explanation": "Baby focus."},
    {"en": "The hall is decorated for the function.", "te": "హాల్ ఫంక్షన్ కోసం అలంకరించబడింది.", "explanation": "Hall focus."},
    {"en": "The exam papers are corrected by the teacher.", "te": "పరీక్ష పేపర్లు టీచర్ చేత సరిచేయబడతాయి.", "explanation": "Papers focus."},
    {"en": "The package was delivered yesterday.", "te": "పార్సెల్ నిన్న డెలివరీ చేయబడింది.", "explanation": "Package focus."},
    {"en": "The thief was caught by the police.", "te": "దొంగ పోలీసులచే పట్టుబడ్డాడు.", "explanation": "Thief focus."},
    {"en": "The rules are followed by the students.", "te": "నియమాలు విద్యార్థులచే పాటించబడతాయి.", "explanation": "Rules focus."},
    {"en": "The songs are sung beautifully by her.", "te": "పాటలు ఆమె చేత అందంగా పాడబడతాయి.", "explanation": "Songs focus."},
    {"en": "The building was designed by an architect.", "te": "భవనం ఆర్కిటెక్ట్ చేత డిజైన్ చేయబడింది.", "explanation": "Building focus."},
    {"en": "The work is finished on time.", "te": "పని సమయానికి పూర్తి చేయబడుతుంది.", "explanation": "Work focus."},
    {"en": "The room is locked every night.", "te": "గది ప్రతి రాత్రి లాక్ చేయబడుతుంది.", "explanation": "Room focus."},
    {"en": "The cake was baked by my sister.", "te": "కేక్ నా సిస్టర్ చేత తయారు చేయబడింది.", "explanation": "Cake focus."},
    {"en": "The train is operated by the government.", "te": "ట్రైన్ ప్రభుత్వంచే నడపబడుతుంది.", "explanation": "Train focus."},
    {"en": "The laptop is repaired by the technician.", "te": "ల్యాప్టాప్ టెక్నీషియన్ చేత బాగుచేయబడుతుంది.", "explanation": "Laptop focus."},
    {"en": "The students are guided by the mentor.", "te": "విద్యార్థులు మెంటర్ చేత మార్గనిర్దేశం చేయబడతారు.", "explanation": "Students focus."},
    {"en": "The bills are paid online.", "te": "బిల్లులు ఆన్లైన్లో చెల్లించబడతాయి.", "explanation": "Bills focus."},
    {"en": "The office is opened at 9 AM.", "te": "ఆఫీస్ ఉదయం 9 గంటలకు తెరవబడుతుంది.", "explanation": "Office focus."},
    {"en": "The photos were taken during the trip.", "te": "ఫోటోలు ట్రిప్ సమయంలో తీసుకోబడ్డాయి.", "explanation": "Photos focus."},
    {"en": "The payment is received successfully.", "te": "పేమెంట్ విజయవంతంగా స్వీకరించబడింది.", "explanation": "Payment focus."},
    {"en": "The students are encouraged by the principal.", "te": "విద్యార్థులు ప్రిన్సిపల్ చేత ప్రోత్సహించబడతారు.", "explanation": "Students focus."},
    {"en": "The machine is operated carefully.", "te": "మెషిన్ జాగ్రత్తగా నడపబడుతుంది.", "explanation": "Machine focus."},
    {"en": "The room was booked online.", "te": "గది ఆన్లైన్లో బుక్ చేయబడింది.", "explanation": "Room focus."},
    {"en": "The application is approved by the manager.", "te": "అప్లికేషన్ మేనేజర్ చేత ఆమోదించబడుతుంది.", "explanation": "Application focus."},
    {"en": "The clothes are washed every Sunday.", "te": "బట్టలు ప్రతి ఆదివారం ఉతకబడతాయి.", "explanation": "Clothes focus."},
    {"en": "The speech was delivered by the CEO.", "te": "స్పీచ్ CEO చేత ఇవ్వబడింది.", "explanation": "Speech focus."},
    {"en": "The menu is updated regularly.", "te": "మెనూ క్రమం తప్పకుండా అప్డేట్ చేయబడుతుంది.", "explanation": "Menu focus."},
    {"en": "The students are trained by experts.", "te": "విద్యార్థులు నిపుణులచే శిక్షణ పొందుతారు.", "explanation": "Students focus."},
    {"en": "The message was shared with everyone.", "te": "సందేశం అందరితో పంచుకోబడింది.", "explanation": "Focus 'message' meeda undi kabatti passive structure use chesam."}
]

blanks = [
    {"question": "The homework ___ completed by the students.", "correct_answer": "is", "telugu_meaning": "హోంవర్క్ విద్యార్థులచే పూర్తి చేయబడింది.", "explanation": "Passive 'is' for present singular.", "options": ["is", "are", "was", "be"]},
    {"question": "The food ___ prepared by my mother.", "correct_answer": "is", "telugu_meaning": "ఆహారం నా అమ్మ చేత తయారు చేయబడుతుంది.", "explanation": "Passive 'is' for present singular.", "options": ["is", "am", "are", "been"]},
    {"question": "The lesson ___ explained by the teacher.", "correct_answer": "is", "telugu_meaning": "పాఠం టీచర్ ద్వారా వివరించబడుతుంది.", "explanation": "Passive 'is' for present singular.", "options": ["is", "are", "was", "were"]},
    {"question": "The match ___ won by our team.", "correct_answer": "was", "telugu_meaning": "మ్యాచ్ మా జట్టు చేత గెలవబడింది.", "explanation": "Passive 'was' for past singular.", "options": ["is", "was", "were", "been"]},
    {"question": "The documents ___ verified by the manager.", "correct_answer": "are", "telugu_meaning": "డాక్యుమెంట్లు మేనేజర్ చేత పరిశీలించబడతాయి.", "explanation": "Passive 'are' for present plural.", "options": ["is", "are", "was", "were"]},
    {"question": "The story ___ written by my friend.", "correct_answer": "was", "telugu_meaning": "కథ నా ఫ్రెండ్ చేత రాయబడింది.", "explanation": "Passive 'was' for past singular.", "options": ["is", "was", "are", "been"]},
    {"question": "The books ___ arranged by the librarian.", "correct_answer": "are", "telugu_meaning": "పుస్తకాలు లైబ్రేరియన్ చేత సర్దబడతాయి.", "explanation": "Passive 'are' for present plural.", "options": ["is", "are", "was", "be"]},
    {"question": "The thief ___ caught by the police.", "correct_answer": "was", "telugu_meaning": "దొంగ పోలీసులచే పట్టుబడ్డాడు.", "explanation": "Passive 'was' for past singular.", "options": ["is", "was", "were", "been"]},
    {"question": "The roads ___ repaired by the workers.", "correct_answer": "are", "telugu_meaning": "రోడ్లు కార్మికులచే మరమ్మత్తు చేయబడతాయి.", "explanation": "Passive 'are' for present plural.", "options": ["is", "are", "was", "been"]},
    {"question": "The bills ___ paid online.", "correct_answer": "are", "telugu_meaning": "బిల్లులు ఆన్లైన్లో చెల్లించబడతాయి.", "explanation": "Passive 'are' for present plural.", "options": ["is", "are", "was", "be"]}
]
# Add 20 more blanks
for i in range(10, 30):
    ex = examples[i]
    be_verb = "is" if "is" in ex['en'] else "are" if "are" in ex['en'] else "was" if "was" in ex['en'] else "were"
    question = ex['en'].replace(be_verb, "___")
    blanks.append({
        "question": question,
        "correct_answer": be_verb,
        "telugu_meaning": ex['te'],
        "explanation": ex['explanation'],
        "options": ["is", "are", "was", "were"]
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
    concept = Concept.objects.filter(name='Passive Voice').first()
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
        print("Passive Voice updated successfully.")
    else:
        print("Concept 'Passive Voice' not found.")

update_concept_data()
