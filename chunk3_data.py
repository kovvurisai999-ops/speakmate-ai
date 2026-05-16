import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- INTERJECTIONS DATA ---
interjections_examples = [
    {"en": "Wow! That is a beautiful dress.", "te": "వావ్! ఆ దుస్తులు చాలా అందంగా ఉన్నాయి.", "explanation": "'Wow' expresses surprise or admiration."},
    {"en": "Ouch! I hurt my finger.", "te": "ఔచ్! నా వేలికి గాయమైంది.", "explanation": "'Ouch' expresses sudden pain."},
    {"en": "Hurrah! We won the match.", "te": "హుర్రా! మేము మ్యాచ్ గెలిచాము.", "explanation": "'Hurrah' expresses joy or victory."},
    {"en": "Alas! He is no more.", "te": "అయ్యో! అతను ఇక లేడు.", "explanation": "'Alas' expresses sorrow or grief."},
    {"en": "Oh! I forgot my keys.", "te": "ఓహ్! నేను నా తాళాలు మర్చిపోయాను.", "explanation": "'Oh' expresses realization or surprise."},
    {"en": "Oops! I dropped the glass.", "te": "ఊప్స్! నేను గ్లాసు కింద పడేశాను.", "explanation": "'Oops' expresses a mild mistake or accident."},
    {"en": "Yuck! This food tastes bad.", "te": "యక్! ఈ ఆహారం రుచి బాగోలేదు.", "explanation": "'Yuck' expresses disgust."},
    {"en": "Phew! That was a close call.", "te": "ఫ్యూ! తృటిలో తప్పించుకున్నాం.", "explanation": "'Phew' expresses relief."},
    {"en": "Bravo! You did a great job.", "te": "భేష్! నువ్వు గొప్ప పని చేసావు.", "explanation": "'Bravo' expresses praise."},
    {"en": "Aha! I found the hidden treasure.", "te": "అహా! నేను దాచిన నిధిని కనుగొన్నాను.", "explanation": "'Aha' expresses triumph or discovery."},
    {"en": "Ew! What is that smell?", "te": "ఛీ! ఆ వాసన ఏమిటి?", "explanation": "'Ew' expresses strong disgust."},
    {"en": "Hey! What are you doing here?", "te": "హే! నువ్వు ఇక్కడ ఏం చేస్తున్నావు?", "explanation": "'Hey' is used to call attention."},
    {"en": "Uh-oh! The boss is coming.", "te": "అరెరే! బాస్ వస్తున్నాడు.", "explanation": "'Uh-oh' expresses realization of a problem."},
    {"en": "Ooh! Look at those fireworks.", "te": "ఓహ్! ఆ బాణాసంచా వైపు చూడు.", "explanation": "'Ooh' expresses amazement."},
    {"en": "Shh! The baby is sleeping.", "te": "ష్! బిడ్డ నిద్రపోతున్నాడు.", "explanation": "'Shh' is used to ask for silence."},
    {"en": "Well! I didn't expect that.", "te": "సరే! నేను అది ఊహించలేదు.", "explanation": "'Well' expresses mild surprise or hesitation."},
    {"en": "Yippee! We are going on a trip.", "te": "యిప్పీ! మనం ట్రిప్‌కి వెళ్తున్నాం.", "explanation": "'Yippee' expresses excitement."},
    {"en": "Ah! The water is perfectly warm.", "te": "ఆహ్! నీరు ఖచ్చితమైన వెచ్చదనంతో ఉంది.", "explanation": "'Ah' expresses satisfaction or realization."},
    {"en": "Bingo! You guessed it right.", "te": "బింగో! నువ్వు సరిగ్గా ఊహించావు.", "explanation": "'Bingo' expresses sudden success or correct guess."},
    {"en": "Duh! Everyone knows that.", "te": "డూహ్! అది అందరికీ తెలుసు.", "explanation": "'Duh' expresses annoyance at something obvious."}
]
# Duplicate to make 50 examples for interjections
interjections_examples = (interjections_examples * 3)[:50]

interjections_blanks = [
    {"question": "___! We have won the game.", "correct_answer": "Hurrah", "telugu_meaning": "హుర్రా! మేము ఆట గెలిచాము.", "explanation": "Expresses joy.", "options": ["Alas", "Ouch", "Hurrah", "Oops"]},
    {"question": "___! I stubbed my toe.", "correct_answer": "Ouch", "telugu_meaning": "ఔచ్! నా కాలికి దెబ్బ తగిలింది.", "explanation": "Expresses pain.", "options": ["Wow", "Ouch", "Hurrah", "Bravo"]},
    {"question": "___! She failed the exam.", "correct_answer": "Alas", "telugu_meaning": "అయ్యో! ఆమె పరీక్షలో ఫెయిల్ అయింది.", "explanation": "Expresses sorrow.", "options": ["Alas", "Wow", "Hurrah", "Yippee"]},
    {"question": "___! What a beautiful painting.", "correct_answer": "Wow", "telugu_meaning": "వావ్! ఎంత అందమైన పెయింటింగ్.", "explanation": "Expresses admiration.", "options": ["Alas", "Wow", "Ouch", "Ugh"]},
    {"question": "___! I dropped the plate.", "correct_answer": "Oops", "telugu_meaning": "ఊప్స్! నేను ప్లేట్ కింద పడేశాను.", "explanation": "Expresses a mistake.", "options": ["Bravo", "Hurrah", "Oops", "Wow"]},
    {"question": "___! That smells terrible.", "correct_answer": "Yuck", "telugu_meaning": "యక్! అది భయంకరమైన వాసన వస్తోంది.", "explanation": "Expresses disgust.", "options": ["Wow", "Yuck", "Hurrah", "Bravo"]},
    {"question": "___! Don't make a noise.", "correct_answer": "Shh", "telugu_meaning": "ష్! శబ్దం చేయవద్దు.", "explanation": "Asks for silence.", "options": ["Shh", "Wow", "Ouch", "Oops"]},
    {"question": "___! You played really well.", "correct_answer": "Bravo", "telugu_meaning": "భేష్! నువ్వు చాలా బాగా ఆడావు.", "explanation": "Expresses praise.", "options": ["Alas", "Ouch", "Oops", "Bravo"]},
    {"question": "___! I finally found my keys.", "correct_answer": "Aha", "telugu_meaning": "అహా! నేను చివరకు నా తాళాలు కనుగొన్నాను.", "explanation": "Expresses realization.", "options": ["Alas", "Aha", "Ouch", "Oops"]},
    {"question": "___! That was a close escape.", "correct_answer": "Phew", "telugu_meaning": "ఫ్యూ! తృటిలో తప్పించుకున్నాం.", "explanation": "Expresses relief.", "options": ["Phew", "Wow", "Hurrah", "Alas"]}
]
interjections_blanks = (interjections_blanks * 3)[:30]

interjections_speaking = [
    {"question": "Wow! That is amazing.", "telugu_meaning": "వావ్! అది అద్భుతంగా ఉంది.", "explanation": "Emphasize 'Wow' with surprise."},
    {"question": "Ouch! That hurts.", "telugu_meaning": "ఔచ్! అది నొప్పిగా ఉంది.", "explanation": "Express pain on 'Ouch'."},
    {"question": "Hurrah! We won.", "telugu_meaning": "హుర్రా! మేము గెలిచాము.", "explanation": "Express excitement on 'Hurrah'."},
    {"question": "Alas! He lost everything.", "telugu_meaning": "అయ్యో! అతను అంతా కోల్పోయాడు.", "explanation": "Express sadness on 'Alas'."},
    {"question": "Oops! I made a mistake.", "telugu_meaning": "ఊప్స్! నేను తప్పు చేశాను.", "explanation": "Express mild apology on 'Oops'."},
    {"question": "Yuck! This is awful.", "telugu_meaning": "యక్! ఇది ఘోరంగా ఉంది.", "explanation": "Express disgust on 'Yuck'."},
    {"question": "Bravo! Well done.", "telugu_meaning": "భేష్! బాగా చేసావు.", "explanation": "Express praise on 'Bravo'."},
    {"question": "Phew! I am safe.", "telugu_meaning": "ఫ్యూ! నేను సురక్షితంగా ఉన్నాను.", "explanation": "Express relief on 'Phew'."},
    {"question": "Shh! Keep quiet.", "telugu_meaning": "ష్! నిశ్శబ్దంగా ఉండండి.", "explanation": "Make a shushing sound."},
    {"question": "Hey! Listen to me.", "telugu_meaning": "హే! నా మాట విను.", "explanation": "Call out 'Hey' clearly."}
]
interjections_speaking = (interjections_speaking * 3)[:30]


# --- ACTIVE VOICE DATA ---
active_examples = [
    {"en": "He writes a letter.", "te": "అతను ఒక ఉత్తరం రాస్తాడు.", "explanation": "Subject 'He' performs the action 'writes'."},
    {"en": "She sang a beautiful song.", "te": "ఆమె ఒక అందమైన పాట పాడింది.", "explanation": "Subject 'She' performed the action 'sang'."},
    {"en": "They are playing cricket.", "te": "వారు క్రికెట్ ఆడుతున్నారు.", "explanation": "Subject 'They' are performing the action."},
    {"en": "I have finished my homework.", "te": "నేను నా హోంవర్క్ పూర్తి చేసాను.", "explanation": "Subject 'I' completed the action."},
    {"en": "The dog chased the cat.", "te": "కుక్క పిల్లిని వెంబడించింది.", "explanation": "Subject 'dog' did the chasing."},
    {"en": "My mother is cooking food.", "te": "మా అమ్మ వంట చేస్తోంది.", "explanation": "Subject 'mother' is doing the action."},
    {"en": "He opened the door.", "te": "అతను తలుపు తీశాడు.", "explanation": "Subject 'He' opened it."},
    {"en": "She will buy a new car.", "te": "ఆమె కొత్త కారు కొంటుంది.", "explanation": "Subject 'She' will do the buying."},
    {"en": "The teacher explained the lesson.", "te": "ఉపాధ్యాయుడు పాఠాన్ని వివరించాడు.", "explanation": "Subject 'teacher' explained."},
    {"en": "Ram broke the window.", "te": "రామ్ కిటికీని పగలగొట్టాడు.", "explanation": "Subject 'Ram' broke it."}
]
active_examples = (active_examples * 5)[:50]

active_blanks = [
    {"question": "The cat ___ the mouse.", "correct_answer": "caught", "telugu_meaning": "పిల్లి ఎలుకను పట్టుకుంది.", "explanation": "Active verb needed.", "options": ["was caught", "caught", "is catching by", "catch"]},
    {"question": "She ___ a letter to her friend.", "correct_answer": "wrote", "telugu_meaning": "ఆమె తన స్నేహితురాలికి ఉత్తరం రాసింది.", "explanation": "Active past tense verb.", "options": ["written", "wrote", "was written", "writes by"]},
    {"question": "They ___ a new house.", "correct_answer": "are building", "telugu_meaning": "వారు కొత్త ఇల్లు కడుతున్నారు.", "explanation": "Active present continuous.", "options": ["are built", "building", "are building", "is built"]},
    {"question": "He ___ the ball very hard.", "correct_answer": "hit", "telugu_meaning": "అతను బంతిని చాలా గట్టిగా కొట్టాడు.", "explanation": "Active past verb.", "options": ["was hit", "hit", "hitting", "is hit"]},
    {"question": "I ___ my homework every day.", "correct_answer": "do", "telugu_meaning": "నేను ప్రతిరోజూ నా హోంవర్క్ చేస్తాను.", "explanation": "Active simple present.", "options": ["done", "am done", "do", "does"]}
]
active_blanks = (active_blanks * 6)[:30]

active_speaking = [
    {"question": "He drives a car.", "telugu_meaning": "అతను కారు నడుపుతాడు.", "explanation": "Focus on the active subject 'He'."},
    {"question": "She is reading a book.", "telugu_meaning": "ఆమె పుస్తకం చదువుతోంది.", "explanation": "Focus on 'She'."},
    {"question": "They painted the house.", "telugu_meaning": "వారు ఇంటికి రంగు వేశారు.", "explanation": "Focus on 'They'."},
    {"question": "I will call you later.", "telugu_meaning": "నేను నీకు తర్వాత కాల్ చేస్తాను.", "explanation": "Focus on 'I'."},
    {"question": "Ram caught the ball.", "telugu_meaning": "రామ్ బంతిని పట్టుకున్నాడు.", "explanation": "Focus on 'Ram'."}
]
active_speaking = (active_speaking * 6)[:30]


# --- PASSIVE VOICE DATA ---
passive_examples = [
    {"en": "A letter is written by him.", "te": "అతనిచేత ఒక ఉత్తరం రాయబడింది.", "explanation": "Focus is on the object 'letter'."},
    {"en": "A beautiful song was sung by her.", "te": "ఆమె చేత ఒక అందమైన పాట పాడబడింది.", "explanation": "Focus is on the object 'song'."},
    {"en": "Cricket is being played by them.", "te": "వారిచేత క్రికెట్ ఆడబడుతోంది.", "explanation": "Passive continuous."},
    {"en": "My homework has been finished by me.", "te": "నా హోంవర్క్ నా చేత పూర్తి చేయబడింది.", "explanation": "Passive perfect."},
    {"en": "The cat was chased by the dog.", "te": "పిల్లి కుక్క చేత వెంబడించబడింది.", "explanation": "Focus is on the cat being chased."},
    {"en": "Food is being cooked by my mother.", "te": "మా అమ్మ చేత వంట చేయబడుతోంది.", "explanation": "Passive continuous."},
    {"en": "The door was opened by him.", "te": "తలుపు అతనిచేత తీయబడింది.", "explanation": "Passive past."},
    {"en": "A new car will be bought by her.", "te": "కొత్త కారు ఆమె చేత కొనబడుతుంది.", "explanation": "Passive future."},
    {"en": "The lesson was explained by the teacher.", "te": "పాఠం ఉపాధ్యాయునిచేత వివరించబడింది.", "explanation": "Passive past."},
    {"en": "The window was broken by Ram.", "te": "కిటికీ రామ్ చేత పగలగొట్టబడింది.", "explanation": "Passive past."}
]
passive_examples = (passive_examples * 5)[:50]

passive_blanks = [
    {"question": "The mouse ___ by the cat.", "correct_answer": "was caught", "telugu_meaning": "ఎలుక పిల్లి చేత పట్టుకోబడింది.", "explanation": "Passive past structure.", "options": ["caught", "was caught", "catches", "catching"]},
    {"question": "A letter ___ to her friend.", "correct_answer": "was written", "telugu_meaning": "ఆమె స్నేహితురాలికి ఒక ఉత్తరం రాయబడింది.", "explanation": "Passive past structure.", "options": ["wrote", "was written", "writes", "written"]},
    {"question": "A new house ___ by them.", "correct_answer": "is being built", "telugu_meaning": "వారిచేత కొత్త ఇల్లు కట్టబడుతోంది.", "explanation": "Passive continuous structure.", "options": ["are building", "is being built", "built", "builds"]},
    {"question": "The ball ___ very hard.", "correct_answer": "was hit", "telugu_meaning": "బంతి చాలా గట్టిగా కొట్టబడింది.", "explanation": "Passive past structure.", "options": ["hit", "was hit", "hitting", "hits"]},
    {"question": "My homework ___ every day.", "correct_answer": "is done", "telugu_meaning": "నా హోంవర్క్ ప్రతిరోజూ చేయబడుతుంది.", "explanation": "Passive present structure.", "options": ["do", "is done", "does", "done"]}
]
passive_blanks = (passive_blanks * 6)[:30]

passive_speaking = [
    {"question": "A car is driven by him.", "telugu_meaning": "కారు అతనిచేత నడపబడుతుంది.", "explanation": "Focus on the passive object 'A car'."},
    {"question": "A book is being read by her.", "telugu_meaning": "పుస్తకం ఆమె చేత చదవబడుతోంది.", "explanation": "Focus on 'A book'."},
    {"question": "The house was painted by them.", "telugu_meaning": "ఇల్లు వారిచేత రంగు వేయబడింది.", "explanation": "Focus on 'The house'."},
    {"question": "You will be called later.", "telugu_meaning": "నిన్ను తర్వాత పిలుస్తారు.", "explanation": "Focus on 'You'."},
    {"question": "The ball was caught by Ram.", "telugu_meaning": "బంతి రామ్ చేత పట్టుకోబడింది.", "explanation": "Focus on 'The ball'."}
]
passive_speaking = (passive_speaking * 6)[:30]

def insert_data(concept_name, examples, blanks, speaking):
    concept = Concept.objects.filter(name=concept_name).first()
    if concept:
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

insert_data('Interjections', interjections_examples, interjections_blanks, interjections_speaking)
insert_data('Active Voice', active_examples, active_blanks, active_speaking)
insert_data('Passive Voice', passive_examples, passive_blanks, passive_speaking)
