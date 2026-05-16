import os
import django
import sys
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

blanks_data = [
    {"question": "She ___ reading a book right now.", "correct_answer": "is", "telugu_meaning": "ఆమె ఇప్పుడు పుస్తకం చదువుతోంది.", "explanation": "Present continuous tense uses 'is' for singular subjects.", "options": ["are", "am", "is", "was"]},
    {"question": "They ___ playing football yesterday.", "correct_answer": "were", "telugu_meaning": "వారు నిన్న ఫుట్‌బాల్ ఆడుతున్నారు.", "explanation": "Past continuous tense uses 'were' for plural subjects.", "options": ["was", "are", "were", "is"]},
    {"question": "I ___ finished my homework.", "correct_answer": "have", "telugu_meaning": "నేను నా హోంవర్క్ పూర్తి చేసాను.", "explanation": "Present perfect uses 'have' with 'I'.", "options": ["has", "had", "have", "am"]},
    {"question": "He ___ not know the answer.", "correct_answer": "does", "telugu_meaning": "అతనికి సమాధానం తెలియదు.", "explanation": "Simple present negative uses 'does not' for singular third person.", "options": ["do", "did", "does", "is"]},
    {"question": "We ___ go to the park tomorrow.", "correct_answer": "will", "telugu_meaning": "మేము రేపు పార్కుకి వెళ్తాము.", "explanation": "Future tense uses 'will'.", "options": ["would", "will", "shall", "can"]},
    {"question": "___ you like some coffee?", "correct_answer": "would", "telugu_meaning": "మీకు కాఫీ కావాలా?", "explanation": "Polite requests use 'would'.", "options": ["will", "can", "would", "do"]},
    {"question": "She ___ be at home by now.", "correct_answer": "should", "telugu_meaning": "ఆమె ఈ పాటికి ఇంట్లో ఉండాలి.", "explanation": "Expectation uses 'should'.", "options": ["could", "would", "should", "must"]},
    {"question": "I ___ swim when I was five.", "correct_answer": "could", "telugu_meaning": "నేను ఐదేళ్ల వయసులో ఈదగలిగాను.", "explanation": "Past ability uses 'could'.", "options": ["can", "may", "could", "would"]},
    {"question": "You ___ wear a helmet while riding.", "correct_answer": "must", "telugu_meaning": "మీరు బైక్ నడిపేటప్పుడు హెల్మెట్ తప్పక ధరించాలి.", "explanation": "Strong obligation uses 'must'.", "options": ["might", "must", "can", "would"]},
    {"question": "It ___ rain today.", "correct_answer": "might", "telugu_meaning": "ఈరోజు వర్షం పడవచ్చు.", "explanation": "Possibility uses 'might'.", "options": ["must", "can", "might", "will"]},
    {"question": "___ I come in?", "correct_answer": "may", "telugu_meaning": "నేను లోపలికి రావచ్చా?", "explanation": "Asking for permission uses 'may'.", "options": ["can", "will", "may", "must"]},
    {"question": "He ___ sleeping when I called.", "correct_answer": "was", "telugu_meaning": "నేను కాల్ చేసినప్పుడు అతను నిద్రపోతున్నాడు.", "explanation": "Past continuous uses 'was' for singular subjects.", "options": ["is", "was", "were", "has"]},
    {"question": "They ___ gone to the market.", "correct_answer": "have", "telugu_meaning": "వారు మార్కెట్‌కి వెళ్లారు.", "explanation": "Present perfect uses 'have' for plural subjects.", "options": ["has", "had", "have", "are"]},
    {"question": "I ___ not like spicy food.", "correct_answer": "do", "telugu_meaning": "నాకు కారం ఉన్న ఆహారం ఇష్టం లేదు.", "explanation": "Simple present negative uses 'do' with 'I'.", "options": ["does", "did", "do", "am"]},
    {"question": "She ___ finished her work before he arrived.", "correct_answer": "had", "telugu_meaning": "అతను రాకముందే ఆమె తన పనిని పూర్తి చేసింది.", "explanation": "Past perfect uses 'had'.", "options": ["has", "have", "had", "was"]},
    {"question": "___ you help me with this?", "correct_answer": "can", "telugu_meaning": "దీనితో మీరు నాకు సహాయం చేయగలరా?", "explanation": "Asking for ability/informal request uses 'can'.", "options": ["may", "must", "can", "should"]},
    {"question": "We ___ been waiting for an hour.", "correct_answer": "have", "telugu_meaning": "మేము ఒక గంట నుండి వేచి ఉన్నాము.", "explanation": "Present perfect continuous uses 'have been' for plural subjects.", "options": ["has", "had", "have", "are"]},
    {"question": "He ___ to go to the doctor.", "correct_answer": "has", "telugu_meaning": "అతను డాక్టర్ దగ్గరికి వెళ్ళాలి.", "explanation": "Obligation uses 'has to' for singular third person.", "options": ["have", "had", "has", "must"]},
    {"question": "I ___ rather stay at home.", "correct_answer": "would", "telugu_meaning": "నేను ఇంట్లోనే ఉండాలనుకుంటున్నాను.", "explanation": "Preference uses 'would rather'.", "options": ["could", "should", "would", "will"]},
    {"question": "You ___ better leave now.", "correct_answer": "had", "telugu_meaning": "మీరు ఇప్పుడు వెళ్లడం మంచిది.", "explanation": "Advice uses 'had better'.", "options": ["have", "has", "had", "would"]},
    {"question": "___ they coming to the party?", "correct_answer": "are", "telugu_meaning": "వారు పార్టీకి వస్తున్నారా?", "explanation": "Present continuous question uses 'are' for plural subjects.", "options": ["is", "am", "are", "do"]},
    {"question": "She ___ not been feeling well lately.", "correct_answer": "has", "telugu_meaning": "ఈమధ్య ఆమెకు ఒంట్లో బాగోలేదు.", "explanation": "Present perfect continuous uses 'has' for singular subjects.", "options": ["have", "had", "has", "is"]},
    {"question": "I ___ be late for the meeting.", "correct_answer": "might", "telugu_meaning": "నేను మీటింగ్‌కి లేట్ అవ్వవచ్చు.", "explanation": "Possibility uses 'might'.", "options": ["must", "can", "might", "would"]},
    {"question": "___ we start the presentation?", "correct_answer": "shall", "telugu_meaning": "మనం ప్రెజెంటేషన్ ప్రారంభిద్దామా?", "explanation": "Suggestions use 'shall' with 'we'.", "options": ["will", "would", "shall", "must"]},
    {"question": "He ___ be joking!", "correct_answer": "must", "telugu_meaning": "అతను కచ్చితంగా జోక్ చేస్తుండాలి!", "explanation": "Strong deduction uses 'must'.", "options": ["can", "might", "must", "should"]},
    {"question": "They ___ not agree with you.", "correct_answer": "may", "telugu_meaning": "వారు మీతో ఏకీభవించకపోవచ్చు.", "explanation": "Possibility uses 'may'.", "options": ["must", "can", "may", "will"]},
    {"question": "I ___ going to call you.", "correct_answer": "was", "telugu_meaning": "నేను నీకు కాల్ చేద్దామనుకున్నాను.", "explanation": "Past intention uses 'was going to'.", "options": ["am", "is", "was", "were"]},
    {"question": "___ you ever been to London?", "correct_answer": "have", "telugu_meaning": "మీరు ఎప్పుడైనా లండన్ వెళ్లారా?", "explanation": "Present perfect question uses 'have'.", "options": ["has", "had", "have", "did"]},
    {"question": "She ___ be very tired after the journey.", "correct_answer": "must", "telugu_meaning": "ప్రయాణం తర్వాత ఆమె బాగా అలసిపోయి ఉండాలి.", "explanation": "Strong deduction uses 'must'.", "options": ["can", "might", "must", "should"]},
    {"question": "We ___ not afford that car.", "correct_answer": "cannot", "telugu_meaning": "మేము ఆ కారుని కొనుక్కోలేము.", "explanation": "Inability uses 'cannot'.", "options": ["may not", "must not", "cannot", "should not"]}
]

speaking_data = [
    {"question": "I am learning English.", "telugu_meaning": "నేను ఇంగ్లీష్ నేర్చుకుంటున్నాను.", "explanation": "Focus on pronouncing 'am' clearly."},
    {"question": "She is going to the market.", "telugu_meaning": "ఆమె మార్కెట్‌కి వెళ్తోంది.", "explanation": "Notice the use of 'is' for singular."},
    {"question": "They are playing in the garden.", "telugu_meaning": "వారు గార్డెన్‌లో ఆడుతున్నారు.", "explanation": "Emphasize 'are' for plural."},
    {"question": "He was watching TV.", "telugu_meaning": "అతను టీవీ చూస్తున్నాడు.", "explanation": "Past continuous with 'was'."},
    {"question": "We were waiting for you.", "telugu_meaning": "మేము నీకోసం ఎదురు చూస్తున్నాము.", "explanation": "Past continuous with 'were'."},
    {"question": "I have finished my work.", "telugu_meaning": "నేను నా పని పూర్తి చేసాను.", "explanation": "Present perfect with 'have'."},
    {"question": "She has gone out.", "telugu_meaning": "ఆమె బయటికి వెళ్ళింది.", "explanation": "Present perfect with 'has'."},
    {"question": "They had left before I arrived.", "telugu_meaning": "నేను వచ్చేలోపే వారు వెళ్ళిపోయారు.", "explanation": "Past perfect with 'had'."},
    {"question": "I do not like coffee.", "telugu_meaning": "నాకు కాఫీ ఇష్టం లేదు.", "explanation": "Negative sentence with 'do not'."},
    {"question": "He does not speak Telugu.", "telugu_meaning": "అతను తెలుగు మాట్లాడడు.", "explanation": "Negative sentence with 'does not'."},
    {"question": "We did not go there.", "telugu_meaning": "మేము అక్కడికి వెళ్లలేదు.", "explanation": "Past negative with 'did not'."},
    {"question": "I will call you later.", "telugu_meaning": "నేను నీకు తర్వాత కాల్ చేస్తాను.", "explanation": "Future tense with 'will'."},
    {"question": "You should see a doctor.", "telugu_meaning": "నువ్వు డాక్టర్‌ని కలవాలి.", "explanation": "Advice with 'should'."},
    {"question": "I can swim very well.", "telugu_meaning": "నేను చాలా బాగా ఈదగలను.", "explanation": "Ability with 'can'."},
    {"question": "Could you help me, please?", "telugu_meaning": "దయచేసి నాకు సహాయం చేయగలరా?", "explanation": "Polite request with 'could'."},
    {"question": "May I come in?", "telugu_meaning": "నేను లోపలికి రావచ్చా?", "explanation": "Asking permission with 'may'."},
    {"question": "It might rain today.", "telugu_meaning": "ఈరోజు వర్షం పడవచ్చు.", "explanation": "Possibility with 'might'."},
    {"question": "You must wear a seatbelt.", "telugu_meaning": "నువ్వు తప్పక సీట్ బెల్ట్ పెట్టుకోవాలి.", "explanation": "Obligation with 'must'."},
    {"question": "Would you like some tea?", "telugu_meaning": "మీకు కొంచెం టీ కావాలా?", "explanation": "Offer with 'would'."},
    {"question": "I would rather stay home.", "telugu_meaning": "నేను ఇంట్లోనే ఉండాలనుకుంటున్నాను.", "explanation": "Preference with 'would rather'."},
    {"question": "She ought to apologize.", "telugu_meaning": "ఆమె క్షమాపణ చెప్పాలి.", "explanation": "Moral obligation with 'ought to'."},
    {"question": "He used to live here.", "telugu_meaning": "అతను ఒకప్పుడు ఇక్కడ నివసించేవాడు.", "explanation": "Past habit with 'used to'."},
    {"question": "You had better leave now.", "telugu_meaning": "నువ్వు ఇప్పుడే వెళ్లడం మంచిది.", "explanation": "Strong advice with 'had better'."},
    {"question": "Are you coming with us?", "telugu_meaning": "నువ్వు మాతో వస్తున్నావా?", "explanation": "Question starting with 'Are'."},
    {"question": "Is he your brother?", "telugu_meaning": "అతను నీ సోదరుడా?", "explanation": "Question starting with 'Is'."},
    {"question": "Do you like music?", "telugu_meaning": "నీకు సంగీతం అంటే ఇష్టమా?", "explanation": "Question starting with 'Do'."},
    {"question": "Did you finish it?", "telugu_meaning": "నువ్వు దాన్ని పూర్తి చేసావా?", "explanation": "Question starting with 'Did'."},
    {"question": "Have you seen this movie?", "telugu_meaning": "నువ్వు ఈ సినిమా చూశావా?", "explanation": "Question starting with 'Have'."},
    {"question": "Has she called yet?", "telugu_meaning": "ఆమె ఇంకా కాల్ చేసిందా?", "explanation": "Question starting with 'Has'."},
    {"question": "Will you be there?", "telugu_meaning": "నువ్వు అక్కడ ఉంటావా?", "explanation": "Question starting with 'Will'."}
]

concept = Concept.objects.filter(name='Helping Verbs').first()
if concept:
    for item in blanks_data:
        Exercise.objects.create(
            concept=concept,
            type='FILL_BLANK',
            question=item['question'],
            correct_answer=item['correct_answer'],
            explanation=item['explanation'],
            telugu_meaning=item['telugu_meaning'],
            options=item['options']
        )
    for item in speaking_data:
        Exercise.objects.create(
            concept=concept,
            type='READ_ALOUD',
            question=item['question'],
            telugu_meaning=item['telugu_meaning'],
            explanation=item['explanation']
        )
    print("Helping Verbs completed successfully.")
else:
    print("Concept not found.")
