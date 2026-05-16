import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- QUESTION TAGS DATA ---
content = "Question Tags are short questions added at the end of a sentence. They are used to confirm information, continue conversation, ask politely, or check if something is true."
rules = """
- Positive sentence -> Negative tag
- Negative sentence -> Positive tag
- Helping verb repeat avvali
- Pronoun use cheyali
- Formula: Statement + "," + Question Tag + "?"
"""

examples = [
    {"en": "You are learning English, aren't you?", "te": "నువ్వు ఇంగ్లీష్ నేర్చుకుంటున్నావు, కదా?", "explanation": "Positive statement kabatti negative tag 'aren't you' use chesam."},
    {"en": "She can speak fluently, can't she?", "te": "ఆమె fluently మాట్లాడగలదు, కదా?", "explanation": "'can' modal ki opposite tag 'can't' use chesam."},
    {"en": "He is your friend, isn't he?", "te": "అతను నీ ఫ్రెండ్, కదా?", "explanation": "Positive sentence ki negative tag add chesam."},
    {"en": "They will attend the class, won't they?", "te": "వాళ్లు క్లాస్ attend అవుతారు, కదా?", "explanation": "Future helping verb 'will' ki 'won't' tag use chesam."},
    {"en": "You like coffee, don't you?", "te": "నీకు కాఫీ ఇష్టం, కదా?", "explanation": "Simple present positive sentence kabatti 'don't you' use chesam."},
    {"en": "She isn't busy today, is she?", "te": "ఆమె ఈరోజు busy గా లేదు, కదా?", "explanation": "Negative statement needs positive tag."},
    {"en": "We should practice daily, shouldn't we?", "te": "మనం ప్రతిరోజూ practice చేయాలి, కదా?", "explanation": "Should -> shouldn't."},
    {"en": "He plays cricket well, doesn't he?", "te": "అతను బాగా క్రికెట్ ఆడతాడు, కదా?", "explanation": "Plays -> doesn't."},
    {"en": "You completed the project, didn't you?", "te": "నువ్వు ప్రాజెక్ట్ పూర్తి చేశావు, కదా?", "explanation": "Completed -> didn't."},
    {"en": "The train arrived on time, didn't it?", "te": "ట్రైన్ సమయానికి వచ్చింది, కదా?", "explanation": "Arrived -> didn't."},
    {"en": "She will call you later, won't she?", "te": "ఆమె తర్వాత నీకు కాల్ చేస్తుంది, కదా?", "explanation": "Will -> won't."},
    {"en": "You can drive a car, can't you?", "te": "నువ్వు కారు నడపగలవు, కదా?", "explanation": "Can -> can't."},
    {"en": "They are coming today, aren't they?", "te": "వాళ్లు ఈరోజు వస్తున్నారు, కదా?", "explanation": "Are -> aren't."},
    {"en": "He doesn't eat junk food, does he?", "te": "అతను junk food తినడు, కదా?", "explanation": "Negative -> positive."},
    {"en": "We have finished the work, haven't we?", "te": "మనం పని పూర్తి చేశాం, కదా?", "explanation": "Have -> haven't."},
    {"en": "She sings beautifully, doesn't she?", "te": "ఆమె అందంగా పాటలు పాడుతుంది, కదా?", "explanation": "Sings -> doesn't."},
    {"en": "You aren't tired, are you?", "te": "నువ్వు అలసిపోలేదు, కదా?", "explanation": "Aren't -> are."},
    {"en": "He can repair computers, can't he?", "te": "అతను కంప్యూటర్లు repair చేయగలడు, కదా?", "explanation": "Can -> can't."},
    {"en": "The manager approved the application, didn't he?", "te": "మేనేజర్ application approve చేశారు, కదా?", "explanation": "Approved -> didn't."},
    {"en": "Students should follow discipline, shouldn't they?", "te": "విద్యార్థులు discipline పాటించాలి, కదా?", "explanation": "Should -> shouldn't."},
    {"en": "Your brother works in Hyderabad, doesn't he?", "te": "నీ అన్న హైదరాబాద్లో పని చేస్తాడు, కదా?", "explanation": "Works -> doesn't."},
    {"en": "The movie was interesting, wasn't it?", "te": "సినిమా ఆసక్తికరంగా ఉంది, కదా?", "explanation": "Was -> wasn't."},
    {"en": "She studied well, didn't she?", "te": "ఆమె బాగా చదివింది, కదా?", "explanation": "Studied -> didn't."},
    {"en": "You won't forget this lesson, will you?", "te": "నువ్వు ఈ పాఠం మర్చిపోవు, కదా?", "explanation": "Won't -> will."},
    {"en": "He is preparing for interviews, isn't he?", "te": "అతను interviews కి సిద్ధమవుతున్నాడు, కదా?", "explanation": "Is -> isn't."},
    {"en": "The students submitted assignments, didn't they?", "te": "విద్యార్థులు assignments submit చేశారు, కదా?", "explanation": "Submitted -> didn't."},
    {"en": "She has a laptop, doesn't she?", "te": "ఆమె వద్ద laptop ఉంది, కదా?", "explanation": "Has -> doesn't."},
    {"en": "We are late, aren't we?", "te": "మనం ఆలస్యంగా ఉన్నాం, కదా?", "explanation": "Are -> aren't."},
    {"en": "He wasn't present yesterday, was he?", "te": "అతను నిన్న హాజరు కాలేదు, కదా?", "explanation": "Wasn't -> was."},
    {"en": "You enjoy speaking English, don't you?", "te": "నువ్వు ఇంగ్లీష్ మాట్లాడటం enjoy చేస్తావు, కదా?", "explanation": "Enjoy -> don't."},
    {"en": "She will join the company, won't she?", "te": "ఆమె కంపెనీలో join అవుతుంది, కదా?", "explanation": "Will -> won't."},
    {"en": "The child likes chocolates, doesn't he?", "te": "పిల్లాడికి chocolates ఇష్టం, కదా?", "explanation": "Likes -> doesn't."},
    {"en": "You are from Andhra Pradesh, aren't you?", "te": "నువ్వు ఆంధ్రప్రదేశ్ నుండి వచ్చావు, కదా?", "explanation": "Are -> aren't."},
    {"en": "She didn't attend the meeting, did she?", "te": "ఆమె meeting attend కాలేదు, కదా?", "explanation": "Didn't -> did."},
    {"en": "They can understand Telugu, can't they?", "te": "వాళ్లు తెలుగు అర్థం చేసుకోగలరు, కదా?", "explanation": "Can -> can't."},
    {"en": "We must complete the work, mustn't we?", "te": "మనం పని తప్పకుండా పూర్తి చేయాలి, కదా?", "explanation": "Must -> mustn't."},
    {"en": "The bus stopped here, didn't it?", "te": "బస్ ఇక్కడ ఆగింది, కదా?", "explanation": "Stopped -> didn't."},
    {"en": "You have seen this movie, haven't you?", "te": "నువ్వు ఈ సినిమా చూశావు, కదా?", "explanation": "Have -> haven't."},
    {"en": "He should improve his communication skills, shouldn't he?", "te": "అతను communication skills మెరుగుపరచాలి, కదా?", "explanation": "Should -> shouldn't."},
    {"en": "She can sing well, can't she?", "te": "ఆమె బాగా పాట పాడగలదు, కదా?", "explanation": "Can -> can't."},
    {"en": "The employees finished the task, didn't they?", "te": "ఉద్యోగులు పని పూర్తి చేశారు, కదా?", "explanation": "Finished -> didn't."},
    {"en": "You shouldn't waste time, should you?", "te": "నువ్వు సమయం వృథా చేయకూడదు, కదా?", "explanation": "Shouldn't -> should."},
    {"en": "He likes coding, doesn't he?", "te": "అతనికి coding ఇష్టం, కదా?", "explanation": "Likes -> doesn't."},
    {"en": "They are your classmates, aren't they?", "te": "వాళ్లు నీ classmates, కదా?", "explanation": "Are -> aren't."},
    {"en": "She wasn't upset, was she?", "te": "ఆమె upset కాలేదు, కదా?", "explanation": "Wasn't -> was."},
    {"en": "We can start now, can't we?", "te": "మనం ఇప్పుడు ప్రారంభించవచ్చు, కదా?", "explanation": "Can -> can't."},
    {"en": "The teacher explained clearly, didn't she?", "te": "టీచర్ స్పష్టంగా explain చేశారు, కదా?", "explanation": "Explained -> didn't."},
    {"en": "You don't like tea, do you?", "te": "నీకు టీ ఇష్టం లేదు, కదా?", "explanation": "Don't -> do."},
    {"en": "He will become successful, won't he?", "te": "అతను విజయవంతం అవుతాడు, కదా?", "explanation": "Will -> won't."},
    {"en": "We are improving our English, aren't we?", "te": "మనం మన ఇంగ్లీష్ మెరుగుపరుచుకుంటున్నాం, కదా?", "explanation": "Are -> aren't."}
]

blanks = [
    {"question": "You are learning English, ___ you?", "correct_answer": "aren't", "telugu_meaning": "నువ్వు ఇంగ్లీష్ నేర్చుకుంటున్నావు, కదా?", "explanation": "Positive 'are' needs 'aren't' tag.", "options": ["aren't", "are", "don't", "isn't"]},
    {"question": "She can speak fluently, ___ she?", "correct_answer": "can't", "telugu_meaning": "ఆమె fluently మాట్లాడగలదు, కదా?", "explanation": "'can' needs 'can't' tag.", "options": ["can't", "can", "couldn't", "won't"]},
    {"question": "He is your friend, ___ he?", "correct_answer": "isn't", "telugu_meaning": "అతను నీ ఫ్రెండ్, కదా?", "explanation": "Positive 'is' needs 'isn't' tag.", "options": ["isn't", "is", "aren't", "doesn't"]},
    {"question": "They will attend the class, ___ they?", "correct_answer": "won't", "telugu_meaning": "వాళ్లు క్లాస్ attend అవుతారు, కదా?", "explanation": "'will' needs 'won't' tag.", "options": ["won't", "will", "can't", "don't"]},
    {"question": "You like coffee, ___ you?", "correct_answer": "don't", "telugu_meaning": "నీకు కాఫీ ఇష్టం, కదా?", "explanation": "Present simple needs 'don't' tag.", "options": ["don't", "do", "aren't", "isn't"]},
    {"question": "She isn't busy today, ___ she?", "correct_answer": "is", "telugu_meaning": "ఆమె ఈరోజు busy గా లేదు, కదా?", "explanation": "Negative statement needs positive tag.", "options": ["is", "isn't", "was", "does"]},
    {"question": "We should practice daily, ___ we?", "correct_answer": "shouldn't", "telugu_meaning": "మనం ప్రతిరోజూ practice చేయాలి, కదా?", "explanation": "Should -> shouldn't.", "options": ["shouldn't", "should", "couldn't", "can't"]},
    {"question": "He plays cricket well, ___ he?", "correct_answer": "doesn't", "telugu_meaning": "అతను బాగా క్రికెట్ ఆడతాడు, కదా?", "explanation": "Third person singular needs 'doesn't' tag.", "options": ["doesn't", "don't", "didn't", "isn't"]},
    {"question": "You completed the project, ___ you?", "correct_answer": "didn't", "telugu_meaning": "నువ్వు ప్రాజెక్ట్ పూర్తి చేశావు, కదా?", "explanation": "Past simple needs 'didn't' tag.", "options": ["didn't", "don't", "wasn't", "haven't"]},
    {"question": "The train arrived on time, ___ it?", "correct_answer": "didn't", "telugu_meaning": "ట్రైన్ సమయానికి వచ్చింది, కదా?", "explanation": "Past simple needs 'didn't' tag.", "options": ["didn't", "doesn't", "wasn't", "isn't"]}
]

# Generate more blanks
for i in range(10, 30):
    ex = examples[i]
    tag = ex['en'].split(',')[-1].strip().replace('?', '')
    question = ex['en'].replace(tag, "___")
    blanks.append({
        "question": question,
        "correct_answer": tag,
        "telugu_meaning": ex['te'],
        "explanation": "Question tag transformation.",
        "options": [tag, tag.replace("n't", ""), "don't", "didn't"]
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
    concept = Concept.objects.filter(name='Question Tags').first()
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
        print("Question Tags updated successfully.")
    else:
        print("Concept 'Question Tags' not found.")

update_concept_data()
