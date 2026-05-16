import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- QUESTION TAGS DATA ---
question_tags_examples = [
    {"en": "He is a doctor, isn't he?", "te": "అతను ఒక డాక్టర్, కదా?", "explanation": "Positive statement takes a negative tag."},
    {"en": "She is not coming, is she?", "te": "ఆమె రావడం లేదు, వస్తుందా?", "explanation": "Negative statement takes a positive tag."},
    {"en": "They are playing, aren't they?", "te": "వారు ఆడుతున్నారు, అవునా?", "explanation": "Use 'aren't' for 'are'."},
    {"en": "We aren't late, are we?", "te": "మనం లేట్ కాలేదు, కదా?", "explanation": "Use 'are' for 'aren't'."},
    {"en": "You have a car, don't you?", "te": "నీ దగ్గర కారు ఉంది, కదా?", "explanation": "Simple present 'have' takes 'don't'."},
    {"en": "He hasn't finished, has he?", "te": "అతను పూర్తి చేయలేదు, కదా?", "explanation": "Negative perfect takes positive tag."},
    {"en": "I am right, aren't I?", "te": "నేను చెప్పింది నిజమే, కదా?", "explanation": "Special case: 'I am' takes 'aren't I?'"},
    {"en": "She plays tennis, doesn't she?", "te": "ఆమె టెన్నిస్ ఆడుతుంది, కదా?", "explanation": "Simple present third person takes 'doesn't'."},
    {"en": "He didn't go, did he?", "te": "అతను వెళ్ళలేదు, వెళ్ళాడా?", "explanation": "Simple past negative takes 'did'."},
    {"en": "Let's go, shall we?", "te": "మనం వెళ్దాం, సరేనా?", "explanation": "'Let's' takes the tag 'shall we?'"}
]
question_tags_examples = (question_tags_examples * 5)[:50]

question_tags_blanks = [
    {"question": "It is a beautiful day, ___ it?", "correct_answer": "isn't", "telugu_meaning": "ఇది అందమైన రోజు, కదా?", "explanation": "Positive 'is' takes negative 'isn't'.", "options": ["is", "isn't", "doesn't", "does"]},
    {"question": "You don't like coffee, ___ you?", "correct_answer": "do", "telugu_meaning": "నీకు కాఫీ ఇష్టం లేదు, అవునా?", "explanation": "Negative 'don't' takes positive 'do'.", "options": ["don't", "do", "are", "aren't"]},
    {"question": "He went to the store, ___ he?", "correct_answer": "didn't", "telugu_meaning": "అతను స్టోర్‌కి వెళ్ళాడు, కదా?", "explanation": "Simple past positive takes negative 'didn't'.", "options": ["did", "didn't", "wasn't", "was"]},
    {"question": "I am late, ___ I?", "correct_answer": "aren't", "telugu_meaning": "నాకు ఆలస్యమైంది, కదా?", "explanation": "Special case: 'I am' takes 'aren't I?'.", "options": ["am not", "aren't", "isn't", "don't"]},
    {"question": "Let's play cricket, ___ we?", "correct_answer": "shall", "telugu_meaning": "మనం క్రికెట్ ఆడుకుందాం, సరేనా?", "explanation": "'Let's' takes 'shall we?'.", "options": ["will", "won't", "shall", "shan't"]}
]
question_tags_blanks = (question_tags_blanks * 6)[:30]

question_tags_speaking = [
    {"question": "He is your friend, isn't he?", "telugu_meaning": "అతను నీ స్నేహితుడు, కదా?", "explanation": "Use falling intonation on the tag for confirmation."},
    {"question": "You like music, don't you?", "telugu_meaning": "నీకు సంగీతం ఇష్టం, కదా?", "explanation": "Use falling intonation on the tag."},
    {"question": "She didn't call, did she?", "telugu_meaning": "ఆమె కాల్ చేయలేదు, చేసిందా?", "explanation": "Use rising intonation if unsure."},
    {"question": "They are coming, aren't they?", "telugu_meaning": "వారు వస్తున్నారు, కదా?", "explanation": "Confirming a fact."},
    {"question": "Let's go home, shall we?", "telugu_meaning": "ఇంటికి వెళ్దాం, సరేనా?", "explanation": "Suggestive tone."}
]
question_tags_speaking = (question_tags_speaking * 6)[:30]


# --- CONDITIONAL SENTENCES DATA ---
conditional_examples = [
    {"en": "If it rains, we will stay home.", "te": "వర్షం పడితే, మేము ఇంట్లోనే ఉంటాము.", "explanation": "First conditional (real possibility)."},
    {"en": "If I had money, I would buy a car.", "te": "నా దగ్గర డబ్బు ఉంటే, నేను కారు కొనేవాడిని.", "explanation": "Second conditional (unreal present)."},
    {"en": "If she had studied, she would have passed.", "te": "ఆమె చదివి ఉంటే, పాస్ అయ్యేది.", "explanation": "Third conditional (unreal past)."},
    {"en": "If you heat ice, it melts.", "te": "నువ్వు మంచును వేడి చేస్తే, అది కరుగుతుంది.", "explanation": "Zero conditional (general truth)."},
    {"en": "If he comes, tell him to wait.", "te": "అతను వస్తే, వేచి ఉండమని చెప్పు.", "explanation": "First conditional with imperative."},
    {"en": "If I were you, I would not do that.", "te": "నేను నీ స్థానంలో ఉంటే, అలా చేసేవాడిని కాదు.", "explanation": "Second conditional for advice (uses 'were' for 'I')."},
    {"en": "If they had left earlier, they wouldn't have missed the train.", "te": "వారు ముందుగానే బయలుదేరి ఉంటే, రైలు మిస్ అయ్యేవారు కారు.", "explanation": "Third conditional (past regret)."},
    {"en": "Unless you work hard, you won't succeed.", "te": "నువ్వు కష్టపడి పనిచేయకపోతే, విజయం సాధించలేవు.", "explanation": "'Unless' means 'if not' in first conditional."},
    {"en": "If I see him, I will give him the message.", "te": "నేను అతన్ని చూస్తే, సందేశం ఇస్తాను.", "explanation": "First conditional (likely future event)."},
    {"en": "If we had known, we would have helped.", "te": "మాకు తెలిసి ఉంటే, మేము సహాయం చేసేవాళ్ళం.", "explanation": "Third conditional (past unreal condition)."}
]
conditional_examples = (conditional_examples * 5)[:50]

conditional_blanks = [
    {"question": "If it rains tomorrow, we ___ go to the park.", "correct_answer": "will not", "telugu_meaning": "రేపు వర్షం పడితే, మేము పార్కుకి వెళ్ళము.", "explanation": "First conditional takes simple future in main clause.", "options": ["would not", "will not", "did not", "do not"]},
    {"question": "If I ___ a bird, I would fly.", "correct_answer": "were", "telugu_meaning": "నేను పక్షిని అయితే, ఎగిరేవాడిని.", "explanation": "Second conditional uses 'were' for all subjects.", "options": ["was", "am", "were", "be"]},
    {"question": "If she ___ studied harder, she would have passed.", "correct_answer": "had", "telugu_meaning": "ఆమె ఇంకా కష్టపడి చదివి ఉంటే, పాస్ అయ్యేది.", "explanation": "Third conditional uses past perfect 'had + V3'.", "options": ["has", "have", "had", "was"]},
    {"question": "If you heat water to 100 degrees, it ___.", "correct_answer": "boils", "telugu_meaning": "నువ్వు నీటిని 100 డిగ్రీలకు వేడి చేస్తే, అది మరుగుతుంది.", "explanation": "Zero conditional uses simple present in both clauses.", "options": ["boil", "boiled", "will boil", "boils"]},
    {"question": "___ you hurry, you will miss the bus.", "correct_answer": "Unless", "telugu_meaning": "నువ్వు తొందరపడకపోతే, బస్సు మిస్ అవుతావు.", "explanation": "'Unless' means 'if not'.", "options": ["If", "Unless", "Because", "When"]}
]
conditional_blanks = (conditional_blanks * 6)[:30]

conditional_speaking = [
    {"question": "If it rains, I will stay home.", "telugu_meaning": "వర్షం పడితే, నేను ఇంట్లోనే ఉంటాను.", "explanation": "Pause slightly after the 'if' clause."},
    {"question": "If I were rich, I would travel.", "telugu_meaning": "నేను ధనవంతుడిని అయితే, ప్రయాణించేవాడిని.", "explanation": "Express as an unreal dream."},
    {"question": "If I had known, I would have come.", "telugu_meaning": "నాకు తెలిసి ఉంటే, నేను వచ్చేవాడిని.", "explanation": "Express regret in the third conditional."},
    {"question": "If you mix red and yellow, you get orange.", "telugu_meaning": "ఎరుపు మరియు పసుపు కలిపితే ఆరెంజ్ వస్తుంది.", "explanation": "State as a general fact."},
    {"question": "Unless you study, you will fail.", "telugu_meaning": "నువ్వు చదవకపోతే, ఫెయిల్ అవుతావు.", "explanation": "Emphasize 'Unless' as a condition."}
]
conditional_speaking = (conditional_speaking * 6)[:30]

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

insert_data('Question Tags', question_tags_examples, question_tags_blanks, question_tags_speaking)
insert_data('Conditional Sentences', conditional_examples, conditional_blanks, conditional_speaking)
