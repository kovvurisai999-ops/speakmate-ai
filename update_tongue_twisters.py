import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- TONGUE TWISTERS DATA ---
content = "Tongue Twisters are difficult sentences used to improve pronunciation, fluency, mouth movement, accent, speaking speed, and voice clarity. They contain similar sounds repeated many times."
rules = """
- Why Important: English pronunciation, mouth flexibility, confidence, fast speaking.
- Key Rules: Slow ga start cheyali, clear pronunciation maintain cheyali, daily practice cheyali.
- Accuracy first, then speed.
"""

examples = [
    {"en": "She sells seashells by the seashore.", "te": "ఆమె సముద్ర తీరంలో పుటలు అమ్ముతుంది.", "explanation": "'s' and 'sh' pronunciation practice."},
    {"en": "Peter Piper picked a peck of pickled peppers.", "te": "పీటర్ పికిల్ చేసిన మిరపకాయల బుట్ట తీసుకున్నాడు.", "explanation": "'p' sound fast pronunciation practice."},
    {"en": "Red lorry, yellow lorry.", "te": "ఎరుపు లారీ, పసుపు లారీ.", "explanation": "'r' and 'l' sounds clarity."},
    {"en": "Thirty-three thieves thought that they thrilled the throne throughout Thursday.", "te": "ముప్పై మూడు దొంగలు గురువారం సింహాసనాన్ని ఆకట్టుకున్నామని అనుకున్నారు.", "explanation": "'th' sound practice."},
    {"en": "How can a clam cram in a clean cream can?", "te": "ఒక clam clean cream can లో ఎలా చేరుతుంది?", "explanation": "'cl' and 'cr' sounds practice."},
    {"en": "I scream, you scream, we all scream for ice cream.", "te": "నేను అరుస్తాను, నువ్వు అరుస్తావు, మనమంతా ఐస్క్రీమ్ కోసం అరుస్తాం.", "explanation": "'scr' sound practice."},
    {"en": "A big black bug bit a big black bear.", "te": "ఒక పెద్ద నల్ల పురుగు పెద్ద నల్ల ఎలుగుబంటిని కాటేసింది.", "explanation": "Alliteration with 'b'."},
    {"en": "Fresh fried fish, fish fresh fried.", "te": "తాజాగా వేయించిన చేప.", "explanation": "F sound practice."},
    {"en": "Six slippery snails slid slowly seaward.", "te": "ఆరు జారే నత్తలు నెమ్మదిగా సముద్రం వైపు జారాయి.", "explanation": "S sound practice."},
    {"en": "Betty bought some butter but the butter was bitter.", "te": "బెట్టి వెన్న కొన్నది కానీ అది చేదుగా ఉంది.", "explanation": "B sound practice."},
    {"en": "Blue bluebird blinks.", "te": "నీలి పక్షి కళ్లను మూసింది.", "explanation": "Bl sound practice."},
    {"en": "Nine nice night nurses nursing nicely.", "te": "తొమ్మిది మంచి నర్స్లు బాగా సేవ చేస్తున్నారు.", "explanation": "N sound practice."},
    {"en": "Round and round the rugged rock the ragged rascal ran.", "te": "ఒక అల్లరి వ్యక్తి గట్టిపొరల చుట్టూ పరుగెత్తాడు.", "explanation": "R sound practice."},
    {"en": "Truly rural.", "te": "నిజంగా గ్రామీణ ప్రాంతం.", "explanation": "R/L challenge."},
    {"en": "Which witch wished which wicked wish?", "te": "ఏ మంత్రగత్తె ఏ కోరిక కోరింది?", "explanation": "W sound practice."},
    {"en": "Fred fed Ted bread and Ted fed Fred bread.", "te": "ఫ్రెడ్ టెడ్కు బ్రెడ్ ఇచ్చాడు, టెడ్ ఫ్రెడ్కు బ్రెడ్ ఇచ్చాడు.", "explanation": "F/T/B combination."},
    {"en": "He threw three free throws.", "te": "అతను మూడు free throws వేశాడు.", "explanation": "Th/F sounds."},
    {"en": "A proper copper coffee pot.", "te": "సరైన రాగి కాఫీ పాత్ర.", "explanation": "P/C sounds."},
    {"en": "Lesser leather never weathered wetter weather better.", "te": "తక్కువ నాణ్యత leather తడి వాతావరణాన్ని తట్టుకోలేదు.", "explanation": "Th/W sounds."},
    {"en": "Four furious friends fought for the phone.", "te": "నాలుగు కోపంగా ఉన్న స్నేహితులు ఫోన్ కోసం పోరాడారు.", "explanation": "F sound alliteration."},
    {"en": "Crazy cats cry cautiously.", "te": "వింత పిల్లులు జాగ్రత్తగా అరుస్తాయి.", "explanation": "C sound practice."},
    {"en": "Tiny turtles talk too much.", "te": "చిన్న తాబేళ్లు చాలా మాట్లాడుతాయి.", "explanation": "T sound practice."},
    {"en": "Seven slippery snakes slid silently.", "te": "ఏడు జారే పాములు నిశ్శబ్దంగా జారాయి.", "explanation": "S sound practice."},
    {"en": "Busy buzzing bees buzzed busily.", "te": "బిజీ తేనెటీగలు గింగిరాలు చేశాయి.", "explanation": "B/Z sounds."},
    {"en": "Thin sticks, thick bricks.", "te": "సన్నని కర్రలు, మందమైన ఇటుకలు.", "explanation": "Th/St/Br sounds."},
    {"en": "Five fast fish flew far.", "te": "ఐదు వేగమైన చేపలు దూరంగా ఎగిరాయి.", "explanation": "F sound practice."},
    {"en": "Quick queens quietly question quirky questions.", "te": "రాణులు నిశ్శబ్దంగా విచిత్రమైన ప్రశ్నలు అడిగారు.", "explanation": "Q/Qu sounds."},
    {"en": "Three tiny turtles took two taxis.", "te": "మూడు చిన్న తాబేళ్లు రెండు టాక్సీలు ఎక్కాయి.", "explanation": "T sound practice."},
    {"en": "Wild wolves walk while whistling.", "te": "అడవి నక్కలు whistle చేస్తూ నడుస్తాయి.", "explanation": "W sound practice."},
    {"en": "Brisk brave brothers broke brown bread.", "te": "ధైర్యమైన అన్నదమ్ములు బ్రౌన్ బ్రెడ్ విరిచారు.", "explanation": "Br sound practice."},
    {"en": "Silver ships sail silently.", "te": "వెండి నౌకలు నిశ్శబ్దంగా ప్రయాణిస్తాయి.", "explanation": "S/Sh sounds."},
    {"en": "Clean clowns climb cloudy cliffs.", "te": "క్లోన్స్ మబ్బులతో ఉన్న కొండలు ఎక్కారు.", "explanation": "Cl sound practice."},
    {"en": "Many merry monkeys make music.", "te": "చాలా కోతులు సంగీతం చేస్తున్నాయి.", "explanation": "M sound practice."},
    {"en": "Dark dragons drink deep water.", "te": " డ్రాగన్స్ లోతైన నీళ్లు తాగాయి.", "explanation": "D sound practice."},
    {"en": "Tall teachers teach tough topics.", "te": "పొడవైన టీచర్లు కఠినమైన topics బోధిస్తున్నారు.", "explanation": "T sound practice."},
    {"en": "Happy hippos hop heavily.", "te": "సంతోషమైన hippos బరువుగా దూకుతున్నాయి.", "explanation": "H sound practice."},
    {"en": "Good girls giggle gracefully.", "te": "మంచి అమ్మాయిలు నవ్వుతున్నారు.", "explanation": "G sound practice."},
    {"en": "Sharp sharks share shiny shells.", "te": "పదునైన sharks మెరిసే పుటలు పంచుకుంటాయి.", "explanation": "Sh sound practice."},
    {"en": "Tiny tigers tiptoe through tunnels.", "te": "చిన్న పులులు సొరంగాల్లో నడుస్తున్నాయి.", "explanation": "T sound practice."},
    {"en": "Bright blue balloons burst badly.", "te": "నీలి బెలూన్లు పేలిపోయాయి.", "explanation": "B sound practice."},
    {"en": "Funny frogs flip freely.", "te": "వింత కప్పలు స్వేచ్ఛగా దూకుతున్నాయి.", "explanation": "F sound practice."},
    {"en": "Lazy lions lick lemons loudly.", "te": "సోమరి సింహాలు నిమ్మకాయలు నాకుతున్నాయి.", "explanation": "L sound practice."},
    {"en": "Smart students speak slowly sometimes.", "te": "తెలివైన విద్యార్థులు కొన్నిసార్లు నెమ్మదిగా మాట్లాడతారు.", "explanation": "S sound practice."},
    {"en": "Heavy horses hurry home happily.", "te": "గుర్రాలు సంతోషంగా ఇంటికి పరుగెత్తాయి.", "explanation": "H sound practice."},
    {"en": "Big brown bears bake banana bread.", "te": "పెద్ద ఎలుగుబంట్లు banana bread తయారు చేశాయి.", "explanation": "B sound practice."},
    {"en": "Fresh flowers fall from fancy farms.", "te": "తాజా పూలు farms నుండి పడుతున్నాయి.", "explanation": "F sound practice."},
    {"en": "Ten tired teachers talked together.", "te": "పది అలసిపోయిన టీచర్లు కలిసి మాట్లాడారు.", "explanation": "T sound practice."},
    {"en": "Silly snakes sing soft songs.", "te": "వింత పాములు మృదువైన పాటలు పాడుతున్నాయి.", "explanation": "S sound practice."},
    {"en": "Polite pandas play peaceful piano pieces.", "te": "సభ్యమైన pandas piano వాయిస్తున్నారు.", "explanation": "P sound practice."},
    {"en": "Quick kids quietly quit quarrelling.", "te": "చురుకైన పిల్లలు గొడవ ఆపేశారు.", "explanation": "Q/Qu pronunciation clarity improve cheyadaniki use chestaru."}
]

blanks = [
    {"question": "She sells ___ by the seashore.", "correct_answer": "seashells", "telugu_meaning": "ఆమె సముద్ర తీరంలో పుటలు అమ్ముతుంది.", "explanation": "Pronunciation practice.", "options": ["seashells", "sea", "shells", "sales"]},
    {"question": "Peter Piper picked a peck of pickled ___.", "correct_answer": "peppers", "telugu_meaning": "పీటర్ పికిల్ చేసిన మిరపకాయల బుట్ట తీసుకున్నాడు.", "explanation": "P sound.", "options": ["peppers", "paper", "pickles", "peck"]},
    {"question": "Red lorry, yellow ___.", "correct_answer": "lorry", "telugu_meaning": "ఎరుపు లారీ, పసుపు లారీ.", "explanation": "Repeated sounds.", "options": ["lorry", "story", "glory", "berry"]},
    {"question": "How can a clam cram in a clean cream ___?", "correct_answer": "can", "telugu_meaning": "ఒక clam clean cream can లో ఎలా చేరుతుంది?", "explanation": "Repeated sounds.", "options": ["can", "cram", "clam", "clean"]},
    {"question": "I scream, you scream, we all scream for ice ___.", "correct_answer": "cream", "telugu_meaning": "నేను అరుస్తాను, నువ్వు అరుస్తావు, మనమంతా ఐస్క్రీమ్ కోసం అరుస్తాం.", "explanation": "Repeated sounds.", "options": ["cream", "dream", "beam", "scream"]},
    {"question": "A big black bug bit a big black ___.", "correct_answer": "bear", "telugu_meaning": "ఒక పెద్ద నల్ల పురుగు పెద్ద నల్ల ఎలుగుబంటిని కాటేసింది.", "explanation": "B sound.", "options": ["bear", "beer", "bee", "bug"]},
    {"question": "Fresh fried fish, fish fresh ___.", "correct_answer": "fried", "telugu_meaning": "తాజాగా వేయించిన చేప.", "explanation": "F sound.", "options": ["fried", "frieds", "frys", "fying"]},
    {"question": "Six slippery snails slid slowly ___.", "correct_answer": "seaward", "telugu_meaning": "ఆరు జారే నత్తలు నెమ్మదిగా సముద్రం వైపు జారాయి.", "explanation": "S sound.", "options": ["seaward", "seward", "sea", "slowly"]},
    {"question": "Betty bought some butter but the butter was ___.", "correct_answer": "bitter", "telugu_meaning": "బెట్టి వెన్న కొన్నది కానీ అది చేదుగా ఉంది.", "explanation": "B sound.", "options": ["bitter", "better", "butter", "batter"]},
    {"question": "Which witch wished which wicked ___?", "correct_answer": "wish", "telugu_meaning": "ఏ మంత్రగత్తె ఏ కోరిక కోరింది?", "explanation": "W sound.", "options": ["wish", "witch", "wicked", "wished"]}
]

# Generate 20 more blanks
for i in range(10, 30):
    ex = examples[i]
    words = ex['en'].split(' ')
    target = words[-1].replace('.', '').replace('?', '')
    question = ex['en'].replace(target, "___")
    blanks.append({
        "question": question,
        "correct_answer": target,
        "telugu_meaning": ex['te'],
        "explanation": "Tongue twister completion.",
        "options": [target, "sound", "word", "speak"]
    })

speaking_sentences = [
    "She sells seashells by the seashore.", "Peter Piper picked a peck of pickled peppers.",
    "Red lorry, yellow lorry.", "Thirty-three thieves thought throughout Thursday.",
    "How can a clam cram in a clean cream can?", "I scream, you scream, we all scream for ice cream.",
    "Fresh fried fish, fish fresh fried.", "A proper copper coffee pot.",
    "Round and round the rugged rock the ragged rascal ran.", "Which witch wished which wicked wish?",
    "Crazy cats cry cautiously.", "Tiny turtles talk too much.", "Wild wolves walk while whistling.",
    "Happy hippos hop heavily.", "Tall teachers teach tough topics.", "Silver ships sail silently.",
    "Quick queens quietly question quirky questions.", "Blue bluebird blinks.",
    "Busy buzzing bees buzzed busily.", "Funny frogs flip freely.", "Big brown bears bake banana bread.",
    "Smart students speak slowly sometimes.", "Fresh flowers fall from fancy farms.", "Silly snakes sing soft songs.",
    "Heavy horses hurry home happily.", "Dark dragons drink deep water.", "Sharp sharks share shiny shells.",
    "Brisk brave brothers broke brown bread.", "Quick kids quietly quit quarrelling.",
    "Polite pandas play peaceful piano pieces"
]

speaking = []
for i, sent in enumerate(speaking_sentences):
    # Find matching telugu from examples if possible
    te = next((e['te'] for e in examples if e['en'].startswith(sent[:10])), "")
    speaking.append({
        "question": sent,
        "telugu_meaning": te,
        "explanation": "Focus on the repeating sounds and speak clearly."
    })

def update_concept_data():
    concept = Concept.objects.filter(name='Tongue Twisters').first()
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
        print("Tongue Twisters updated successfully.")
    else:
        print("Concept 'Tongue Twisters' not found.")

update_concept_data()
