import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- FLUENCY DATA ---
fluency_content = "Fluency is the ability to speak easily, smoothly, and continuously without pausing a lot. It means your thoughts flow naturally into words."
fluency_rules = """
- Do not worry too much about grammar mistakes while speaking.
- Think in English rather than translating from your mother tongue.
- Practice speaking out loud every day.
- Learn phrases and expressions rather than individual words to speak faster.
"""

fluency_examples = [
    {"en": "She speaks English fluently.", "te": "ఆమె ఇంగ్లీష్ అనర్గళంగా మాట్లాడుతుంది.", "explanation": "Speaking without hesitation."},
    {"en": "I want to improve my speaking fluency.", "te": "నేను నా మాట్లాడే ధారాళతను మెరుగుపరచుకోవాలనుకుంటున్నాను.", "explanation": "A common learning goal."},
    {"en": "He paused for a moment to find the right word.", "te": "సరైన పదాన్ని వెతకడానికి అతను క్షణం పాటు ఆగాడు.", "explanation": "Lack of fluency causes pauses."},
    {"en": "Practice helps you speak naturally.", "te": "ప్రాక్టీస్ చేయడం వల్ల మీరు సహజంగా మాట్లాడగలుగుతారు.", "explanation": "The key to fluency."},
    {"en": "Don't translate in your head.", "te": "మీ మనస్సులో అనువదించకండి.", "explanation": "A tip for fluency."},
    {"en": "Her speech was smooth and continuous.", "te": "ఆమె ప్రసంగం సాఫీగా మరియు నిరంతరంగా సాగింది.", "explanation": "Describing fluent speech."},
    {"en": "Fluency comes with regular practice.", "te": "క్రమం తప్పకుండా సాధన చేయడం ద్వారా అనర్గళంగా మాట్లాడటం వస్తుంది.", "explanation": "Fact about language learning."},
    {"en": "I get stuck when I try to speak fast.", "te": "నేను వేగంగా మాట్లాడటానికి ప్రయత్నించినప్పుడు ఆగిపోతాను.", "explanation": "A fluency challenge."},
    {"en": "Listen to native speakers to understand the flow.", "te": "ఫ్లో (ధారాళత) అర్థం చేసుకోవడానికి మాతృభాషగా మాట్లాడేవారిని వినండి.", "explanation": "Fluency advice."},
    {"en": "Confidence boosts your fluency.", "te": "ఆత్మవిశ్వాసం మీ ధారాళతను పెంచుతుంది.", "explanation": "Connection between confidence and fluency."}
]
fluency_examples = (fluency_examples * 5)[:50]

fluency_blanks = [
    {"question": "He wants to speak English ___.", "correct_answer": "fluently", "telugu_meaning": "అతను ఇంగ్లీష్ అనర్గళంగా మాట్లాడాలనుకుంటున్నాడు.", "explanation": "Adverb for speaking smoothly.", "options": ["fluent", "fluently", "fluency", "fast"]},
    {"question": "To improve fluency, stop ___ in your head.", "correct_answer": "translating", "telugu_meaning": "ధారాళత మెరుగుపరచడానికి, మీ మనస్సులో అనువదించడం ఆపండి.", "explanation": "Thinking in native language slows you down.", "options": ["speaking", "listening", "translating", "writing"]},
    {"question": "Her ___ was smooth and continuous.", "correct_answer": "speech", "telugu_meaning": "ఆమె ప్రసంగం సాఫీగా మరియు నిరంతరంగా సాగింది.", "explanation": "The act of speaking.", "options": ["walk", "speech", "run", "jump"]},
    {"question": "Fluency means speaking without too many ___.", "correct_answer": "pauses", "telugu_meaning": "ధారాళత అంటే చాలా పాజ్‌లు (విరామాలు) లేకుండా మాట్లాడటం.", "explanation": "Stopping while speaking.", "options": ["words", "sentences", "pauses", "sounds"]},
    {"question": "Practice helps you speak more ___.", "correct_answer": "naturally", "telugu_meaning": "ప్రాక్టీస్ చేయడం వల్ల మీరు మరింత సహజంగా మాట్లాడగలుగుతారు.", "explanation": "Speaking like a native.", "options": ["naturally", "hardly", "badly", "slowly"]}
]
fluency_blanks = (fluency_blanks * 6)[:30]

fluency_speaking = [
    {"question": "I want to speak fluently.", "telugu_meaning": "నేను అనర్గళంగా మాట్లాడాలనుకుంటున్నాను.", "explanation": "Say it smoothly without stopping."},
    {"question": "Practice makes you perfect.", "telugu_meaning": "ప్రాక్టీస్ మిమ్మల్ని పర్ఫెక్ట్ చేస్తుంది.", "explanation": "Say it as one continuous thought."},
    {"question": "Don't translate in your head.", "telugu_meaning": "మీ మనసులో అనువదించుకోకండి.", "explanation": "Connect the words naturally."},
    {"question": "She speaks English very well.", "telugu_meaning": "ఆమె ఇంగ్లీష్ చాలా బాగా మాట్లాడుతుంది.", "explanation": "Focus on the flow of the sentence."},
    {"question": "Listen to native speakers every day.", "telugu_meaning": "ప్రతిరోజూ నేటివ్ స్పీకర్స్ వినండి.", "explanation": "Maintain a steady pace."}
]
fluency_speaking = (fluency_speaking * 6)[:30]


# --- PRONUNCIATION DATA ---
pronunciation_content = "Pronunciation refers to the way a word or a language is spoken. Good pronunciation ensures that the listener understands exactly what you are saying."
pronunciation_rules = """
- Learn the sounds of English (phonetics) that don't exist in your native language.
- Pay attention to word stress (e.g., reCORD vs REcord).
- Use online dictionaries to listen to the audio of new words.
- Record yourself speaking and compare it with native speakers.
"""

pronunciation_examples = [
    {"en": "His pronunciation is very clear.", "te": "అతని ఉచ్చారణ చాలా స్పష్టంగా ఉంది.", "explanation": "Easy to understand."},
    {"en": "How do you pronounce this word?", "te": "మీరు ఈ పదాన్ని ఎలా ఉచ్చరిస్తారు?", "explanation": "Asking for pronunciation help."},
    {"en": "She mispronounced my name.", "te": "ఆమె నా పేరును తప్పుగా ఉచ్చరించింది.", "explanation": "Saying something incorrectly."},
    {"en": "English spelling can be tricky for pronunciation.", "te": "ఇంగ్లీష్ స్పెల్లింగ్ ఉచ్చారణకు గమ్మత్తుగా ఉంటుంది.", "explanation": "Spelling doesn't always match sound."},
    {"en": "You need to stress the first syllable.", "te": "మీరు మొదటి అక్షరాన్ని నొక్కి చెప్పాలి.", "explanation": "Talking about word stress."},
    {"en": "Listen to the audio and repeat.", "te": "ఆడియో విని రిపీట్ చేయండి.", "explanation": "Practice method."},
    {"en": "He has a problem pronouncing the 'th' sound.", "te": "అతనికి 'th' శబ్దాన్ని ఉచ్చరించడంలో సమస్య ఉంది.", "explanation": "A common difficulty."},
    {"en": "Clear pronunciation is better than a fake accent.", "te": "నకిలీ యాస కంటే స్పష్టమైన ఉచ్చారణ మంచిది.", "explanation": "Pronunciation vs Accent."},
    {"en": "I am working on my pronunciation skills.", "te": "నేను నా ఉచ్చారణ నైపుణ్యాలపై పని చేస్తున్నాను.", "explanation": "Self-improvement."},
    {"en": "Phonetics helps in understanding pronunciation.", "te": "ఉచ్చారణను అర్థం చేసుకోవడంలో ఫొనెటిక్స్ సహాయపడుతుంది.", "explanation": "The study of speech sounds."}
]
pronunciation_examples = (pronunciation_examples * 5)[:50]

pronunciation_blanks = [
    {"question": "How do you ___ this word?", "correct_answer": "pronounce", "telugu_meaning": "మీరు ఈ పదాన్ని ఎలా ఉచ్చరిస్తారు?", "explanation": "Verb for making word sounds.", "options": ["spell", "write", "pronounce", "read"]},
    {"question": "His ___ is very clear.", "correct_answer": "pronunciation", "telugu_meaning": "అతని ఉచ్చారణ చాలా స్పష్టంగా ఉంది.", "explanation": "Noun for the way words are spoken.", "options": ["grammar", "pronunciation", "spelling", "writing"]},
    {"question": "You must put the ___ on the right syllable.", "correct_answer": "stress", "telugu_meaning": "మీరు సరైన సిలబుల్‌పై ఒత్తిడి (స్ట్రెస్) ఉంచాలి.", "explanation": "Emphasis on a part of a word.", "options": ["stress", "letter", "sound", "voice"]},
    {"question": "She ___ my name incorrectly.", "correct_answer": "mispronounced", "telugu_meaning": "ఆమె నా పేరును తప్పుగా ఉచ్చరించింది.", "explanation": "Pronounced wrongly.", "options": ["spelled", "wrote", "mispronounced", "called"]},
    {"question": "Listen to the ___ to learn how to say it.", "correct_answer": "audio", "telugu_meaning": "దానిని ఎలా చెప్పాలో తెలుసుకోవడానికి ఆడియో వినండి.", "explanation": "Sound recording.", "options": ["video", "audio", "book", "text"]}
]
pronunciation_blanks = (pronunciation_blanks * 6)[:30]

pronunciation_speaking = [
    {"question": "How do you pronounce this word?", "telugu_meaning": "ఈ పదాన్ని ఎలా ఉచ్చరించాలి?", "explanation": "Focus on clarity."},
    {"question": "My pronunciation is getting better.", "telugu_meaning": "నా ఉచ్చారణ మెరుగుపడుతోంది.", "explanation": "Say 'pronunciation' clearly."},
    {"question": "Stress the first syllable.", "telugu_meaning": "మొదటి అక్షరాన్ని నొక్కి చెప్పండి.", "explanation": "Emphasize the word 'stress'."},
    {"question": "Listen and repeat after me.", "telugu_meaning": "వినండి మరియు నా తర్వాత రిపీట్ చేయండి.", "explanation": "Speak with a guiding tone."},
    {"question": "Clear speech is very important.", "telugu_meaning": "స్పష్టమైన మాట చాలా ముఖ్యం.", "explanation": "Enunciate every word."}
]
pronunciation_speaking = (pronunciation_speaking * 6)[:30]


# --- ACCENT DATA ---
accent_content = "An accent is a distinctive way of pronouncing a language, especially one associated with a particular country, area, or social class. Focus on clarity rather than changing your accent entirely."
accent_rules = """
- Remember that everyone has an accent.
- A neutral accent is one that is easy for people globally to understand.
- Do not fake an American or British accent if it makes you difficult to understand.
- Focus on intonation (the rise and fall of the voice) to sound more natural.
"""

accent_examples = [
    {"en": "He speaks with a strong British accent.", "te": "అతను బలమైన బ్రిటిష్ యాసతో మాట్లాడుతాడు.", "explanation": "Specific regional accent."},
    {"en": "Your accent is very easy to understand.", "te": "మీ యాస అర్థం చేసుకోవడం చాలా సులభం.", "explanation": "A clear, neutral accent."},
    {"en": "She is trying to learn an American accent.", "te": "ఆమె అమెరికన్ యాసను నేర్చుకోవడానికి ప్రయత్నిస్తోంది.", "explanation": "Acquiring a new accent."},
    {"en": "Don't fake your accent.", "te": "మీ యాసను నకిలీ చేయకండి.", "explanation": "Advice on speaking naturally."},
    {"en": "Everyone has an accent.", "te": "ప్రతి ఒక్కరికీ యాస ఉంటుంది.", "explanation": "A linguistic fact."},
    {"en": "Intonation is more important than accent.", "te": "యాస కంటే ఇంటోనేషన్ (స్వరం హెచ్చుతగ్గులు) చాలా ముఖ్యం.", "explanation": "Focusing on rhythm."},
    {"en": "I love the Australian accent.", "te": "నాకు ఆస్ట్రేలియన్ యాస అంటే ఇష్టం.", "explanation": "Expressing preference."},
    {"en": "A neutral accent helps in global communication.", "te": "న్యూట్రల్ యాస గ్లోబల్ కమ్యూనికేషన్‌లో సహాయపడుతుంది.", "explanation": "Benefit of neutrality."},
    {"en": "Can you guess my accent?", "te": "నా యాసను మీరు ఊహించగలరా?", "explanation": "A common conversation starter."},
    {"en": "Her accent shows she is from the south.", "te": "ఆమె యాస ఆమె దక్షిణ ప్రాంతం నుండి వచ్చినట్లు చూపుతుంది.", "explanation": "Accents indicate origins."}
]
accent_examples = (accent_examples * 5)[:50]

accent_blanks = [
    {"question": "He has a strong British ___.", "correct_answer": "accent", "telugu_meaning": "అతనికి బలమైన బ్రిటిష్ యాస ఉంది.", "explanation": "Way of pronunciation.", "options": ["voice", "sound", "accent", "tone"]},
    {"question": "A ___ accent is easy for everyone to understand.", "correct_answer": "neutral", "telugu_meaning": "న్యూట్రల్ (తటస్థ) యాసను ఎవరైనా సులభంగా అర్థం చేసుకోవచ్చు.", "explanation": "An accent without strong regional features.", "options": ["fake", "neutral", "hard", "heavy"]},
    {"question": "Don't ___ an American accent if it's not natural.", "correct_answer": "fake", "telugu_meaning": "సహజంగా రాకపోతే అమెరికన్ యాసను నకిలీ చేయవద్దు.", "explanation": "To pretend or imitate unnaturally.", "options": ["make", "do", "fake", "take"]},
    {"question": "___ is the rise and fall of the voice in speaking.", "correct_answer": "Intonation", "telugu_meaning": "మాట్లాడేటప్పుడు వాయిస్ పెరగడం మరియు తగ్గడాన్ని ఇంటోనేషన్ అంటారు.", "explanation": "Speech melody.", "options": ["Grammar", "Spelling", "Intonation", "Volume"]},
    {"question": "___ has an accent.", "correct_answer": "Everyone", "telugu_meaning": "ప్రతి ఒక్కరికీ యాస ఉంటుంది.", "explanation": "A universal fact.", "options": ["Nobody", "Everyone", "Someone", "Anyone"]}
]
accent_blanks = (accent_blanks * 6)[:30]

accent_speaking = [
    {"question": "He has a British accent.", "telugu_meaning": "అతనికి బ్రిటిష్ యాస ఉంది.", "explanation": "Speak clearly and neutrally."},
    {"question": "Focus on a neutral accent.", "telugu_meaning": "న్యూట్రల్ యాసపై దృష్టి పెట్టండి.", "explanation": "Emphasize 'neutral'."},
    {"question": "Intonation is very important.", "telugu_meaning": "ఇంటోనేషన్ చాలా ముఖ్యం.", "explanation": "Let your voice rise and fall naturally."},
    {"question": "Don't fake your accent.", "telugu_meaning": "మీ యాసను ఫేక్ చేయకండి.", "explanation": "Speak with a serious, advising tone."},
    {"question": "Everyone has an accent.", "telugu_meaning": "ప్రతి ఒక్కరికీ యాస ఉంటుంది.", "explanation": "State it as a simple fact."}
]
accent_speaking = (accent_speaking * 6)[:30]

def insert_level4_data(concept_name, content, rules, examples, blanks, speaking):
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

insert_level4_data('Fluency', fluency_content, fluency_rules, fluency_examples, fluency_blanks, fluency_speaking)
insert_level4_data('Pronunciation', pronunciation_content, pronunciation_rules, pronunciation_examples, pronunciation_blanks, pronunciation_speaking)
insert_level4_data('Accent', accent_content, accent_rules, accent_examples, accent_blanks, accent_speaking)
