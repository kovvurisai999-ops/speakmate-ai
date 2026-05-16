import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

examples_data = [
    {"en": "He runs fast.", "te": "అతను వేగంగా పరిగెత్తుతాడు.", "explanation": "'fast' describes how he runs."},
    {"en": "She sings beautifully.", "te": "ఆమె అందంగా పాడుతుంది.", "explanation": "'beautifully' describes how she sings."},
    {"en": "They walked slowly.", "te": "వారు నెమ్మదిగా నడిచారు.", "explanation": "'slowly' describes how they walked."},
    {"en": "He spoke loudly.", "te": "అతను గట్టిగా మాట్లాడాడు.", "explanation": "'loudly' describes how he spoke."},
    {"en": "She works hard.", "te": "ఆమె కష్టపడి పనిచేస్తుంది.", "explanation": "'hard' describes how she works."},
    {"en": "The boy cried bitterly.", "te": "అబ్బాయి వెక్కి వెక్కి ఏడ్చాడు.", "explanation": "'bitterly' describes how he cried."},
    {"en": "He drives carefully.", "te": "అతను జాగ్రత్తగా డ్రైవ్ చేస్తాడు.", "explanation": "'carefully' describes how he drives."},
    {"en": "She answered correctly.", "te": "ఆమె సరిగ్గా సమాధానం చెప్పింది.", "explanation": "'correctly' describes how she answered."},
    {"en": "The sun shines brightly.", "te": "సూర్యుడు ప్రకాశవంతంగా మెరుస్తున్నాడు.", "explanation": "'brightly' describes how it shines."},
    {"en": "He treated me kindly.", "te": "అతను నాతో దయగా ప్రవర్తించాడు.", "explanation": "'kindly' describes how he treated."},
    {"en": "They won easily.", "te": "వారు సులభంగా గెలిచారు.", "explanation": "'easily' describes how they won."},
    {"en": "She waited patiently.", "te": "ఆమె ఓపికగా వేచి ఉంది.", "explanation": "'patiently' describes how she waited."},
    {"en": "He arrived late.", "te": "అతను ఆలస్యంగా వచ్చాడు.", "explanation": "'late' describes when he arrived."},
    {"en": "She gets up early.", "te": "ఆమె త్వరగా నిద్రలేస్తుంది.", "explanation": "'early' describes when she gets up."},
    {"en": "I will do it now.", "te": "నేను దానిని ఇప్పుడు చేస్తాను.", "explanation": "'now' describes when."},
    {"en": "He went yesterday.", "te": "అతను నిన్న వెళ్ళాడు.", "explanation": "'yesterday' describes when."},
    {"en": "They will come tomorrow.", "te": "వారు రేపు వస్తారు.", "explanation": "'tomorrow' describes when."},
    {"en": "I have seen him before.", "te": "నేను అతనిని ఇంతకు ముందు చూశాను.", "explanation": "'before' describes when."},
    {"en": "She will arrive soon.", "te": "ఆమె త్వరలో వస్తుంది.", "explanation": "'soon' describes when."},
    {"en": "He is coming today.", "te": "అతను ఈరోజు వస్తున్నాడు.", "explanation": "'today' describes when."},
    {"en": "I will speak to him later.", "te": "నేను అతనితో తర్వాత మాట్లాడుతాను.", "explanation": "'later' describes when."},
    {"en": "Please come here.", "te": "దయచేసి ఇక్కడికి రండి.", "explanation": "'here' describes where."},
    {"en": "He went there.", "te": "అతను అక్కడికి వెళ్ళాడు.", "explanation": "'there' describes where."},
    {"en": "Look up.", "te": "పైకి చూడు.", "explanation": "'up' describes where."},
    {"en": "Please sit down.", "te": "దయచేసి కూర్చోండి.", "explanation": "'down' describes where."},
    {"en": "He lives inside.", "te": "అతను లోపల నివసిస్తున్నాడు.", "explanation": "'inside' describes where."},
    {"en": "Wait outside.", "te": "బయట వేచి ఉండండి.", "explanation": "'outside' describes where."},
    {"en": "He looked everywhere.", "te": "అతను అన్ని చోట్లా వెతికాడు.", "explanation": "'everywhere' describes where."},
    {"en": "They went nowhere.", "te": "వారు ఎక్కడికీ వెళ్ళలేదు.", "explanation": "'nowhere' describes where."},
    {"en": "I am fully prepared.", "te": "నేను పూర్తిగా సిద్ధంగా ఉన్నాను.", "explanation": "'fully' describes the degree of preparation."},
    {"en": "He is very tired.", "te": "అతను చాలా అలసిపోయాడు.", "explanation": "'very' describes the degree of tiredness."},
    {"en": "She is almost ready.", "te": "ఆమె దాదాపు సిద్ధంగా ఉంది.", "explanation": "'almost' describes the degree."},
    {"en": "It is quite cold.", "te": "ఇది చాలా చల్లగా ఉంది.", "explanation": "'quite' describes the degree."},
    {"en": "He was completely exhausted.", "te": "అతను పూర్తిగా అలసిపోయాడు.", "explanation": "'completely' describes the degree."},
    {"en": "I partly agree with you.", "te": "నేను మీతో పాక్షికంగా ఏకీభవిస్తున్నాను.", "explanation": "'partly' describes the degree."},
    {"en": "This is too hot.", "te": "ఇది చాలా వేడిగా ఉంది.", "explanation": "'too' describes excessive degree."},
    {"en": "I often visit them.", "te": "నేను తరచుగా వారిని కలుస్తాను.", "explanation": "'often' describes frequency."},
    {"en": "He never tells a lie.", "te": "అతను ఎప్పుడూ అబద్ధం చెప్పడు.", "explanation": "'never' describes frequency."},
    {"en": "She always speaks the truth.", "te": "ఆమె ఎల్లప్పుడూ నిజం చెబుతుంది.", "explanation": "'always' describes frequency."},
    {"en": "I sometimes go to the cinema.", "te": "నేను కొన్నిసార్లు సినిమాకు వెళ్తాను.", "explanation": "'sometimes' describes frequency."},
    {"en": "They rarely come here.", "te": "వారు అరుదుగా ఇక్కడికి వస్తారు.", "explanation": "'rarely' describes frequency."},
    {"en": "He visits us occasionally.", "te": "అతను అప్పుడప్పుడు మమ్మల్ని కలుస్తాడు.", "explanation": "'occasionally' describes frequency."},
    {"en": "I have called him twice.", "te": "నేను అతనికి రెండుసార్లు కాల్ చేశాను.", "explanation": "'twice' describes frequency."},
    {"en": "He came once.", "te": "అతను ఒకసారి వచ్చాడు.", "explanation": "'once' describes frequency."},
    {"en": "Why are you crying?", "te": "నువ్వు ఎందుకు ఏడుస్తున్నావు?", "explanation": "'why' is an interrogative adverb."},
    {"en": "Where do you live?", "te": "నువ్వు ఎక్కడ నివసిస్తున్నావు?", "explanation": "'where' is an interrogative adverb."},
    {"en": "When will you come?", "te": "నువ్వు ఎప్పుడు వస్తావు?", "explanation": "'when' is an interrogative adverb."},
    {"en": "How did you do it?", "te": "నువ్వు దీన్ని ఎలా చేశావు?", "explanation": "'how' is an interrogative adverb."},
    {"en": "Therefore, I left.", "te": "అందువల్ల, నేను వెళ్ళిపోయాను.", "explanation": "'therefore' is a conjunctive adverb."},
    {"en": "He worked hard; thus, he succeeded.", "te": "అతను కష్టపడి పనిచేశాడు; అందువలన, అతను విజయం సాధించాడు.", "explanation": "'thus' is a conjunctive adverb."}
]

blanks_data = [
    {"question": "He runs very ___.", "correct_answer": "fast", "telugu_meaning": "అతను చాలా వేగంగా పరిగెత్తుతాడు.", "explanation": "Describes how he runs. 'Fastly' is not a word.", "options": ["fastly", "fast", "quick", "faster"]},
    {"question": "She speaks English ___.", "correct_answer": "fluently", "telugu_meaning": "ఆమె ఇంగ్లీష్ అనర్గళంగా మాట్లాడుతుంది.", "explanation": "Adverb modifying 'speaks'.", "options": ["fluent", "fluently", "fluency", "fast"]},
    {"question": "They waited ___ for the train.", "correct_answer": "patiently", "telugu_meaning": "వారు రైలు కోసం ఓపికగా వేచి ఉన్నారు.", "explanation": "Describes the manner of waiting.", "options": ["patient", "patience", "patiently", "calm"]},
    {"question": "He answered all the questions ___.", "correct_answer": "correctly", "telugu_meaning": "అతను అన్ని ప్రశ్నలకు సరిగ్గా సమాధానం చెప్పాడు.", "explanation": "Describes how he answered.", "options": ["correct", "correctly", "correction", "right"]},
    {"question": "The sun is shining ___.", "correct_answer": "brightly", "telugu_meaning": "సూర్యుడు ప్రకాశవంతంగా మెరుస్తున్నాడు.", "explanation": "Adverb modifying 'shining'.", "options": ["bright", "brightly", "brightness", "light"]},
    {"question": "She sings very ___.", "correct_answer": "beautifully", "telugu_meaning": "ఆమె చాలా అందంగా పాడుతుంది.", "explanation": "Describes how she sings.", "options": ["beautiful", "beauty", "beautifully", "good"]},
    {"question": "He drives ___.", "correct_answer": "carefully", "telugu_meaning": "అతను జాగ్రత్తగా డ్రైవ్ చేస్తాడు.", "explanation": "Describes the manner of driving.", "options": ["careful", "carefully", "care", "safe"]},
    {"question": "I completely ___ with you.", "correct_answer": "agree", "telugu_meaning": "నేను మీతో పూర్తిగా ఏకీభవిస్తున్నాను.", "explanation": "'Completely' modifies 'agree'.", "options": ["agree", "agrees", "agreement", "agreed"]},
    {"question": "She was ___ exhausted after work.", "correct_answer": "completely", "telugu_meaning": "పని తర్వాత ఆమె పూర్తిగా అలసిపోయింది.", "explanation": "Adverb of degree.", "options": ["complete", "completeness", "completely", "full"]},
    {"question": "He is ___ late for the meeting.", "correct_answer": "always", "telugu_meaning": "అతను మీటింగ్‌కు ఎల్లప్పుడూ ఆలస్యంగా వస్తాడు.", "explanation": "Adverb of frequency.", "options": ["always", "sometime", "rare", "neverly"]},
    {"question": "I have ___ finished my homework.", "correct_answer": "almost", "telugu_meaning": "నేను నా హోంవర్క్ దాదాపు పూర్తి చేశాను.", "explanation": "Adverb of degree.", "options": ["almost", "most", "nearlyly", "fast"]},
    {"question": "They play football ___.", "correct_answer": "often", "telugu_meaning": "వారు తరచుగా ఫుట్‌బాల్ ఆడుతారు.", "explanation": "Adverb of frequency.", "options": ["often", "oftenly", "much", "many"]},
    {"question": "He will come ___.", "correct_answer": "tomorrow", "telugu_meaning": "అతను రేపు వస్తాడు.", "explanation": "Adverb of time.", "options": ["tomorrow", "yesterday", "before", "next"]},
    {"question": "I saw him ___.", "correct_answer": "yesterday", "telugu_meaning": "నేను నిన్న అతన్ని చూశాను.", "explanation": "Adverb of time.", "options": ["tomorrow", "yesterday", "soon", "now"]},
    {"question": "Please put the box ___.", "correct_answer": "there", "telugu_meaning": "దయచేసి పెట్టెను అక్కడ పెట్టండి.", "explanation": "Adverb of place.", "options": ["their", "they're", "there", "then"]},
    {"question": "Come ___ immediately.", "correct_answer": "here", "telugu_meaning": "వెంటనే ఇక్కడికి రా.", "explanation": "Adverb of place.", "options": ["hear", "here", "their", "there"]},
    {"question": "He went ___ to sleep.", "correct_answer": "upstairs", "telugu_meaning": "అతను నిద్రపోవడానికి పైకి వెళ్ళాడు.", "explanation": "Adverb of place.", "options": ["upstairs", "upstair", "up", "upper"]},
    {"question": "I have seen this movie ___.", "correct_answer": "before", "telugu_meaning": "నేను ఇంతకు ముందే ఈ సినిమా చూశాను.", "explanation": "Adverb of time.", "options": ["after", "before", "ago", "since"]},
    {"question": "She spoke to him ___.", "correct_answer": "angrily", "telugu_meaning": "ఆమె అతనితో కోపంగా మాట్లాడింది.", "explanation": "Adverb of manner.", "options": ["angry", "angrily", "anger", "mad"]},
    {"question": "He laughed ___ at the joke.", "correct_answer": "loudly", "telugu_meaning": "జోక్‌కి అతను గట్టిగా నవ్వాడు.", "explanation": "Adverb of manner.", "options": ["loud", "loudly", "noise", "loudness"]},
    {"question": "The baby is sleeping ___.", "correct_answer": "peacefully", "telugu_meaning": "బిడ్డ ప్రశాంతంగా నిద్రపోతున్నాడు.", "explanation": "Adverb of manner.", "options": ["peaceful", "peace", "peacefully", "quiet"]},
    {"question": "She works very ___.", "correct_answer": "hard", "telugu_meaning": "ఆమె చాలా కష్టపడి పనిచేస్తుంది.", "explanation": "'Hard' is the adverb form. 'Hardly' means 'barely'.", "options": ["hardly", "hard", "hardness", "tough"]},
    {"question": "I can ___ hear you.", "correct_answer": "hardly", "telugu_meaning": "నేను మీరు చెప్పేది అస్సలు వినలేకపోతున్నాను.", "explanation": "'Hardly' means barely.", "options": ["hardly", "hard", "tough", "fast"]},
    {"question": "He completed the test ___.", "correct_answer": "quickly", "telugu_meaning": "అతను పరీక్షను త్వరగా పూర్తి చేశాడు.", "explanation": "Adverb of manner.", "options": ["quick", "quickly", "fastly", "speed"]},
    {"question": "They are ___ happy with the result.", "correct_answer": "very", "telugu_meaning": "వారు ఫలితంతో చాలా సంతోషంగా ఉన్నారు.", "explanation": "Adverb of degree.", "options": ["much", "very", "too", "so"]},
    {"question": "The soup is ___ hot to eat.", "correct_answer": "too", "telugu_meaning": "సూప్ తినలేనంత వేడిగా ఉంది.", "explanation": "'Too' means excessively.", "options": ["to", "too", "two", "very"]},
    {"question": "I am ___ tired today.", "correct_answer": "quite", "telugu_meaning": "నేను ఈరోజు చాలా అలసిపోయాను.", "explanation": "Adverb of degree.", "options": ["quiet", "quite", "quit", "very"]},
    {"question": "He solved the puzzle ___.", "correct_answer": "easily", "telugu_meaning": "అతను పజిల్‌ను సులభంగా పరిష్కరించాడు.", "explanation": "Adverb of manner.", "options": ["easy", "easily", "easiness", "simple"]},
    {"question": "She dances ___ well.", "correct_answer": "extremely", "telugu_meaning": "ఆమె అద్భుతంగా డాన్స్ చేస్తుంది.", "explanation": "Adverb of degree.", "options": ["extreme", "extremely", "much", "very"], "telugu_meaning": "ఆమె చాలా అద్భుతంగా డాన్స్ చేస్తుంది."},
    {"question": "I have ___ been to Paris.", "correct_answer": "never", "telugu_meaning": "నేను ఎప్పుడూ పారిస్ వెళ్ళలేదు.", "explanation": "Adverb of frequency.", "options": ["ever", "never", "always", "sometimes"]}
]

speaking_data = [
    {"question": "He runs very fast.", "telugu_meaning": "అతను చాలా వేగంగా పరిగెత్తుతాడు.", "explanation": "Focus on 'fast' as an adverb."},
    {"question": "She sings beautifully.", "telugu_meaning": "ఆమె అందంగా పాడుతుంది.", "explanation": "Focus on the ending '-ly' in beautifully."},
    {"question": "They walked slowly.", "telugu_meaning": "వారు నెమ్మదిగా నడిచారు.", "explanation": "Emphasize 'slowly'."},
    {"question": "He spoke loudly.", "telugu_meaning": "అతను గట్టిగా మాట్లాడాడు.", "explanation": "Emphasize 'loudly'."},
    {"question": "She works hard.", "telugu_meaning": "ఆమె కష్టపడి పనిచేస్తుంది.", "explanation": "Remember 'hard' is the adverb, not 'hardly'."},
    {"question": "The baby slept peacefully.", "telugu_meaning": "బిడ్డ ప్రశాంతంగా నిద్రపోయాడు.", "explanation": "Emphasize 'peacefully'."},
    {"question": "He drives carefully.", "telugu_meaning": "అతను జాగ్రత్తగా డ్రైవ్ చేస్తాడు.", "explanation": "Emphasize 'carefully'."},
    {"question": "She answered correctly.", "telugu_meaning": "ఆమె సరిగ్గా సమాధానం చెప్పింది.", "explanation": "Emphasize 'correctly'."},
    {"question": "I will do it now.", "telugu_meaning": "నేను దానిని ఇప్పుడు చేస్తాను.", "explanation": "Focus on the adverb of time 'now'."},
    {"question": "He went yesterday.", "telugu_meaning": "అతను నిన్న వెళ్ళాడు.", "explanation": "Focus on 'yesterday'."},
    {"question": "Please come here.", "telugu_meaning": "దయచేసి ఇక్కడికి రండి.", "explanation": "Focus on 'here'."},
    {"question": "He went there.", "telugu_meaning": "అతను అక్కడికి వెళ్ళాడు.", "explanation": "Focus on 'there'."},
    {"question": "Look up.", "telugu_meaning": "పైకి చూడు.", "explanation": "Focus on 'up'."},
    {"question": "Please sit down.", "telugu_meaning": "దయచేసి కూర్చోండి.", "explanation": "Focus on 'down'."},
    {"question": "He is very tired.", "telugu_meaning": "అతను చాలా అలసిపోయాడు.", "explanation": "Focus on 'very'."},
    {"question": "She is almost ready.", "telugu_meaning": "ఆమె దాదాపు సిద్ధంగా ఉంది.", "explanation": "Focus on 'almost'."},
    {"question": "This is too hot.", "telugu_meaning": "ఇది చాలా వేడిగా ఉంది.", "explanation": "Focus on 'too'."},
    {"question": "I often visit them.", "telugu_meaning": "నేను తరచుగా వారిని కలుస్తాను.", "explanation": "Focus on 'often'."},
    {"question": "He never tells a lie.", "telugu_meaning": "అతను ఎప్పుడూ అబద్ధం చెప్పడు.", "explanation": "Focus on 'never'."},
    {"question": "She always speaks the truth.", "telugu_meaning": "ఆమె ఎల్లప్పుడూ నిజం చెబుతుంది.", "explanation": "Focus on 'always'."},
    {"question": "I sometimes go to the cinema.", "telugu_meaning": "నేను కొన్నిసార్లు సినిమాకు వెళ్తాను.", "explanation": "Focus on 'sometimes'."},
    {"question": "Where do you live?", "telugu_meaning": "నువ్వు ఎక్కడ నివసిస్తున్నావు?", "explanation": "Focus on 'where'."},
    {"question": "When will you come?", "telugu_meaning": "నువ్వు ఎప్పుడు వస్తావు?", "explanation": "Focus on 'when'."},
    {"question": "How did you do it?", "telugu_meaning": "నువ్వు దీన్ని ఎలా చేశావు?", "explanation": "Focus on 'how'."},
    {"question": "He solved it easily.", "telugu_meaning": "అతను దాన్ని సులభంగా పరిష్కరించాడు.", "explanation": "Focus on 'easily'."},
    {"question": "She arrived late.", "telugu_meaning": "ఆమె ఆలస్యంగా వచ్చింది.", "explanation": "Focus on 'late'."},
    {"question": "He gets up early.", "telugu_meaning": "అతను త్వరగా నిద్రలేస్తాడు.", "explanation": "Focus on 'early'."},
    {"question": "They play outside.", "telugu_meaning": "వారు బయట ఆడుకుంటారు.", "explanation": "Focus on 'outside'."},
    {"question": "Stay inside.", "telugu_meaning": "లోపలే ఉండు.", "explanation": "Focus on 'inside'."},
    {"question": "I agree completely.", "telugu_meaning": "నేను పూర్తిగా ఏకీభవిస్తున్నాను.", "explanation": "Focus on 'completely'."}
]

concept = Concept.objects.filter(name='Adverbs').first()
if concept:
    concept.examples = examples_data
    concept.save()
    
    Exercise.objects.filter(concept=concept, type='FILL_BLANK').delete()
    Exercise.objects.filter(concept=concept, type='READ_ALOUD').delete()
    
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
    print("Adverbs completed successfully.")
else:
    print("Concept 'Adverbs' not found.")
