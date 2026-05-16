import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- DIFFICULT WORDS DATA ---
content = "Difficult Words are English words that are hard to pronounce, spell, understand, or speak fluently. Learning these improves vocabulary, accent, and speaking confidence."
rules = """
- Syllables ga divide chesi practice cheyali.
- Slow pronunciation tho start cheyali.
- Repeat practice important.
- Difficult sounds ni clearly speak cheyali.
- Daily speaking lo use cheyali.
"""

examples = [
    {"en": "Entrepreneur", "te": "వ్యాపారవేత్త (ON-truh-pruh-NUR)", "explanation": "She became a successful entrepreneur at a young age. (Startup contexts lo common word)."},
    {"en": "Pronunciation", "te": "ఉచ్చారణ (pro-NUN-see-AY-shun)", "explanation": "Your pronunciation is improving daily."},
    {"en": "Communication", "te": "భావ వ్యక్తీకరణ (kuh-myoo-ni-KAY-shun)", "explanation": "Good communication helps during interviews."},
    {"en": "Opportunity", "te": "అవకాశం (op-er-TOO-ni-tee)", "explanation": "This job is a great opportunity for me."},
    {"en": "Responsibility", "te": "బాధ్యత (re-spon-si-BIL-i-tee)", "explanation": "Managing a team is a big responsibility."},
    {"en": "Environment", "te": "వాతావరణం (en-VY-run-ment)", "explanation": "Our office has a friendly environment."},
    {"en": "Development", "te": "అభివృద్ధి (de-VEL-up-ment)", "explanation": "Software development requires patience."},
    {"en": "Technology", "te": "సాంకేతికత (tek-NOL-uh-jee)", "explanation": "Technology is changing education rapidly."},
    {"en": "Experience", "te": "అనుభవం (ik-SPEER-ee-uhns)", "explanation": "He has three years of work experience."},
    {"en": "Knowledge", "te": "జ్ఞానం (NOL-ij)", "explanation": "Reading books increases knowledge."},
    {"en": "Schedule", "te": "సమయపట్టిక (SKED-jool)", "explanation": "My interview is scheduled for tomorrow."},
    {"en": "Necessary", "te": "అవసరం (NES-uh-ser-ee)", "explanation": "Practice is necessary for fluency."},
    {"en": "Successful", "te": "విజయవంతమైన (suk-SES-ful)", "explanation": "She is a successful software engineer."},
    {"en": "Conversation", "te": "సంభాషణ (kon-ver-SAY-shun)", "explanation": "We had a long conversation in English."},
    {"en": "Psychology", "te": "మనస్తత్వశాస్త్రం (sy-KOL-uh-jee)", "explanation": "She is studying psychology in college."},
    {"en": "Vehicle", "te": "వాహనం (VEE-i-kul)", "explanation": "That vehicle belongs to my uncle."},
    {"en": "Restaurant", "te": "భోజనశాల (RES-tuh-rant)", "explanation": "We ate dinner at a famous restaurant."},
    {"en": "Temperature", "te": "ఉష్ణోగ్రత (TEM-pruh-chur)", "explanation": "Today's temperature is very high."},
    {"en": "Particularly", "te": "ముఖ్యంగా (par-TIK-yuh-ler-lee)", "explanation": "I particularly enjoy learning English."},
    {"en": "Comfortable", "te": "సౌకర్యవంతంగా (KUMF-ter-bul)", "explanation": "Now I feel comfortable speaking English."},
    {"en": "Confidence", "te": "ఆత్మవిశ్వాసం (KON-fi-dense)", "explanation": "Confidence helps during presentations."},
    {"en": "Achievement", "te": "విజయం/సాధన (uh-CHEEV-ment)", "explanation": "Getting this job is a big achievement."},
    {"en": "Educational", "te": "విద్యాసంబంధిత (ed-yoo-KAY-shun-ul)", "explanation": "This app provides educational content."},
    {"en": "Motivation", "te": "ప్రేరణ (mo-ti-VAY-shun)", "explanation": "Daily practice gives me motivation."},
    {"en": "Dictionary", "te": "నిఘంటువు (DIK-shun-er-ee)", "explanation": "I use a dictionary to learn new words."},
    {"en": "Beautiful", "te": "అందమైన (BYOO-ti-ful)", "explanation": "She has a beautiful voice."},
    {"en": "Colleague", "te": "సహోద్యోగి (KOL-eeg)", "explanation": "My colleague helped me finish the project."},
    {"en": "Frequently", "te": "తరచుగా (FREE-kwent-lee)", "explanation": "I frequently practice spoken English."},
    {"en": "Improvement", "te": "మెరుగుదల (im-PROOV-ment)", "explanation": "I can see improvement in my speaking."},
    {"en": "Management", "te": "నిర్వహణ (MAN-ij-ment)", "explanation": "Time management is very important."},
    {"en": "Examination", "te": "పరీక్ష (eg-zam-uh-NAY-shun)", "explanation": "My examination starts next week."},
    {"en": "International", "te": "అంతర్జాతీయ (in-ter-NASH-uh-nul)", "explanation": "He works for an international company."},
    {"en": "Electricity", "te": "విద్యుత్తు (ee-lek-TRIS-i-tee)", "explanation": "The electricity went off suddenly."},
    {"en": "Mathematics", "te": "గణితం (math-uh-MAT-iks)", "explanation": "Mathematics improves logical thinking."},
    {"en": "University", "te": "విశ్వవిద్యాలయం (yoo-ni-VER-si-tee)", "explanation": "She studies at a famous university."},
    {"en": "Professional", "te": "వృత్తిపరమైన (pro-FESH-un-ul)", "explanation": "He behaves in a professional manner."},
    {"en": "Knowledgeable", "te": "జ్ఞానం ఉన్న (NOL-ij-uh-bul)", "explanation": "Our teacher is very knowledgeable."},
    {"en": "Preparation", "te": "తయారీ (prep-uh-RAY-shun)", "explanation": "Interview preparation takes time."},
    {"en": "Determination", "te": "దృఢ నిశ్చయం (dee-ter-mi-NAY-shun)", "explanation": "Determination leads to success."},
    {"en": "Photographer", "te": "ఛాయాచిత్రకారుడు (fuh-TOG-ruh-fer)", "explanation": "My friend is a professional photographer."},
    {"en": "Architecture", "te": "వాస్తుశిల్పం (AR-ki-tek-chur)", "explanation": "The building architecture looks amazing."},
    {"en": "Competition", "te": "పోటీ (kom-puh-TISH-un)", "explanation": "There is high competition in software jobs."},
    {"en": "Government", "te": "ప్రభుత్వం (GUV-ern-ment)", "explanation": "The government launched a new scheme."},
    {"en": "Recommendation", "te": "సిఫార్సు (rek-uh-men-DAY-shun)", "explanation": "The teacher gave me a recommendation letter."},
    {"en": "University", "te": "విశ్వవిద్యాలయం", "explanation": "Higher education focus."},
    {"en": "Management", "te": "నిర్వహణ", "explanation": "Workplace skill."},
    {"en": "Opportunity", "te": "అవకాశం", "explanation": "Growth focus."},
    {"en": "Communication", "te": "భావ వ్యక్తీకరణ", "explanation": "Essential skill."},
    {"en": "Confidence", "te": "ఆత్మవిశ్వాసం", "explanation": "Speaking focus."},
    {"en": "Successful", "te": "విజయవంతమైన", "explanation": "Goal focus."}
]

blanks = [
    {"question": "Good ___ helps during interviews.", "correct_answer": "communication", "telugu_meaning": "మంచి communication interviews లో సహాయపడుతుంది.", "explanation": "Interview skill.", "options": ["communication", "knowledge", "preparation", "confidence"]},
    {"question": "Daily practice improves your ___.", "correct_answer": "pronunciation", "telugu_meaning": "ప్రతిరోజూ ప్రాక్టీస్ చేస్తే నీ ఉచ్చారణ మెరుగవుతుంది.", "explanation": "Speaking focus.", "options": ["pronunciation", "grammar", "writing", "reading"]},
    {"question": "This job is a great ___.", "correct_answer": "opportunity", "telugu_meaning": "ఈ ఉద్యోగం ఒక మంచి అవకాశం.", "explanation": "Career growth.", "options": ["opportunity", "problem", "difficult", "task"]},
    {"question": "Reading books increases ___.", "correct_answer": "knowledge", "telugu_meaning": "పుస్తకాలు చదవడం వల్ల జ్ఞానం పెరుగుతుంది.", "explanation": "Learning focus.", "options": ["knowledge", "money", "time", "speed"]},
    {"question": "Time ___ is very important.", "correct_answer": "management", "telugu_meaning": "సమయ నిర్వహణ చాలా ముఖ్యం.", "explanation": "Workplace skill.", "options": ["management", "running", "passing", "wasting"]},
    {"question": "Interview ___ takes time.", "correct_answer": "preparation", "telugu_meaning": "ఇంటర్వ్యూ తయారీకి సమయం పడుతుంది.", "explanation": "Process focus.", "options": ["preparation", "finishing", "waiting", "calling"]},
    {"question": "Confidence improves public ___.", "correct_answer": "speaking", "telugu_meaning": "ఆత్మవిశ్వాసం పబ్లిక్ స్పీకింగ్‌ను మెరుగుపరుస్తుంది.", "explanation": "Skill focus.", "options": ["speaking", "writing", "sleeping", "eating"]},
    {"question": "My brother wants to become an ___.", "correct_answer": "entrepreneur", "telugu_meaning": "మా అన్నయ్య వ్యాపారవేత్త అవ్వాలనుకుంటున్నాడు.", "explanation": "Business goal.", "options": ["entrepreneur", "employee", "student", "teacher"]},
    {"question": "She studies at a famous ___.", "correct_answer": "university", "telugu_meaning": "ఆమె ఒక ప్రసిద్ధ విశ్వవిద్యాలయంలో చదువుతోంది.", "explanation": "Education place.", "options": ["university", "school", "home", "office"]},
    {"question": "Technology is changing ___ rapidly.", "correct_answer": "education", "telugu_meaning": "టెక్నాలజీ విద్యావిధానాన్ని వేగంగా మారుస్తోంది.", "explanation": "Impact focus.", "options": ["education", "weather", "food", "sports"]}
]

# Add 20 more blanks from examples list
for i in range(10, 30):
    ex = examples[i]
    target = ex['en'].lower()
    question = f"___ is important for success." if "Successful" in ex['en'] else f"We use a ___ to learn new words." if "Dictionary" in ex['en'] else f"He has three years of work ___." if "Experience" in ex['en'] else f"Her ___ was amazing."
    blanks.append({
        "question": question,
        "correct_answer": ex['en'],
        "telugu_meaning": ex['te'],
        "explanation": "Advanced vocabulary.",
        "options": [ex['en'], "thing", "work", "job"]
    })

speaking_sentences = [
    "Your pronunciation is improving daily.", "Good communication builds confidence.",
    "This opportunity can change my career.", "Software development requires patience.",
    "Technology is changing the world rapidly.", "Reading books improves knowledge.",
    "Interview preparation is very important.", "Confidence helps during presentations.",
    "Time management improves productivity.", "The office environment is friendly.",
    "Practice is necessary for fluency.", "Speaking English creates opportunities.",
    "My colleague helped me complete the task.", "The temperature is very high today.",
    "This achievement motivates me.", "Educational apps help students learn faster.",
    "I frequently practice spoken English.", "The university offers quality education.",
    "Professional communication is important.", "Determination leads to success.",
    "The photographer captured beautiful moments.", "Architecture requires creativity and planning.",
    "Competition is increasing in every field.", "Improvement comes with daily practice.",
    "The government launched a new project.", "The teacher gave me a recommendation letter.",
    "We had an interesting conversation yesterday.", "Winning the competition was a huge achievement.",
    "Confidence removes fear while speaking.", "My goal is to become a successful entrepreneur"
]

speaking = []
for sent in speaking_sentences:
    speaking.append({
        "question": sent,
        "telugu_meaning": "",
        "explanation": "Pronounce the difficult words clearly."
    })

def update_concept_data():
    concept = Concept.objects.filter(name='Difficult Words').first()
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
        print("Difficult Words updated successfully.")
    else:
        print("Concept 'Difficult Words' not found.")

update_concept_data()
