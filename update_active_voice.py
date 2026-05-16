import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- ACTIVE VOICE DATA ---
content = "In Active Voice, the subject itself performs the action. Example: The boy plays cricket. Here: Subject -> The boy, Verb -> plays, Object -> cricket. The subject is doing the action."
rules = """
- Subject performs the action
- Structure is simple and direct
- Easy to understand
- Mostly used in daily English
- Formula: Subject + Verb + Object
"""

examples = [
    {"en": "He writes a letter.", "te": "అతను ఒక ఉత్తరం రాస్తాడు.", "explanation": "Subject 'He' action 'writes' perform chestundi."},
    {"en": "She cooks dinner every night.", "te": "ఆమె ప్రతి రాత్రి భోజనం తయారు చేస్తుంది.", "explanation": "'She' subject action 'cooks' chestundi."},
    {"en": "The teacher explains the lesson.", "te": "టీచర్ పాఠాన్ని వివరిస్తారు.", "explanation": "Teacher direct ga action perform chestunnaru."},
    {"en": "My father drives the car.", "te": "నా నాన్న కారు నడుపుతారు.", "explanation": "Subject 'father' action 'drives' chestunnaru."},
    {"en": "They play football after school.", "te": "వాళ్లు స్కూల్ తర్వాత ఫుట్బాల్ ఆడుతారు.", "explanation": "'They' subject action ni direct ga perform chestundi."},
    {"en": "I read English newspapers daily.", "te": "నేను ప్రతిరోజూ ఇంగ్లీష్ పేపర్ చదువుతాను.", "explanation": "'I' subject action 'read' chestundi."},
    {"en": "The chef prepares delicious food.", "te": "షెఫ్ రుచికరమైన ఆహారం తయారు చేస్తారు.", "explanation": "Chef action ni perform chestunnaru."},
    {"en": "The students complete the project.", "te": "విద్యార్థులు ప్రాజెక్ట్ పూర్తి చేస్తారు.", "explanation": "Students direct action perform chestunnaru."},
    {"en": "My mother cleans the house.", "te": "నా అమ్మ ఇల్లు శుభ్రం చేస్తుంది.", "explanation": "Subject 'mother' action 'cleans' chestundi."},
    {"en": "The doctor checks the patient.", "te": "డాక్టర్ రోగిని పరీక్షిస్తారు.", "explanation": "Doctor action ni direct ga perform chestunnaru."},
    {"en": "She sings beautiful songs.", "te": "ఆమె అందమైన పాటలు పాడుతుంది.", "explanation": "'She' subject action 'sings' chestundi."},
    {"en": "The manager conducts the meeting.", "te": "మేనేజర్ మీటింగ్ నిర్వహిస్తారు.", "explanation": "Manager meeting action ni lead chestunnaru."},
    {"en": "We practice spoken English daily.", "te": "మేము ప్రతిరోజూ స్పోకెన్ ఇంగ్లీష్ ప్రాక్టీస్ చేస్తాము.", "explanation": "'We' subject action perform chestundi."},
    {"en": "The police catch the thief.", "te": "పోలీసులు దొంగను పట్టుకుంటారు.", "explanation": "Police direct action perform chestunnaru."},
    {"en": "The boy flies a kite.", "te": "అబ్బాయి గాలిపటం ఎగరేస్తాడు.", "explanation": "Boy action 'flies' perform chestunnadu."},
    {"en": "She answers the phone quickly.", "te": "ఆమె వెంటనే ఫోన్కు సమాధానం ఇస్తుంది.", "explanation": "Subject 'She' performs action 'answers'."},
    {"en": "The company launches a new app.", "te": "కంపెనీ కొత్త యాప్ ప్రారంభిస్తుంది.", "explanation": "Subject 'company' performs action 'launches'."},
    {"en": "I complete my homework every evening.", "te": "నేను ప్రతి సాయంత్రం హోంవర్క్ పూర్తి చేస్తాను.", "explanation": "Subject 'I' performs action 'complete'."},
    {"en": "The baby drinks milk.", "te": "బేబీ పాలు తాగుతుంది.", "explanation": "Subject 'baby' performs action 'drinks'."},
    {"en": "My sister teaches mathematics.", "te": "నా సిస్టర్ గణితం బోధిస్తుంది.", "explanation": "Subject 'sister' performs action 'teaches'."},
    {"en": "The farmer grows vegetables.", "te": "రైతు కూరగాయలు పండిస్తాడు.", "explanation": "Subject 'farmer' performs action 'grows'."},
    {"en": "The engineer designs buildings.", "te": "ఇంజనీర్ భవనాలను డిజైన్ చేస్తారు.", "explanation": "Subject 'engineer' performs action 'designs'."},
    {"en": "The child opens the door.", "te": "పిల్లాడు తలుపు తెరుస్తాడు.", "explanation": "Subject 'child' performs action 'opens'."},
    {"en": "The waiter serves food politely.", "te": "వెయిటర్ మర్యాదగా ఆహారం అందిస్తాడు.", "explanation": "Subject 'waiter' performs action 'serves'."},
    {"en": "My friend repairs computers.", "te": "నా ఫ్రెండ్ కంప్యూటర్లు రిపేర్ చేస్తాడు.", "explanation": "Subject 'friend' performs action 'repairs'."},
    {"en": "The principal announces the results.", "te": "ప్రిన్సిపల్ ఫలితాలు ప్రకటిస్తారు.", "explanation": "Subject 'principal' performs action 'announces'."},
    {"en": "The players win the match.", "te": "ఆటగాళ్లు మ్యాచ్ గెలుస్తారు.", "explanation": "Subject 'players' performs action 'win'."},
    {"en": "The artist paints beautiful pictures.", "te": "కళాకారుడు అందమైన చిత్రాలు వేస్తాడు.", "explanation": "Subject 'artist' performs action 'paints'."},
    {"en": "The shopkeeper sells fresh fruits.", "te": "దుకాణదారు తాజా పండ్లు అమ్ముతాడు.", "explanation": "Subject 'shopkeeper' performs action 'sells'."},
    {"en": "The students ask many questions.", "te": "విద్యార్థులు చాలా ప్రశ్నలు అడుగుతారు.", "explanation": "Subject 'students' performs action 'ask'."},
    {"en": "She wears a blue dress.", "te": "ఆమె నీలం రంగు డ్రెస్ ధరిస్తుంది.", "explanation": "Subject 'She' performs action 'wears'."},
    {"en": "My uncle runs a business.", "te": "నా మామ వ్యాపారం నడుపుతారు.", "explanation": "Subject 'uncle' performs action 'runs'."},
    {"en": "The nurse helps the patient.", "te": "నర్స్ రోగికి సహాయం చేస్తుంది.", "explanation": "Subject 'nurse' performs action 'helps'."},
    {"en": "The programmer develops software.", "te": "ప్రోగ్రామర్ సాఫ్ట్వేర్ తయారు చేస్తాడు.", "explanation": "Subject 'programmer' performs action 'develops'."},
    {"en": "The children enjoy cartoons.", "te": "పిల్లలు కార్టూన్లు ఆనందిస్తారు.", "explanation": "Subject 'children' performs action 'enjoy'."},
    {"en": "The bus driver follows traffic rules.", "te": "బస్ డ్రైవర్ ట్రాఫిక్ నియమాలు పాటిస్తాడు.", "explanation": "Subject 'driver' performs action 'follows'."},
    {"en": "My cousin learns coding online.", "te": "నా cousin ఆన్లైన్లో coding నేర్చుకుంటాడు.", "explanation": "Subject 'cousin' performs action 'learns'."},
    {"en": "The singer performs on stage.", "te": "గాయకుడు స్టేజ్ పై ప్రదర్శన ఇస్తాడు.", "explanation": "Subject 'singer' performs action 'performs'."},
    {"en": "The students attend online classes.", "te": "విద్యార్థులు ఆన్లైన్ క్లాసులు attend అవుతారు.", "explanation": "Subject 'students' performs action 'attend'."},
    {"en": "The gardener waters the plants.", "te": "మాలి మొక్కలకు నీళ్లు పోస్తాడు.", "explanation": "Subject 'gardener' performs action 'waters'."},
    {"en": "The dog guards the house.", "te": "కుక్క ఇంటిని కాపాడుతుంది.", "explanation": "Subject 'dog' performs action 'guards'."},
    {"en": "The students prepare for exams.", "te": "విద్యార్థులు పరీక్షలకు సిద్ధమవుతారు.", "explanation": "Subject 'students' performs action 'prepare'."},
    {"en": "The mechanic repairs bikes.", "te": "మెకానిక్ బైక్లు రిపేర్ చేస్తాడు.", "explanation": "Subject 'mechanic' performs action 'repairs'."},
    {"en": "The actor entertains the audience.", "te": "నటుడు ప్రేక్షకులను అలరిస్తాడు.", "explanation": "Subject 'actor' performs action 'entertains'."},
    {"en": "The librarian organizes books.", "te": "లైబ్రేరియన్ పుస్తకాలను సర్దుతారు.", "explanation": "Subject 'librarian' performs action 'organizes'."},
    {"en": "The pilot flies the airplane.", "te": "పైలట్ విమానం నడుపుతాడు.", "explanation": "Subject 'pilot' performs action 'flies'."},
    {"en": "The electrician fixes the fan.", "te": "ఎలక్ట్రిషియన్ ఫ్యాన్ బాగుచేస్తాడు.", "explanation": "Subject 'electrician' performs action 'fixes'."},
    {"en": "The students celebrate the festival.", "te": "విద్యార్థులు పండుగ జరుపుకుంటారు.", "explanation": "Subject 'students' performs action 'celebrate'."},
    {"en": "My grandmother tells stories.", "te": "నా అమ్మమ్మ కథలు చెబుతుంది.", "explanation": "Subject 'grandmother' performs action 'tells'."},
    {"en": "The teacher motivates the students.", "te": "టీచర్ విద్యార్థులను ప్రోత్సహిస్తారు.", "explanation": "Teacher direct ga motivating action perform chestunnaru."}
]

blanks = [
    {"question": "The cat ___ the mouse.", "correct_answer": "caught", "telugu_meaning": "పిల్లి ఎలుకను పట్టుకుంది.", "explanation": "Action performed by the cat.", "options": ["caught", "catches", "caughted", "catching"]},
    {"question": "She ___ dinner every night.", "correct_answer": "cooks", "telugu_meaning": "ఆమె ప్రతి రాత్రి భోజనం తయారు చేస్తుంది.", "explanation": "Habitual action.", "options": ["cook", "cooks", "cooking", "cooked"]},
    {"question": "The teacher ___ the lesson clearly.", "correct_answer": "explains", "telugu_meaning": "టీచర్ పాఠాన్ని స్పష్టంగా వివరిస్తారు.", "explanation": "Action by the teacher.", "options": ["explains", "explain", "explaining", "explained"]},
    {"question": "My father ___ the car carefully.", "correct_answer": "drives", "telugu_meaning": "నా నాన్న కారు జాగ్రత్తగా నడుపుతారు.", "explanation": "Present action.", "options": ["drive", "drives", "driving", "drove"]},
    {"question": "The students ___ the project on time.", "correct_answer": "complete", "telugu_meaning": "విద్యార్థులు ప్రాజెక్టును సకాలంలో పూర్తి చేస్తారు.", "explanation": "Action by the students.", "options": ["complete", "completes", "completing", "completed"]},
    {"question": "The doctor ___ the patient.", "correct_answer": "checks", "telugu_meaning": "డాక్టర్ రోగిని పరీక్షిస్తారు.", "explanation": "Doctor's action.", "options": ["checks", "check", "checking", "checked"]},
    {"question": "The police ___ the thief.", "correct_answer": "catch", "telugu_meaning": "పోలీసులు దొంగను పట్టుకుంటారు.", "explanation": "Action by the police.", "options": ["catch", "catches", "catching", "caught"]},
    {"question": "The farmer ___ vegetables.", "correct_answer": "grows", "telugu_meaning": "రైతు కూరగాయలు పండిస్తాడు.", "explanation": "Farmer's work.", "options": ["grow", "grows", "growing", "grown"]},
    {"question": "The chef ___ delicious food.", "correct_answer": "prepares", "telugu_meaning": "షెఫ్ రుచికరమైన ఆహారం తయారు చేస్తారు.", "explanation": "Chef's action.", "options": ["prepares", "prepare", "preparing", "prepared"]},
    {"question": "The students ___ many questions.", "correct_answer": "ask", "telugu_meaning": "విద్యార్థులు చాలా ప్రశ్నలు అడుగుతారు.", "explanation": "Students' inquiry.", "options": ["asks", "ask", "asking", "asked"]}
]
# Generate 20 more blanks from the examples to reach 30
for i in range(10, 30):
    ex = examples[i]
    verb = ex['en'].split(' ')[1].replace('.', '')
    question = ex['en'].replace(verb, '___')
    blanks.append({
        "question": question,
        "correct_answer": verb,
        "telugu_meaning": ex['te'],
        "explanation": ex['explanation'],
        "options": [verb, verb + "ing", verb + "s", "was " + verb]
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
    concept = Concept.objects.filter(name='Active Voice').first()
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
        print("Active Voice updated successfully with 50 examples, 30 blanks, 30 speaking.")
    else:
        print("Concept 'Active Voice' not found.")

update_concept_data()
