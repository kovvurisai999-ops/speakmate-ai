import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- CONDITIONAL SENTENCES DATA ---
content = "Conditional Sentences are used to talk about possibilities, future situations, imaginary situations, results of actions, and cause and effect. They usually use: if + condition + result."
rules = """
- 'if' clause condition ni chupistundi
- Main clause result ni chupistundi
- Tense type batti structure change avvutundi
- Zero Conditional: General truth (If+Present Simple, Present Simple)
- First Conditional: Real future possibility (If+Present Simple, will+Base Verb)
- Second Conditional: Imaginary situation (If+Past Simple, would+Base Verb)
- Third Conditional: Past imaginary situation (If+Past Perfect, would have+Past Participle)
"""

examples = [
    {"en": "If you practice English daily, you will improve quickly.", "te": "నువ్వు ప్రతిరోజూ ఇంగ్లీష్ practice చేస్తే, త్వరగా improve అవుతావు.", "explanation": "Future real possibility kabatti first conditional use chesam."},
    {"en": "If it rains, we will stay at home.", "te": "వర్షం పడితే, మేము ఇంట్లో ఉంటాం.", "explanation": "Possible future situation ni chupistundi."},
    {"en": "If you heat ice, it melts.", "te": "నువ్వు మంచును వేడి చేస్తే, అది కరుగుతుంది.", "explanation": "General truth kabatti zero conditional use chesam."},
    {"en": "If I had a bike, I would travel daily.", "te": "నా దగ్గర bike ఉంటే, నేను ప్రతిరోజూ ప్రయాణం చేసేవాడిని.", "explanation": "Imaginary situation kabatti second conditional use chesam."},
    {"en": "If she had studied harder, she would have passed the exam.", "te": "ఆమె బాగా చదివి ఉంటే, పరీక్షలో pass అయ్యేది.", "explanation": "Past regret situation kabatti third conditional use chesam."},
    {"en": "If you wake up early, you will reach college on time.", "te": "నువ్వు త్వరగా లేస్తే, కాలేజీకి సమయానికి చేరుకుంటావు.", "explanation": "First conditional."},
    {"en": "If I become a software engineer, I will help my family.", "te": "నేను software engineer అయితే, నా కుటుంబానికి సహాయం చేస్తాను.", "explanation": "Future goal."},
    {"en": "If they invite me, I will attend the function.", "te": "వాళ్లు నన్ను ఆహ్వానిస్తే, నేను function కి వెళ్తాను.", "explanation": "Real possibility."},
    {"en": "If you drink enough water, you stay healthy.", "te": "నువ్వు సరిపడా నీళ్లు తాగితే, ఆరోగ్యంగా ఉంటావు.", "explanation": "General truth."},
    {"en": "If he earns more money, he will buy a new phone.", "te": "అతను ఎక్కువ డబ్బు సంపాదిస్తే, కొత్త ఫోన్ కొనుగోలు చేస్తాడు.", "explanation": "First conditional."},
    {"en": "If I knew coding well, I would build apps.", "te": "నాకు coding బాగా వచ్చి ఉంటే, apps build చేసేవాడిని.", "explanation": "Second conditional (imaginary now)."},
    {"en": "If students study regularly, they get good marks.", "te": "విద్యార్థులు regular గా చదివితే, మంచి మార్కులు వస్తాయి.", "explanation": "General truth."},
    {"en": "If you speak confidently, people will listen to you.", "te": "నువ్వు confident గా మాట్లాడితే, ప్రజలు నీ మాట వింటారు.", "explanation": "First conditional."},
    {"en": "If she had attended the interview, she would have got the job.", "te": "ఆమె interview కి వెళ్లి ఉంటే, ఉద్యోగం వచ్చేది.", "explanation": "Third conditional."},
    {"en": "If we save money, we will travel next year.", "te": "మనం డబ్బు save చేస్తే, వచ్చే సంవత్సరం ప్రయాణం చేస్తాం.", "explanation": "First conditional."},
    {"en": "If I were rich, I would start a company.", "te": "నేను ధనవంతుడిని అయితే, కంపెనీ ప్రారంభించేవాడిని.", "explanation": "Second conditional."},
    {"en": "If you touch fire, it burns.", "te": "నువ్వు మంటను తాకితే, కాలిపోతుంది.", "explanation": "Zero conditional."},
    {"en": "If the bus arrives early, we will reach office quickly.", "te": "బస్ త్వరగా వస్తే, మేము office కి త్వరగా చేరుకుంటాం.", "explanation": "First conditional."},
    {"en": "If I had more time, I would learn spoken English better.", "te": "నాకు ఎక్కువ సమయం ఉంటే, spoken English ఇంకా బాగా నేర్చుకునేవాడిని.", "explanation": "Second conditional."},
    {"en": "If they had informed me earlier, I would have attended the meeting.", "te": "వాళ్లు ముందే చెప్పి ఉంటే, నేను meeting కి వెళ్లేవాడిని.", "explanation": "Third conditional."},
    {"en": "If you eat healthy food, you stay fit.", "te": "నువ్వు ఆరోగ్యకరమైన ఆహారం తింటే, fit గా ఉంటావు.", "explanation": "Zero conditional."},
    {"en": "If she learns communication skills, she will get a better job.", "te": "ఆమె communication skills నేర్చుకుంటే, మంచి ఉద్యోగం వస్తుంది.", "explanation": "First conditional."},
    {"en": "If I had a laptop, I would practice coding daily.", "te": "నా దగ్గర laptop ఉంటే, నేను ప్రతిరోజూ coding practice చేసేవాడిని.", "explanation": "Second conditional."},
    {"en": "If he had listened to the teacher, he would have understood the lesson.", "te": "అతను టీచర్ మాట విని ఉంటే, పాఠం అర్థమయ్యేది.", "explanation": "Third conditional."},
    {"en": "If we work hard, we will achieve success.", "te": "మనం కష్టపడితే, విజయం సాధిస్తాం.", "explanation": "First conditional."},
    {"en": "If you press this button, the machine starts.", "te": "నువ్వు ఈ button నొక్కితే, machine start అవుతుంది.", "explanation": "Zero conditional."},
    {"en": "If she practiced daily, she would speak English fluently.", "te": "ఆమె ప్రతిరోజూ practice చేస్తే, fluently మాట్లాడేది.", "explanation": "Second conditional."},
    {"en": "If I had known about the event, I would have participated.", "te": "నాకు event గురించి తెలిసి ఉంటే, పాల్గొనేవాడిని.", "explanation": "Third conditional."},
    {"en": "If you revise lessons daily, exams become easier.", "te": "నువ్వు lessons ప్రతిరోజూ revise చేస్తే, exams సులభం అవుతాయి.", "explanation": "Zero conditional."},
    {"en": "If he gets selected, he will join the company.", "te": "అతను select అయితే, కంపెనీలో join అవుతాడు.", "explanation": "First conditional."},
    {"en": "If I were the manager, I would help employees.", "te": "నేను manager అయితే, ఉద్యోగులకు సహాయం చేసేవాడిని.", "explanation": "Second conditional."},
    {"en": "If they had started early, they would have reached on time.", "te": "వాళ్లు త్వరగా బయలుదేరి ఉంటే, సమయానికి చేరుకునేవారు.", "explanation": "Third conditional."},
    {"en": "If you switch off the fan, electricity is saved.", "te": "నువ్వు ఫ్యాన్ ఆఫ్ చేస్తే, విద్యుత్ save అవుతుంది.", "explanation": "Zero conditional."},
    {"en": "If she improves her pronunciation, she will speak clearly.", "te": "ఆమె pronunciation మెరుగుపరుచుకుంటే, స్పష్టంగా మాట్లాడుతుంది.", "explanation": "First conditional."},
    {"en": "If I had confidence, I would speak on stage.", "te": "నాకు confidence ఉంటే, stage మీద మాట్లాడేవాడిని.", "explanation": "Second conditional."},
    {"en": "If he had prepared well, he would have answered correctly.", "te": "అతను బాగా prepare అయ్యి ఉంటే, సరైన సమాధానం చెప్పేవాడు.", "explanation": "Third conditional."},
    {"en": "If we plant trees, the environment becomes better.", "te": "మనం చెట్లు నాటితే, పర్యావరణం మెరుగవుతుంది.", "explanation": "Zero conditional."},
    {"en": "If you complete the course, you will gain skills.", "te": "నువ్వు course పూర్తి చేస్తే, skills వస్తాయి.", "explanation": "First conditional."},
    {"en": "If I were taller, I would become a basketball player.", "te": "నేను పొడవుగా ఉంటే, basketball player అయ్యేవాడిని.", "explanation": "Second conditional."},
    {"en": "If she had saved money, she would have bought a bike.", "te": "ఆమె డబ్బు save చేసి ఉంటే, bike కొనుగోలు చేసేది.", "explanation": "Third conditional."},
    {"en": "If you practice speaking daily, your confidence increases.", "te": "నువ్వు ప్రతిరోజూ speaking practice చేస్తే, confidence పెరుగుతుంది.", "explanation": "Zero conditional."},
    {"en": "If he gets free time, he will watch a movie.", "te": "అతనికి free time వస్తే, సినిమా చూస్తాడు.", "explanation": "First conditional."},
    {"en": "If I had better English, I would crack interviews easily.", "te": "నాకు మంచి ఇంగ్లీష్ వచ్చి ఉంటే, interviews సులభంగా crack చేసేవాడిని.", "explanation": "Second conditional."},
    {"en": "If they had booked tickets earlier, they would have got seats.", "te": "వాళ్లు ముందే tickets book చేసి ఉంటే, seats దొరికేవి.", "explanation": "Third conditional."},
    {"en": "If students ask questions, learning becomes easier.", "te": "విద్యార్థులు ప్రశ్నలు అడిగితే, learning సులభం అవుతుంది.", "explanation": "Zero conditional."},
    {"en": "If she studies coding, she will become a developer.", "te": "ఆమె coding చదివితే, developer అవుతుంది.", "explanation": "First conditional."},
    {"en": "If I were confident, I would attend public speaking events.", "te": "నాకు confidence ఉంటే, public speaking events కి వెళ్తాను.", "explanation": "Second conditional."},
    {"en": "If he had practiced speaking, he would have spoken fluently.", "te": "అతను speaking practice చేసి ఉంటే, fluently మాట్లాడేవాడు.", "explanation": "Third conditional."},
    {"en": "If we learn English, we get more opportunities.", "te": "మనం ఇంగ్లీష్ నేర్చుకుంటే, ఎక్కువ అవకాశాలు వస్తాయి.", "explanation": "Zero conditional."},
    {"en": "If you believe in yourself, you will achieve your goals.", "te": "నువ్వు నిన్ను నువ్వు నమ్మితే, నీ goals సాధిస్తావు.", "explanation": "First conditional."}
]

blanks = [
    {"question": "If you study hard, you ___ pass the exam.", "correct_answer": "will", "telugu_meaning": "నువ్వు బాగా చదివితే, పరీక్షలో పాస్ అవుతావు.", "explanation": "First conditional 'will'.", "options": ["will", "would", "would have", "shall"]},
    {"question": "If it rains, we ___ stay at home.", "correct_answer": "will", "telugu_meaning": "వర్షం పడితే, మేము ఇంట్లో ఉంటాం.", "explanation": "First conditional 'will'.", "options": ["will", "would", "had", "be"]},
    {"question": "If you heat water, it ___.", "correct_answer": "boils", "telugu_meaning": "నువ్వు నీటిని వేడి చేస్తే, అది మరుగుతుంది.", "explanation": "Zero conditional present simple.", "options": ["boils", "boil", "boiled", "boiling"]},
    {"question": "If I had money, I ___ buy a car.", "correct_answer": "would", "telugu_meaning": "నా దగ్గర డబ్బు ఉంటే, నేను కారు కొనేవాడిని.", "explanation": "Second conditional 'would'.", "options": ["would", "will", "would have", "can"]},
    {"question": "If she had studied harder, she would have ___ the exam.", "correct_answer": "passed", "telugu_meaning": "ఆమె బాగా చదివి ఉంటే, పరీక్షలో పాస్ అయ్యేది.", "explanation": "Third conditional past participle.", "options": ["passed", "pass", "passing", "passes"]},
    {"question": "If you wake up early, you ___ reach college on time.", "correct_answer": "will", "telugu_meaning": "నువ్వు త్వరగా లేస్తే, కాలేజీకి సమయానికి చేరుకుంటావు.", "explanation": "First conditional 'will'.", "options": ["will", "would", "can", "must"]},
    {"question": "If students study regularly, they ___ good marks.", "correct_answer": "get", "telugu_meaning": "విద్యార్థులు regular గా చదివితే, మంచి మార్కులు వస్తాయి.", "explanation": "Zero conditional present.", "options": ["get", "gets", "getting", "got"]},
    {"question": "If you touch fire, it ___.", "correct_answer": "burns", "telugu_meaning": "నువ్వు మంటను తాకితే, కాలిపోతుంది.", "explanation": "Zero conditional present.", "options": ["burns", "burn", "burning", "burned"]},
    {"question": "If I knew coding well, I ___ build apps.", "correct_answer": "would", "telugu_meaning": "నాకు coding బాగా వచ్చి ఉంటే, apps build చేసేవాడిని.", "explanation": "Second conditional 'would'.", "options": ["would", "will", "can", "must"]},
    {"question": "If he gets selected, he ___ join the company.", "correct_answer": "will", "telugu_meaning": "అతను select అయితే, కంపెనీలో join అవుతాడు.", "explanation": "First conditional 'will'.", "options": ["will", "would", "could", "shall"]}
]

# Add 20 more blanks
for i in range(10, 30):
    ex = examples[i]
    if "will" in ex['en']: target = "will"
    elif "would have" in ex['en']: target = "would have"
    elif "would" in ex['en']: target = "would"
    elif "gets" in ex['en']: target = "gets"
    else: target = "if"
        
    question = ex['en'].replace(target, "___")
    blanks.append({
        "question": question,
        "correct_answer": target,
        "telugu_meaning": ex['te'],
        "explanation": "Conditional structure.",
        "options": ["will", "would", "would have", "should"] if target != "if" else ["if", "when", "unless", "but"]
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
    concept = Concept.objects.filter(name='Conditional Sentences').first()
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
        print("Conditional Sentences updated successfully.")
    else:
        print("Concept 'Conditional Sentences' not found.")

update_concept_data()
