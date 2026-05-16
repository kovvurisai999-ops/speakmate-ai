import os
import django
import sys
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

examples_data = [
    {"en": "She is a beautiful girl.", "te": "ఆమె అందమైన అమ్మాయి.", "explanation": "'beautiful' describes the noun 'girl'."},
    {"en": "He lives in a big house.", "te": "అతను పెద్ద ఇంట్లో నివసిస్తున్నాడు.", "explanation": "'big' describes the size of the house."},
    {"en": "I bought a red car.", "te": "నేను ఎరుపు రంగు కారు కొన్నాను.", "explanation": "'red' describes the color of the car."},
    {"en": "This is a heavy box.", "te": "ఇది బరువైన పెట్టె.", "explanation": "'heavy' describes the weight of the box."},
    {"en": "She has long hair.", "te": "ఆమెకు పొడవాటి జుట్టు ఉంది.", "explanation": "'long' describes the length of the hair."},
    {"en": "He is a tall man.", "te": "అతను పొడవాటి మనిషి.", "explanation": "'tall' describes the height of the man."},
    {"en": "They are happy children.", "te": "వారు సంతోషకరమైన పిల్లలు.", "explanation": "'happy' describes the emotional state."},
    {"en": "It is a hot day.", "te": "ఇది వేడి రోజు.", "explanation": "'hot' describes the temperature."},
    {"en": "The ice cream is cold.", "te": "ఐస్ క్రీమ్ చల్లగా ఉంది.", "explanation": "'cold' describes the temperature of the ice cream."},
    {"en": "He is a strong athlete.", "te": "అతను బలమైన క్రీడాకారుడు.", "explanation": "'strong' describes physical power."},
    {"en": "She gave me a sweet apple.", "te": "ఆమె నాకు తీయని ఆపిల్ ఇచ్చింది.", "explanation": "'sweet' describes the taste."},
    {"en": "The knife is sharp.", "te": "కత్తి పదునుగా ఉంది.", "explanation": "'sharp' describes the quality of the knife."},
    {"en": "This is an expensive watch.", "te": "ఇది ఖరీదైన వాచ్.", "explanation": "'expensive' describes the cost."},
    {"en": "They bought a cheap phone.", "te": "వారు చౌకైన ఫోన్ కొన్నారు.", "explanation": "'cheap' describes the cost."},
    {"en": "The old man is walking slowly.", "te": "ముసలివాడు నెమ్మదిగా నడుస్తున్నాడు.", "explanation": "'old' describes the age of the man."},
    {"en": "She bought a new dress.", "te": "ఆమె కొత్త దుస్తులు కొన్నది.", "explanation": "'new' describes the age of the dress."},
    {"en": "He is a poor farmer.", "te": "అతను పేద రైతు.", "explanation": "'poor' describes financial status."},
    {"en": "The rich merchant donated money.", "te": "ధనిక వ్యాపారి డబ్బు దానం చేశాడు.", "explanation": "'rich' describes financial status."},
    {"en": "It is a clean room.", "te": "ఇది శుభ్రమైన గది.", "explanation": "'clean' describes the condition of the room."},
    {"en": "The streets are dirty.", "te": "వీధులు మురికిగా ఉన్నాయి.", "explanation": "'dirty' describes the condition of the streets."},
    {"en": "She is wearing a beautiful ring.", "te": "ఆమె అందమైన ఉంగరం ధరించింది.", "explanation": "'beautiful' describes the ring."},
    {"en": "He is a brave soldier.", "te": "అతను ధైర్యమైన సైనికుడు.", "explanation": "'brave' describes character."},
    {"en": "The scary movie frightened me.", "te": "భయానక చిత్రం నన్ను భయపెట్టింది.", "explanation": "'scary' describes the movie."},
    {"en": "This is a soft pillow.", "te": "ఇది మృదువైన దిండు.", "explanation": "'soft' describes the texture."},
    {"en": "The rock is hard.", "te": "రాయి గట్టిగా ఉంటుంది.", "explanation": "'hard' describes the texture."},
    {"en": "I need some fresh air.", "te": "నాకు కొంచెం స్వచ్ఛమైన గాలి కావాలి.", "explanation": "'fresh' describes the air."},
    {"en": "The stale bread is tasteless.", "te": "నిల్వ ఉన్న రొట్టె రుచిలేనిది.", "explanation": "'stale' and 'tasteless' are adjectives."},
    {"en": "He is a famous actor.", "te": "అతను ప్రసిద్ధ నటుడు.", "explanation": "'famous' describes the actor."},
    {"en": "The quiet boy sat in the corner.", "te": "నిశ్శబ్ద అబ్బాయి మూలలో కూర్చున్నాడు.", "explanation": "'quiet' describes the boy's behavior."},
    {"en": "The loud music gave me a headache.", "te": "పెద్ద శబ్దంతో ఉన్న సంగీతం నాకు తలనొప్పి తెప్పించింది.", "explanation": "'loud' describes the music."},
    {"en": "She is a careful driver.", "te": "ఆమె జాగ్రత్తగా డ్రైవ్ చేసే వ్యక్తి.", "explanation": "'careful' describes how she drives."},
    {"en": "The careless mistake cost him a lot.", "te": "అజాగ్రత్త తప్పు అతనికి చాలా నష్టాన్ని కలిగించింది.", "explanation": "'careless' describes the mistake."},
    {"en": "He is an intelligent student.", "te": "అతను తెలివైన విద్యార్థి.", "explanation": "'intelligent' describes mental ability."},
    {"en": "The foolish story made everyone laugh.", "te": "తెలివితక్కువ కథ అందరినీ నవ్వించింది.", "explanation": "'foolish' describes the story."},
    {"en": "It was a difficult exam.", "te": "ఇది కష్టమైన పరీక్ష.", "explanation": "'difficult' describes the exam's level."},
    {"en": "The easy task was completed quickly.", "te": "సులభమైన పని త్వరగా పూర్తయింది.", "explanation": "'easy' describes the task."},
    {"en": "I have two dogs.", "te": "నాకు రెండు కుక్కలు ఉన్నాయి.", "explanation": "'two' is a numerical adjective."},
    {"en": "She was the first person to arrive.", "te": "ఆమె వచ్చిన మొదటి వ్యక్తి.", "explanation": "'first' is an ordinal adjective."},
    {"en": "I want some water.", "te": "నాకు కొంచెం నీరు కావాలి.", "explanation": "'some' is a quantitative adjective."},
    {"en": "There is little hope left.", "te": "కొద్ది ఆశ మాత్రమే మిగిలి ఉంది.", "explanation": "'little' is a quantitative adjective."},
    {"en": "He has much experience.", "te": "అతనికి చాలా అనుభవం ఉంది.", "explanation": "'much' describes quantity."},
    {"en": "There are many books on the shelf.", "te": "షెల్ఫ్‌లో చాలా పుస్తకాలు ఉన్నాయి.", "explanation": "'many' describes number."},
    {"en": "Every child needs love.", "te": "ప్రతి బిడ్డకు ప్రేమ అవసరం.", "explanation": "'every' is a distributive adjective."},
    {"en": "Which color do you like?", "te": "నీకు ఏ రంగు ఇష్టం?", "explanation": "'which' is an interrogative adjective."},
    {"en": "Whose bag is this?", "te": "ఈ బ్యాగ్ ఎవరిది?", "explanation": "'whose' is an interrogative adjective."},
    {"en": "This pen is mine.", "te": "ఈ పెన్ నాది.", "explanation": "'this' is a demonstrative adjective."},
    {"en": "Those birds are flying.", "te": "ఆ పక్షులు ఎగురుతున్నాయి.", "explanation": "'those' is a demonstrative adjective."},
    {"en": "My car is parked outside.", "te": "నా కారు బయట పార్క్ చేయబడింది.", "explanation": "'my' is a possessive adjective."},
    {"en": "Their house is very beautiful.", "te": "వారి ఇల్లు చాలా అందంగా ఉంటుంది.", "explanation": "'their' is a possessive adjective."},
    {"en": "He is a good boy.", "te": "అతను మంచి అబ్బాయి.", "explanation": "'good' describes the character of the boy."}
]

blanks_data = [
    {"question": "She is wearing a ___ dress.", "correct_answer": "beautiful", "telugu_meaning": "ఆమె అందమైన దుస్తులు ధరించింది.", "explanation": "Describes the appearance of the dress.", "options": ["beauty", "beautifully", "beautiful", "beautify"]},
    {"question": "The elephant is a ___ animal.", "correct_answer": "large", "telugu_meaning": "ఏనుగు పెద్ద జంతువు.", "explanation": "Describes size.", "options": ["small", "tiny", "large", "light"]},
    {"question": "I like ___ tea, not cold tea.", "correct_answer": "hot", "telugu_meaning": "నాకు వేడి టీ ఇష్టం, చల్లని టీ కాదు.", "explanation": "Describes temperature.", "options": ["hot", "ice", "freezing", "sweet"]},
    {"question": "He bought an ___ car yesterday.", "correct_answer": "expensive", "telugu_meaning": "అతను నిన్న ఖరీదైన కారు కొన్నాడు.", "explanation": "Describes price.", "options": ["expensively", "expense", "expensive", "cheaply"]},
    {"question": "This box is too ___ for me to carry.", "correct_answer": "heavy", "telugu_meaning": "ఈ పెట్టె నేను మోయలేనంత బరువుగా ఉంది.", "explanation": "Describes weight.", "options": ["heavily", "heavy", "light", "soft"]},
    {"question": "The ___ boy helped the old lady.", "correct_answer": "kind", "telugu_meaning": "దయగల అబ్బాయి వృద్ధురాలికి సహాయం చేశాడు.", "explanation": "Describes character.", "options": ["kindly", "kindness", "kind", "cruel"]},
    {"question": "She has ___ hair.", "correct_answer": "long", "telugu_meaning": "ఆమెకు పొడవాటి జుట్టు ఉంది.", "explanation": "Describes length.", "options": ["length", "long", "longly", "shortly"]},
    {"question": "The test was very ___.", "correct_answer": "difficult", "telugu_meaning": "పరీక్ష చాలా కష్టంగా ఉంది.", "explanation": "Describes the level of the test.", "options": ["difficulty", "difficult", "easy", "simply"]},
    {"question": "He is an ___ man.", "correct_answer": "old", "telugu_meaning": "అతను వృద్ధుడు.", "explanation": "Describes age.", "options": ["old", "age", "new", "youngly"]},
    {"question": "They live in a ___ house.", "correct_answer": "big", "telugu_meaning": "వారు పెద్ద ఇంట్లో నివసిస్తున్నారు.", "explanation": "Describes size.", "options": ["bigness", "big", "smallness", "tiny"]},
    {"question": "The sky is ___ today.", "correct_answer": "blue", "telugu_meaning": "ఈరోజు ఆకాశం నీలంగా ఉంది.", "explanation": "Describes color.", "options": ["blueness", "blue", "red", "darkly"]},
    {"question": "She gave me a ___ smile.", "correct_answer": "sweet", "telugu_meaning": "ఆమె నాకు తీయని చిరునవ్వు ఇచ్చింది.", "explanation": "Describes the smile.", "options": ["sweetness", "sweet", "sweetly", "sour"]},
    {"question": "I need a ___ knife to cut this.", "correct_answer": "sharp", "telugu_meaning": "దీన్ని కత్తిరించడానికి నాకు పదునైన కత్తి కావాలి.", "explanation": "Describes the edge of the knife.", "options": ["sharply", "sharpness", "sharp", "blunt"]},
    {"question": "The movie was very ___.", "correct_answer": "boring", "telugu_meaning": "సినిమా చాలా విసుగుగా ఉంది.", "explanation": "Describes the feeling given by the movie.", "options": ["bored", "boring", "bore", "interest"]},
    {"question": "He is a ___ worker.", "correct_answer": "hard", "telugu_meaning": "అతను కష్టపడి పనిచేసే వ్యక్తి.", "explanation": "Describes the worker.", "options": ["hardly", "hardness", "hard", "soft"]},
    {"question": "It is a ___ story.", "correct_answer": "true", "telugu_meaning": "ఇది నిజమైన కథ.", "explanation": "Describes the factuality.", "options": ["truth", "truly", "true", "false"]},
    {"question": "The ___ dog barked at the stranger.", "correct_answer": "angry", "telugu_meaning": "కోపంతో ఉన్న కుక్క అపరిచితుడిని చూసి అరిచింది.", "explanation": "Describes emotion.", "options": ["anger", "angrily", "angry", "happy"]},
    {"question": "This is a ___ mistake.", "correct_answer": "huge", "telugu_meaning": "ఇది చాలా పెద్ద తప్పు.", "explanation": "Describes magnitude.", "options": ["hugely", "huge", "small", "tiny"]},
    {"question": "I like ___ food.", "correct_answer": "spicy", "telugu_meaning": "నాకు కారంగా ఉండే ఆహారం ఇష్టం.", "explanation": "Describes taste.", "options": ["spice", "spicy", "sweet", "salt"]},
    {"question": "He is a ___ driver.", "correct_answer": "careful", "telugu_meaning": "అతను జాగ్రత్తగా డ్రైవ్ చేసే వ్యక్తి.", "explanation": "Describes the noun driver.", "options": ["care", "carefully", "careful", "careless"]},
    {"question": "The ___ street is empty.", "correct_answer": "dark", "telugu_meaning": "చీకటి వీధి ఖాళీగా ఉంది.", "explanation": "Describes illumination.", "options": ["darkness", "darkly", "dark", "light"], "telugu_meaning": "చీకటి వీధి ఖాళీగా ఉంది."},
    {"question": "She has ___ eyes.", "correct_answer": "brown", "telugu_meaning": "ఆమెకు గోధుమ రంగు కళ్ళు ఉన్నాయి.", "explanation": "Describes color.", "options": ["brownness", "brown", "brownly", "blue"]},
    {"question": "He is a ___ boy.", "correct_answer": "smart", "telugu_meaning": "అతను చురుకైన అబ్బాయి.", "explanation": "Describes intelligence.", "options": ["smartly", "smartness", "smart", "dumb"]},
    {"question": "I want a ___ glass of water.", "correct_answer": "clean", "telugu_meaning": "నాకు శుభ్రమైన గ్లాసు నీరు కావాలి.", "explanation": "Describes state.", "options": ["cleanly", "cleanness", "clean", "dirty"]},
    {"question": "The ___ building was demolished.", "correct_answer": "old", "telugu_meaning": "పాత భవనం కూల్చివేయబడింది.", "explanation": "Describes age.", "options": ["oldness", "old", "new", "young"]},
    {"question": "It is a ___ road.", "correct_answer": "narrow", "telugu_meaning": "ఇది ఇరుకైన రహదారి.", "explanation": "Describes width.", "options": ["narrowly", "narrow", "wide", "broad"]},
    {"question": "She is a ___ singer.", "correct_answer": "famous", "telugu_meaning": "ఆమె ప్రసిద్ధ గాయని.", "explanation": "Describes fame.", "options": ["fame", "famously", "famous", "unknown"]},
    {"question": "The ___ child cried.", "correct_answer": "hungry", "telugu_meaning": "ఆకలితో ఉన్న బిడ్డ ఏడ్చాడు.", "explanation": "Describes feeling.", "options": ["hunger", "hungrily", "hungry", "full"]},
    {"question": "This is a ___ place.", "correct_answer": "quiet", "telugu_meaning": "ఇది నిశ్శబ్దమైన ప్రదేశం.", "explanation": "Describes noise level.", "options": ["quietly", "quietness", "quiet", "loud"]},
    {"question": "He is my ___ brother.", "correct_answer": "elder", "telugu_meaning": "అతను నా అన్నయ్య.", "explanation": "Describes age relation.", "options": ["eldest", "elderly", "elder", "older"]}
]

speaking_data = [
    {"question": "She is a beautiful girl.", "telugu_meaning": "ఆమె అందమైన అమ్మాయి.", "explanation": "Emphasize 'beautiful'."},
    {"question": "It is a hot day.", "telugu_meaning": "ఇది వేడి రోజు.", "explanation": "Emphasize 'hot'."},
    {"question": "I have a new car.", "telugu_meaning": "నా దగ్గర కొత్త కారు ఉంది.", "explanation": "Emphasize 'new'."},
    {"question": "The elephant is a large animal.", "telugu_meaning": "ఏనుగు ఒక పెద్ద జంతువు.", "explanation": "Emphasize 'large'."},
    {"question": "He is an old man.", "telugu_meaning": "అతను ముసలివాడు.", "explanation": "Emphasize 'old'."},
    {"question": "She has long hair.", "telugu_meaning": "ఆమెకు పొడవాటి జుట్టు ఉంది.", "explanation": "Emphasize 'long'."},
    {"question": "This is a heavy box.", "telugu_meaning": "ఇది బరువైన పెట్టె.", "explanation": "Emphasize 'heavy'."},
    {"question": "I like sweet apples.", "telugu_meaning": "నాకు తీయని ఆపిల్స్ ఇష్టం.", "explanation": "Emphasize 'sweet'."},
    {"question": "The knife is sharp.", "telugu_meaning": "కత్తి పదునుగా ఉంది.", "explanation": "Emphasize 'sharp'."},
    {"question": "He is a rich man.", "telugu_meaning": "అతను ధనవంతుడు.", "explanation": "Emphasize 'rich'."},
    {"question": "The water is cold.", "telugu_meaning": "నీరు చల్లగా ఉంది.", "explanation": "Emphasize 'cold'."},
    {"question": "She is wearing a red dress.", "telugu_meaning": "ఆమె ఎరుపు రంగు దుస్తులు ధరించింది.", "explanation": "Emphasize 'red'."},
    {"question": "It is a small house.", "telugu_meaning": "ఇది చిన్న ఇల్లు.", "explanation": "Emphasize 'small'."},
    {"question": "He is a tall boy.", "telugu_meaning": "అతను పొడవాటి అబ్బాయి.", "explanation": "Emphasize 'tall'."},
    {"question": "They are happy children.", "telugu_meaning": "వారు సంతోషకరమైన పిల్లలు.", "explanation": "Emphasize 'happy'."},
    {"question": "The movie was scary.", "telugu_meaning": "సినిమా భయానకంగా ఉంది.", "explanation": "Emphasize 'scary'."},
    {"question": "I am tired today.", "telugu_meaning": "నేను ఈరోజు అలసిపోయాను.", "explanation": "Emphasize 'tired'."},
    {"question": "The room is clean.", "telugu_meaning": "గది శుభ్రంగా ఉంది.", "explanation": "Emphasize 'clean'."},
    {"question": "He is a brave soldier.", "telugu_meaning": "అతను ధైర్యమైన సైనికుడు.", "explanation": "Emphasize 'brave'."},
    {"question": "This is a cheap phone.", "telugu_meaning": "ఇది చౌకైన ఫోన్.", "explanation": "Emphasize 'cheap'."},
    {"question": "The streets are dirty.", "telugu_meaning": "వీధులు మురికిగా ఉన్నాయి.", "explanation": "Emphasize 'dirty'."},
    {"question": "She is an intelligent student.", "telugu_meaning": "ఆమె తెలివైన విద్యార్థిని.", "explanation": "Emphasize 'intelligent'."},
    {"question": "It was a difficult exam.", "telugu_meaning": "ఇది కష్టమైన పరీక్ష.", "explanation": "Emphasize 'difficult'."},
    {"question": "The task was easy.", "telugu_meaning": "పని సులభంగా ఉంది.", "explanation": "Emphasize 'easy'."},
    {"question": "He has a soft pillow.", "telugu_meaning": "అతనికి మృదువైన దిండు ఉంది.", "explanation": "Emphasize 'soft'."},
    {"question": "The rock is hard.", "telugu_meaning": "రాయి గట్టిగా ఉంది.", "explanation": "Emphasize 'hard'."},
    {"question": "I need some fresh air.", "telugu_meaning": "నాకు స్వచ్ఛమైన గాలి కావాలి.", "explanation": "Emphasize 'fresh'."},
    {"question": "He is a famous actor.", "telugu_meaning": "అతను ప్రసిద్ధ నటుడు.", "explanation": "Emphasize 'famous'."},
    {"question": "The quiet boy sat there.", "telugu_meaning": "నిశ్శబ్ద అబ్బాయి అక్కడ కూర్చున్నాడు.", "explanation": "Emphasize 'quiet'."},
    {"question": "The music is loud.", "telugu_meaning": "సంగీతం పెద్దగా ఉంది.", "explanation": "Emphasize 'loud'."}
]

concept = Concept.objects.filter(name='Adjectives').first()
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
    print("Adjectives completed successfully.")
else:
    print("Concept 'Adjectives' not found.")
