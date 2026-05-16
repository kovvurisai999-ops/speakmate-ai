import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- WORD STRESS DATA ---
word_stress_content = "Word Stress is the emphasis placed on a specific syllable within a word when speaking. In English, changing the stress can change the meaning of the word (e.g., RE-cord vs re-CORD)."
word_stress_rules = """
- In most two-syllable nouns and adjectives, the first syllable is stressed (e.g., PRE-sent, HAP-py).
- In most two-syllable verbs, the second syllable is stressed (e.g., pre-SENT, de-CIDE).
- Words ending in -ic, -sion, and -tion have stress on the second-to-last syllable (e.g., gra-PHIC, sta-TION).
- Practice listening to native speakers to naturally pick up the stress patterns.
"""

word_stress_examples = [
    {"en": "I need to RE-cord this video.", "te": "నేను ఈ వీడియోని రికార్డ్ చేయాలి.", "explanation": "re-CORD (verb): to store audio/video."},
    {"en": "He set a new RE-cord.", "te": "అతను కొత్త రికార్డు సృష్టించాడు.", "explanation": "RE-cord (noun): a performance level."},
    {"en": "They gave me a PRE-sent.", "te": "వారు నాకు బహుమతి ఇచ్చారు.", "explanation": "PRE-sent (noun): a gift."},
    {"en": "She will pre-SENT the award.", "te": "ఆమె అవార్డును బహుకరిస్తుంది.", "explanation": "pre-SENT (verb): to give or show."},
    {"en": "He is a rebel (RE-bel).", "te": "అతను ఒక తిరుగుబాటుదారుడు.", "explanation": "RE-bel (noun): a person who resists."},
    {"en": "Do not rebel (re-BEL) against the rules.", "te": "నియమాలకు వ్యతిరేకంగా తిరుగుబాటు చేయవద్దు.", "explanation": "re-BEL (verb): to resist."},
    {"en": "What is the ob-JECT of this game?", "te": "ఈ ఆట యొక్క లక్ష్యం ఏమిటి?", "explanation": "OB-ject (noun): a goal or thing."},
    {"en": "I ob-JECT to your decision.", "te": "మీ నిర్ణయాన్ని నేను వ్యతిరేకిస్తున్నాను.", "explanation": "ob-JECT (verb): to oppose."},
    {"en": "I need a per-MIT to park here.", "te": "నేను ఇక్కడ పార్క్ చేయడానికి అనుమతి పత్రం కావాలి.", "explanation": "PER-mit (noun): a document giving permission."},
    {"en": "Please per-MIT me to leave.", "te": "దయచేసి నన్ను వెళ్లడానికి అనుమతించండి.", "explanation": "per-MIT (verb): to allow."}
]
word_stress_examples = (word_stress_examples * 5)[:50]

word_stress_blanks = [
    {"question": "She bought me a birthday ___.", "correct_answer": "present", "telugu_meaning": "ఆమె నాకు పుట్టినరోజు బహుమతి కొన్నది.", "explanation": "Noun: PRE-sent.", "options": ["present", "past", "gift", "future"]},
    {"question": "He will ___ the report today.", "correct_answer": "present", "telugu_meaning": "అతను ఈరోజు నివేదికను సమర్పిస్తాడు.", "explanation": "Verb: pre-SENT.", "options": ["show", "give", "present", "make"]},
    {"question": "He broke the world ___.", "correct_answer": "record", "telugu_meaning": "అతను ప్రపంచ రికార్డును బద్దలు కొట్టాడు.", "explanation": "Noun: RE-cord.", "options": ["book", "record", "glass", "table"]},
    {"question": "Please ___ this song for me.", "correct_answer": "record", "telugu_meaning": "దయచేసి నాకోసం ఈ పాటను రికార్డ్ చేయండి.", "explanation": "Verb: re-CORD.", "options": ["sing", "play", "record", "write"]},
    {"question": "I have an ___ in my eye.", "correct_answer": "object", "telugu_meaning": "నా కంటిలో ఒక వస్తువు పడింది.", "explanation": "Noun: OB-ject.", "options": ["object", "dust", "fly", "tear"]}
]
word_stress_blanks = (word_stress_blanks * 6)[:30]

word_stress_speaking = [
    {"question": "He gave me a PRE-sent.", "telugu_meaning": "అతను నాకు బహుమతి ఇచ్చాడు.", "explanation": "Stress the first syllable (PRE-sent)."},
    {"question": "I will pre-SENT my work.", "telugu_meaning": "నేను నా పనిని సమర్పిస్తాను.", "explanation": "Stress the second syllable (pre-SENT)."},
    {"question": "He broke the RE-cord.", "telugu_meaning": "అతను రికార్డును బద్దలు కొట్టాడు.", "explanation": "Stress the first syllable (RE-cord)."},
    {"question": "Please re-CORD my voice.", "telugu_meaning": "దయచేసి నా గొంతును రికార్డ్ చేయండి.", "explanation": "Stress the second syllable (re-CORD)."},
    {"question": "Do not re-BEL.", "telugu_meaning": "తిరుగుబాటు చేయవద్దు.", "explanation": "Stress the second syllable (re-BEL)."}
]
word_stress_speaking = (word_stress_speaking * 6)[:30]


# --- TONGUE TWISTERS DATA ---
twisters_content = "Tongue Twisters are phrases or sentences that are difficult to articulate rapidly. They are an excellent exercise to improve pronunciation, fluency, and speech clarity."
twisters_rules = """
- Start slowly. Ensure you are pronouncing every sound correctly before speeding up.
- Focus on the difficult sounds (e.g., 's' vs 'sh', 'p' vs 'b').
- Repeat the twister several times in a row.
- Have fun with it! Making mistakes is part of the learning process.
"""

twisters_examples = [
    {"en": "She sells seashells by the seashore.", "te": "ఆమె సముద్ర తీరంలో సముద్రపు గవ్వలను విక్రయిస్తుంది.", "explanation": "Practices 's' and 'sh' sounds."},
    {"en": "Peter Piper picked a peck of pickled peppers.", "te": "పీటర్ పైపర్ ఒక పెక్ (కొలత) ఊరగాయ మిరియాలు తీసుకున్నాడు.", "explanation": "Practices the 'p' sound."},
    {"en": "I scream, you scream, we all scream for ice cream.", "te": "నేను అరుస్తాను, నువ్వు అరుస్తావు, మనమంతా ఐస్ క్రీమ్ కోసం అరుస్తాము.", "explanation": "Practices long 'e' and 'sc' sounds."},
    {"en": "How much wood would a woodchuck chuck if a woodchuck could chuck wood?", "te": "ఒక వడ్రంగి పిట్ట కలపను కొట్టగలిగితే ఎంత కలపను కొడుతుంది?", "explanation": "Practices 'w' and 'ch' sounds."},
    {"en": "Betty Botter bought some butter.", "te": "బెట్టీ బాటర్ కొంచెం వెన్న కొన్నది.", "explanation": "Practices 'b' and 't' sounds."},
    {"en": "Fuzzy Wuzzy was a bear. Fuzzy Wuzzy had no hair.", "te": "ఫజ్జీ వజ్జీ ఒక ఎలుగుబంటి. ఫజ్జీ వజ్జీకి జుట్టు లేదు.", "explanation": "Practices 'f', 'z', and 'w' sounds."},
    {"en": "A big black bug bit a big black bear.", "te": "ఒక పెద్ద నల్లటి పురుగు ఒక పెద్ద నల్లటి ఎలుగుబంటిని కుట్టింది.", "explanation": "Practices the 'b' sound."},
    {"en": "Red lorry, yellow lorry.", "te": "ఎరుపు లారీ, పసుపు లారీ.", "explanation": "Practices 'r' and 'l' sounds (often tricky)."},
    {"en": "Six slippery snails slid slowly seaward.", "te": "ఆరు జారే నత్తలు నెమ్మదిగా సముద్రం వైపు జారాయి.", "explanation": "Practices 's' and 'sl' sounds."},
    {"en": "The thirty-three thieves thought that they thrilled the throne throughout Thursday.", "te": "ముప్పై ముగ్గురు దొంగలు గురువారం అంతటా సింహాసనాన్ని ఉర్రూతలూగించామని భావించారు.", "explanation": "Practices the 'th' sound."}
]
twisters_examples = (twisters_examples * 5)[:50]

twisters_blanks = [
    {"question": "She sells ___ by the seashore.", "correct_answer": "seashells", "telugu_meaning": "ఆమె సముద్ర తీరంలో సముద్రపు గవ్వలను విక్రయిస్తుంది.", "explanation": "Famous 's'/'sh' twister.", "options": ["shells", "seashells", "shoes", "shirts"]},
    {"question": "Peter Piper picked a peck of pickled ___.", "correct_answer": "peppers", "telugu_meaning": "పీటర్ పైపర్ ఒక పెక్ ఊరగాయ మిరియాలు తీసుకున్నాడు.", "explanation": "Famous 'p' twister.", "options": ["apples", "peppers", "plums", "peaches"]},
    {"question": "I scream, you scream, we all scream for ice ___.", "correct_answer": "cream", "telugu_meaning": "మనమంతా ఐస్ క్రీమ్ కోసం అరుస్తాము.", "explanation": "Rhyming twister.", "options": ["cream", "dream", "team", "beam"]},
    {"question": "A big black ___ bit a big black bear.", "correct_answer": "bug", "telugu_meaning": "ఒక పెద్ద నల్లటి పురుగు ఒక పెద్ద నల్లటి ఎలుగుబంటిని కుట్టింది.", "explanation": "'b' sound twister.", "options": ["dog", "cat", "bug", "bird"]},
    {"question": "Red ___, yellow lorry.", "correct_answer": "lorry", "telugu_meaning": "ఎరుపు లారీ, పసుపు లారీ.", "explanation": "'r' and 'l' sound twister.", "options": ["car", "bus", "lorry", "van"]}
]
twisters_blanks = (twisters_blanks * 6)[:30]

twisters_speaking = [
    {"question": "She sells seashells by the seashore.", "telugu_meaning": "ఆమె సముద్ర తీరంలో గవ్వలు అమ్ముతుంది.", "explanation": "Differentiate clearly between 's' and 'sh'."},
    {"question": "Peter Piper picked a peck of pickled peppers.", "telugu_meaning": "పీటర్ పైపర్ మిరియాలు తీసుకున్నాడు.", "explanation": "Pop the 'p' sound clearly."},
    {"question": "I scream, you scream, we all scream for ice cream.", "telugu_meaning": "మనమంతా ఐస్ క్రీమ్ కోసం అరుస్తాము.", "explanation": "Link the words smoothly."},
    {"question": "Red lorry, yellow lorry.", "telugu_meaning": "ఎరుపు లారీ, పసుపు లారీ.", "explanation": "Make the 'r' and 'l' sounds distinct."},
    {"question": "A big black bug bit a big black bear.", "telugu_meaning": "నల్లటి పురుగు నల్లటి ఎలుగుబంటిని కుట్టింది.", "explanation": "Focus on the 'b' sound."}
]
twisters_speaking = (twisters_speaking * 6)[:30]


# --- DIFFICULT WORDS DATA ---
diff_words_content = "Difficult Words in English are those that are often mispronounced or misspelled due to irregular rules, silent letters, or unusual origins. Mastering them greatly improves your confidence."
diff_words_rules = """
- Break long words into smaller syllables (e.g., com-fort-a-ble).
- Listen to the audio pronunciation in a dictionary.
- Create mnemonic devices (memory tricks) for spelling.
- Practice using these words in your daily sentences.
"""

diff_words_examples = [
    {"en": "She sat in a comfortable chair.", "te": "ఆమె సౌకర్యవంతమైన కుర్చీలో కూర్చుంది.", "explanation": "Pronounced 'comf-tuh-bul', not 'com-fort-a-ble'."},
    {"en": "He bought a new vehicle.", "te": "అతను కొత్త వాహనం కొన్నాడు.", "explanation": "Pronounced 'vee-uh-kul', the 'h' is silent."},
    {"en": "I eat vegetables every day.", "te": "నేను ప్రతిరోజూ కూరగాయలు తింటాను.", "explanation": "Pronounced 'vej-tuh-buls', not 've-ge-ta-bles'."},
    {"en": "Can I have a receipt, please?", "te": "దయచేసి నాకు రసీదు ఇవ్వగలరా?", "explanation": "Pronounced 're-seet', the 'p' is silent."},
    {"en": "The choir sang beautifully.", "te": "గాయక బృందం అద్భుతంగా పాడింది.", "explanation": "Pronounced 'kwire', not 'cho-ir'."},
    {"en": "He went to the restaurant.", "te": "అతను రెస్టారెంట్‌కు వెళ్ళాడు.", "explanation": "Pronounced 'res-trunt' or 'res-tuh-ront'."},
    {"en": "We had a lot of chaos today.", "te": "ఈరోజు మాకు చాలా గందరగోళం జరిగింది.", "explanation": "Pronounced 'kay-os', 'ch' makes a 'k' sound."},
    {"en": "Wednesday is the middle of the week.", "te": "బుధవారం వారం మధ్యలో ఉంటుంది.", "explanation": "Pronounced 'wenz-day', the first 'd' is silent."},
    {"en": "I love the subtle flavor.", "te": "నాకు ఆ సూక్ష్మమైన రుచి ఇష్టం.", "explanation": "Pronounced 'suh-tul', the 'b' is silent."},
    {"en": "The schedule has changed.", "te": "షెడ్యూల్ మారింది.", "explanation": "Pronounced 'sked-jool' (US) or 'shed-yool' (UK)."}
]
diff_words_examples = (diff_words_examples * 5)[:50]

diff_words_blanks = [
    {"question": "I need a ___ chair to sit on.", "correct_answer": "comfortable", "telugu_meaning": "నాకు కూర్చోవడానికి సౌకర్యవంతమైన కుర్చీ కావాలి.", "explanation": "Often mispronounced word.", "options": ["hard", "comfortable", "tall", "short"]},
    {"question": "Please give me the bill or ___.", "correct_answer": "receipt", "telugu_meaning": "దయచేసి నాకు బిల్లు లేదా రసీదు ఇవ్వండి.", "explanation": "Silent 'p'.", "options": ["receit", "receipt", "recipt", "paper"]},
    {"question": "Car is a type of ___.", "correct_answer": "vehicle", "telugu_meaning": "కారు ఒక రకమైన వాహనం.", "explanation": "Silent 'h'.", "options": ["vehicel", "veicle", "vehicle", "toy"]},
    {"question": "Carrots are healthy ___.", "correct_answer": "vegetables", "telugu_meaning": "క్యారెట్లు ఆరోగ్యకరమైన కూరగాయలు.", "explanation": "Syllable dropping word.", "options": ["fruits", "vegetables", "meats", "sweets"]},
    {"question": "Today is Tuesday, tomorrow is ___.", "correct_answer": "Wednesday", "telugu_meaning": "ఈరోజు మంగళవారం, రేపు బుధవారం.", "explanation": "Silent 'd'.", "options": ["Wednesday", "Wensday", "Thursday", "Friday"]}
]
diff_words_blanks = (diff_words_blanks * 6)[:30]

diff_words_speaking = [
    {"question": "This chair is comfortable.", "telugu_meaning": "ఈ కుర్చీ సౌకర్యవంతంగా ఉంది.", "explanation": "Say 'comf-tuh-bul'."},
    {"question": "Can I have the receipt?", "telugu_meaning": "నాకు రసీదు ఇవ్వగలరా?", "explanation": "Say 're-seet'."},
    {"question": "Eat your vegetables.", "telugu_meaning": "మీ కూరగాయలు తినండి.", "explanation": "Say 'vej-tuh-buls'."},
    {"question": "It caused a lot of chaos.", "telugu_meaning": "ఇది చాలా గందరగోళానికి కారణమైంది.", "explanation": "Say 'kay-os'."},
    {"question": "I will see you on Wednesday.", "telugu_meaning": "నేను నిన్ను బుధవారం కలుస్తాను.", "explanation": "Say 'wenz-day'."}
]
diff_words_speaking = (diff_words_speaking * 6)[:30]

def insert_data(concept_name, content, rules, examples, blanks, speaking):
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

insert_data('Word Stress', word_stress_content, word_stress_rules, word_stress_examples, word_stress_blanks, word_stress_speaking)
insert_data('Tongue Twisters', twisters_content, twisters_rules, twisters_examples, twisters_blanks, twisters_speaking)
insert_data('Difficult Words', diff_words_content, diff_words_rules, diff_words_examples, diff_words_blanks, diff_words_speaking)
