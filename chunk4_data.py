import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- DIRECT SPEECH DATA ---
direct_examples = [
    {"en": "He said, 'I am happy.'", "te": "అతను 'నేను సంతోషంగా ఉన్నాను' అని అన్నాడు.", "explanation": "Exact words of the speaker are in quotes."},
    {"en": "She said, 'I like ice cream.'", "te": "ఆమె 'నాకు ఐస్ క్రీమ్ ఇష్టం' అని చెప్పింది.", "explanation": "Quotes enclose the exact spoken sentence."},
    {"en": "Ram said to me, 'I am going to school.'", "te": "రామ్ నాతో 'నేను పాఠశాలకు వెళ్తున్నాను' అని అన్నాడు.", "explanation": "Reporting verb 'said to' introduces the quote."},
    {"en": "The teacher said, 'Sit down.'", "te": "ఉపాధ్యాయుడు 'కూర్చోండి' అని చెప్పారు.", "explanation": "Direct command enclosed in quotes."},
    {"en": "He said, 'Where are you going?'", "te": "అతను 'నువ్వు ఎక్కడికి వెళ్తున్నావు?' అని అడిగాడు.", "explanation": "Direct question enclosed in quotes."},
    {"en": "She said, 'What a beautiful flower!'", "te": "ఆమె 'ఎంత అందమైన పువ్వు!' అని ఆశ్చర్యపోయింది.", "explanation": "Direct exclamation enclosed in quotes."},
    {"en": "Mother said, 'I have cooked dinner.'", "te": "అమ్మ 'నేను రాత్రి భోజనం వండాను' అని చెప్పింది.", "explanation": "Direct statement of action completed."},
    {"en": "He said, 'I will come tomorrow.'", "te": "అతను 'నేను రేపు వస్తాను' అని అన్నాడు.", "explanation": "Direct statement about the future."},
    {"en": "She said, 'I cannot help you.'", "te": "ఆమె 'నేను నీకు సహాయం చేయలేను' అని చెప్పింది.", "explanation": "Direct negative statement."},
    {"en": "They said, 'We won the match.'", "te": "వారు 'మేము మ్యాచ్ గెలిచాము' అని అన్నారు.", "explanation": "Direct statement of past event."}
]
direct_examples = (direct_examples * 5)[:50]

direct_blanks = [
    {"question": "He said, ___I am busy.___ ", "correct_answer": "''", "telugu_meaning": "అతను, 'నేను బిజీగా ఉన్నాను' అని అన్నాడు.", "explanation": "Direct speech must be enclosed in quotation marks.", "options": ["''", "()", "[]", "nothing"]},
    {"question": "She ___ , 'I want to sleep.'", "correct_answer": "said", "telugu_meaning": "ఆమె, 'నాకు నిద్రపోవాలని ఉంది' అని చెప్పింది.", "explanation": "Reporting verb.", "options": ["told", "said", "asked", "say"]},
    {"question": "He said to me, '___ are you?'", "correct_answer": "How", "telugu_meaning": "అతను నాతో, 'నువ్వు ఎలా ఉన్నావు?' అని అన్నాడు.", "explanation": "Direct question word.", "options": ["What", "How", "Where", "Who"]},
    {"question": "The boy said, 'I ___ playing.'", "correct_answer": "am", "telugu_meaning": "బాలుడు, 'నేను ఆడుకుంటున్నాను' అని అన్నాడు.", "explanation": "Direct present continuous.", "options": ["is", "am", "are", "was"]},
    {"question": "Mother said, '___ the door.'", "correct_answer": "Close", "telugu_meaning": "అమ్మ, 'తలుపు మూసివేయి' అని చెప్పింది.", "explanation": "Direct command.", "options": ["Closed", "Closing", "Close", "Closes"]}
]
direct_blanks = (direct_blanks * 6)[:30]

direct_speaking = [
    {"question": "He said, 'I am tired.'", "telugu_meaning": "అతను 'నేను అలసిపోయాను' అని అన్నాడు.", "explanation": "Pause slightly before quoting."},
    {"question": "She said, 'I need help.'", "telugu_meaning": "ఆమె 'నాకు సహాయం కావాలి' అని చెప్పింది.", "explanation": "Pause slightly before quoting."},
    {"question": "Ram said, 'I will go.'", "telugu_meaning": "రామ్ 'నేను వెళ్తాను' అని అన్నాడు.", "explanation": "Pause slightly before quoting."},
    {"question": "The teacher said, 'Quiet.'", "telugu_meaning": "ఉపాధ్యాయుడు 'నిశ్శబ్దం' అని చెప్పారు.", "explanation": "Express as a direct command."},
    {"question": "He said, 'Are you okay?'", "telugu_meaning": "అతను 'నువ్వు బాగానే ఉన్నావా?' అని అడిగాడు.", "explanation": "Express as a direct question."}
]
direct_speaking = (direct_speaking * 6)[:30]


# --- INDIRECT SPEECH DATA ---
indirect_examples = [
    {"en": "He said that he was happy.", "te": "అతను తాను సంతోషంగా ఉన్నానని అన్నాడు.", "explanation": "Reported speech using 'that', present tense changes to past."},
    {"en": "She said that she liked ice cream.", "te": "ఆమెకు ఐస్ క్రీమ్ ఇష్టమని ఆమె చెప్పింది.", "explanation": "Present simple 'like' changes to past simple 'liked'."},
    {"en": "Ram told me that he was going to school.", "te": "రామ్ తాను పాఠశాలకు వెళ్తున్నానని నాతో చెప్పాడు.", "explanation": "'Said to' changes to 'told', present continuous to past continuous."},
    {"en": "The teacher ordered them to sit down.", "te": "ఉపాధ్యాయుడు వారిని కూర్చోమని ఆదేశించాడు.", "explanation": "Command changes to infinitive 'to sit'."},
    {"en": "He asked where I was going.", "te": "నేను ఎక్కడికి వెళ్తున్నానని అతను అడిగాడు.", "explanation": "Question changes to statement format after 'asked'."},
    {"en": "She exclaimed that it was a beautiful flower.", "te": "అది చాలా అందమైన పువ్వు అని ఆమె ఆశ్చర్యపోయింది.", "explanation": "Exclamation changes to 'exclaimed that'."},
    {"en": "Mother said that she had cooked dinner.", "te": "అమ్మ తాను రాత్రి భోజనం వండానని చెప్పింది.", "explanation": "Present perfect changes to past perfect."},
    {"en": "He said that he would come the next day.", "te": "అతను మరుసటి రోజు వస్తానని అన్నాడు.", "explanation": "'Will' changes to 'would', 'tomorrow' to 'the next day'."},
    {"en": "She said that she could not help me.", "te": "ఆమె నాకు సహాయం చేయలేనని చెప్పింది.", "explanation": "'Cannot' changes to 'could not'."},
    {"en": "They said that they had won the match.", "te": "వారు మ్యాచ్ గెలిచామని అన్నారు.", "explanation": "Past simple 'won' changes to past perfect 'had won'."}
]
indirect_examples = (indirect_examples * 5)[:50]

indirect_blanks = [
    {"question": "He said ___ he was busy.", "correct_answer": "that", "telugu_meaning": "అతను తాను బిజీగా ఉన్నానని అన్నాడు.", "explanation": "Conjunction used in indirect statements.", "options": ["if", "that", "whether", "what"]},
    {"question": "She ___ me that she wanted to sleep.", "correct_answer": "told", "telugu_meaning": "ఆమె తాను నిద్రపోవాలని అనుకుంటున్నానని నాతో చెప్పింది.", "explanation": "Used when the listener is mentioned.", "options": ["said", "told", "asked", "spoke"]},
    {"question": "He asked me ___ I was.", "correct_answer": "how", "telugu_meaning": "అతను నేను ఎలా ఉన్నానని అడిగాడు.", "explanation": "Question word used as a connector.", "options": ["that", "if", "how", "whether"]},
    {"question": "The boy said that he ___ playing.", "correct_answer": "was", "telugu_meaning": "బాలుడు తాను ఆడుకుంటున్నానని అన్నాడు.", "explanation": "Present continuous changes to past continuous.", "options": ["am", "is", "was", "were"]},
    {"question": "Mother ordered me ___ close the door.", "correct_answer": "to", "telugu_meaning": "తలుపు మూసివేయమని అమ్మ నన్ను ఆదేశించింది.", "explanation": "Commands use 'to' + verb.", "options": ["that", "to", "for", "if"]}
]
indirect_blanks = (indirect_blanks * 6)[:30]

indirect_speaking = [
    {"question": "He said that he was tired.", "telugu_meaning": "అతను తాను అలసిపోయానని అన్నాడు.", "explanation": "Speak fluently as a single statement."},
    {"question": "She said that she needed help.", "telugu_meaning": "ఆమెకు సహాయం కావాలని ఆమె చెప్పింది.", "explanation": "Speak fluently as a single statement."},
    {"question": "Ram said that he would go.", "telugu_meaning": "రామ్ తాను వెళ్తానని అన్నాడు.", "explanation": "Speak fluently as a single statement."},
    {"question": "The teacher ordered us to be quiet.", "telugu_meaning": "ఉపాధ్యాయుడు మమ్మల్ని నిశ్శబ్దంగా ఉండమని ఆదేశించాడు.", "explanation": "Speak fluently as a single statement."},
    {"question": "He asked if I was okay.", "telugu_meaning": "నేను బాగానే ఉన్నానా అని అతను అడిగాడు.", "explanation": "Speak fluently as an indirect question."}
]
indirect_speaking = (indirect_speaking * 6)[:30]


# --- MODALS DATA ---
modals_examples = [
    {"en": "I can speak English.", "te": "నేను ఇంగ్లీష్ మాట్లాడగలను.", "explanation": "'can' expresses ability."},
    {"en": "Could you help me?", "te": "మీరు నాకు సహాయం చేయగలరా?", "explanation": "'could' expresses a polite request."},
    {"en": "It may rain today.", "te": "ఈరోజు వర్షం పడవచ్చు.", "explanation": "'may' expresses possibility."},
    {"en": "Might I ask a question?", "te": "నేను ఒక ప్రశ్న అడగవచ్చా?", "explanation": "'might' expresses a formal, hesitant request."},
    {"en": "You must wear a helmet.", "te": "మీరు తప్పక హెల్మెట్ ధరించాలి.", "explanation": "'must' expresses strong obligation."},
    {"en": "We should respect our elders.", "te": "మనం పెద్దలను గౌరవించాలి.", "explanation": "'should' expresses duty or advice."},
    {"en": "I will call you later.", "te": "నేను నీకు తర్వాత కాల్ చేస్తాను.", "explanation": "'will' expresses a future action or promise."},
    {"en": "Would you like some tea?", "te": "మీకు టీ కావాలా?", "explanation": "'would' expresses an offer or polite request."},
    {"en": "Shall we go now?", "te": "మనం ఇప్పుడు వెళ్దామా?", "explanation": "'shall' expresses a suggestion."},
    {"en": "You ought to apologize.", "te": "నువ్వు క్షమాపణ చెప్పాలి.", "explanation": "'ought to' expresses moral obligation."}
]
modals_examples = (modals_examples * 5)[:50]

modals_blanks = [
    {"question": "I ___ swim very fast.", "correct_answer": "can", "telugu_meaning": "నేను చాలా వేగంగా ఈదగలను.", "explanation": "Ability.", "options": ["may", "can", "must", "should"]},
    {"question": "___ I come in, sir?", "correct_answer": "May", "telugu_meaning": "నేను లోపలికి రావచ్చా, సార్?", "explanation": "Formal permission.", "options": ["Can", "Will", "May", "Must"]},
    {"question": "You ___ obey the rules.", "correct_answer": "must", "telugu_meaning": "మీరు తప్పక నియమాలను పాటించాలి.", "explanation": "Strong obligation.", "options": ["can", "may", "must", "might"]},
    {"question": "We ___ help the poor.", "correct_answer": "should", "telugu_meaning": "మనం పేదలకు సహాయం చేయాలి.", "explanation": "Moral duty or advice.", "options": ["can", "may", "should", "might"]},
    {"question": "___ you open the door, please?", "correct_answer": "Could", "telugu_meaning": "దయచేసి మీరు తలుపు తీయగలరా?", "explanation": "Polite request.", "options": ["May", "Might", "Could", "Should"]}
]
modals_blanks = (modals_blanks * 6)[:30]

modals_speaking = [
    {"question": "I can do it.", "telugu_meaning": "నేను దానిని చేయగలను.", "explanation": "Emphasize 'can' for ability."},
    {"question": "May I help you?", "telugu_meaning": "నేను మీకు సహాయం చేయవచ్చా?", "explanation": "Emphasize 'May' for polite offer."},
    {"question": "You must listen.", "telugu_meaning": "నువ్వు తప్పక వినాలి.", "explanation": "Emphasize 'must' for strong obligation."},
    {"question": "We should go now.", "telugu_meaning": "మనం ఇప్పుడు వెళ్లాలి.", "explanation": "Emphasize 'should' for advice."},
    {"question": "Would you like coffee?", "telugu_meaning": "మీకు కాఫీ కావాలా?", "explanation": "Emphasize 'Would' for a polite offer."}
]
modals_speaking = (modals_speaking * 6)[:30]

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

insert_data('Direct Speech', direct_examples, direct_blanks, direct_speaking)
insert_data('Indirect Speech', indirect_examples, indirect_blanks, indirect_speaking)
insert_data('Modals', modals_examples, modals_blanks, modals_speaking)
