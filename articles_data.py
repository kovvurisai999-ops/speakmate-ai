import os
import django
import sys
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

examples_data = [
    {"en": "I saw a cat on the roof.", "te": "నేను పైకప్పు మీద ఒక పిల్లిని చూశాను.", "explanation": "We use 'a' for a singular, non-specific consonant-sounding noun."},
    {"en": "She ate an apple.", "te": "ఆమె ఒక ఆపిల్ తింది.", "explanation": "We use 'an' before a vowel-sounding noun."},
    {"en": "The sun rises in the east.", "te": "సూర్యుడు తూర్పున ఉదయిస్తాడు.", "explanation": "We use 'the' for unique objects like sun and directions like east."},
    {"en": "He bought a new car.", "te": "అతను కొత్త కారు కొన్నాడు.", "explanation": "Using 'a' for introducing a non-specific noun for the first time."},
    {"en": "The car he bought is red.", "te": "అతను కొన్న కారు ఎరుపు రంగులో ఉంది.", "explanation": "Using 'the' because the car is now specific (the one he bought)."},
    {"en": "I need an umbrella.", "te": "నాకు ఒక గొడుగు కావాలి.", "explanation": "Starts with a vowel sound 'u'."},
    {"en": "She is a university student.", "te": "ఆమె ఒక విశ్వవిద్యాలయ విద్యార్థిని.", "explanation": "Starts with a consonant sound 'yu' despite the vowel letter 'u'."},
    {"en": "It takes an hour to reach.", "te": "చేరుకోవడానికి ఒక గంట పడుతుంది.", "explanation": "The 'h' in hour is silent, so it starts with a vowel sound."},
    {"en": "He is an honest man.", "te": "అతను నిజాయితీగల వ్యక్తి.", "explanation": "The 'h' is silent, so 'an' is used."},
    {"en": "Can you pass the salt?", "te": "మీరు ఉప్పు అందించగలరా?", "explanation": "Both speaker and listener know which salt is meant, so 'the' is used."},
    {"en": "I want a dog.", "te": "నాకు ఒక కుక్క కావాలి.", "explanation": "General desire for any dog."},
    {"en": "The dog is barking.", "te": "ఆ కుక్క అరుస్తోంది.", "explanation": "Referring to a specific dog that is currently barking."},
    {"en": "We visited the Taj Mahal.", "te": "మేము తాజ్ మహల్ సందర్శించాము.", "explanation": "Use 'the' before famous monuments."},
    {"en": "He is the best player.", "te": "అతను ఉత్తమ ఆటగాడు.", "explanation": "Use 'the' before superlative adjectives like 'best'."},
    {"en": "I live in a small town.", "te": "నేను ఒక చిన్న పట్టణంలో నివసిస్తున్నాను.", "explanation": "General, non-specific town."},
    {"en": "The town where I live is beautiful.", "te": "నేను నివసించే పట్టణం చాలా అందంగా ఉంటుంది.", "explanation": "Specific town now."},
    {"en": "She plays the piano.", "te": "ఆమె పియానో వాయిస్తుంది.", "explanation": "Use 'the' before musical instruments."},
    {"en": "He is a doctor.", "te": "అతను ఒక డాక్టర్.", "explanation": "Use 'a' or 'an' to state someone's profession."},
    {"en": "I read a book yesterday.", "te": "నేను నిన్న ఒక పుస్తకం చదివాను.", "explanation": "Any non-specific book."},
    {"en": "The book was very interesting.", "te": "ఆ పుస్తకం చాలా ఆసక్తికరంగా ఉంది.", "explanation": "Referring back to the specific book mentioned earlier."},
    {"en": "They live near the river Ganges.", "te": "వారు గంగా నదికి సమీపంలో నివసిస్తున్నారు.", "explanation": "Use 'the' before river names."},
    {"en": "A bird is flying.", "te": "ఒక పక్షి ఎగురుతోంది.", "explanation": "General statement about a bird."},
    {"en": "An elephant is a large animal.", "te": "ఏనుగు ఒక పెద్ద జంతువు.", "explanation": "General statement using 'an' before a vowel."},
    {"en": "The Earth moves around the Sun.", "te": "భూమి సూర్యుని చుట్టూ తిరుగుతుంది.", "explanation": "Unique astronomical bodies take 'the'."},
    {"en": "Give me a pen.", "te": "నాకు ఒక పెన్ ఇవ్వు.", "explanation": "Any pen will do."},
    {"en": "Give me the red pen.", "te": "నాకు ఎరుపు రంగు పెన్ ఇవ్వు.", "explanation": "Asking for a specific pen."},
    {"en": "I met a European tourist.", "te": "నేను ఒక యూరోపియన్ పర్యాటకుడిని కలిశాను.", "explanation": "European starts with a 'yu' consonant sound, so 'a' is used."},
    {"en": "He has a one-rupee coin.", "te": "అతని వద్ద ఒక రూపాయి నాణెం ఉంది.", "explanation": "One starts with a 'wa' consonant sound, so 'a' is used."},
    {"en": "She is an MLA.", "te": "ఆమె ఒక ఎమ్మెల్యే.", "explanation": "MLA starts with the vowel sound 'em', so 'an' is used."},
    {"en": "The rich should help the poor.", "te": "ధనవంతులు పేదలకు సహాయం చేయాలి.", "explanation": "Use 'the' before adjectives to refer to a whole class of people."},
    {"en": "Look at the moon.", "te": "చంద్రుడి వైపు చూడు.", "explanation": "Unique object in the sky."},
    {"en": "I need a glass of water.", "te": "నాకు ఒక గ్లాసు నీరు కావాలి.", "explanation": "Counting the glass, not the water."},
    {"en": "He works in an office.", "te": "అతను ఒక ఆఫీసులో పనిచేస్తాడు.", "explanation": "Starts with a vowel sound."},
    {"en": "The office is near my house.", "te": "ఆఫీసు నా ఇంటికి సమీపంలో ఉంది.", "explanation": "Referring to the specific office."},
    {"en": "I watched a movie last night.", "te": "నేను నిన్న రాత్రి ఒక సినిమా చూశాను.", "explanation": "Introducing a non-specific movie."},
    {"en": "The movie was amazing.", "te": "సినిమా అద్భుతంగా ఉంది.", "explanation": "Referring to the movie just mentioned."},
    {"en": "An apple a day keeps the doctor away.", "te": "రోజుకు ఒక ఆపిల్ తింటే డాక్టర్ అవసరం ఉండదు.", "explanation": "General saying using both indefinite and definite articles."},
    {"en": "We stayed at a hotel.", "te": "మేము ఒక హోటల్‌లో బస చేసాము.", "explanation": "Any hotel."},
    {"en": "The hotel was very expensive.", "te": "ఆ హోటల్ చాలా ఖరీదైనది.", "explanation": "The specific hotel they stayed at."},
    {"en": "He is learning to play the guitar.", "te": "అతను గిటార్ వాయించడం నేర్చుకుంటున్నాడు.", "explanation": "Musical instruments take 'the'."},
    {"en": "I have an idea.", "te": "నాకు ఒక ఆలోచన ఉంది.", "explanation": "Starts with a vowel sound."},
    {"en": "The idea is brilliant.", "te": "ఆ ఆలోచన అద్భుతంగా ఉంది.", "explanation": "Specific idea just mentioned."},
    {"en": "She is wearing a blue dress.", "te": "ఆమె నీలిరంగు దుస్తులు ధరించింది.", "explanation": "Describing clothing generally."},
    {"en": "The dress looks great on her.", "te": "ఆ దుస్తులు ఆమెకు చాలా బాగున్నాయి.", "explanation": "The specific dress she is wearing."},
    {"en": "I saw an old man.", "te": "నేను ఒక ముసలివాడిని చూశాను.", "explanation": "Vowel sound 'o'."},
    {"en": "The old man was crossing the road.", "te": "ఆ ముసలివాడు రోడ్డు దాటుతున్నాడు.", "explanation": "Specific old man."},
    {"en": "It is a beautiful day.", "te": "ఇది ఒక అందమైన రోజు.", "explanation": "General description."},
    {"en": "The day we met was rainy.", "te": "మనం కలిసిన రోజు వర్షం పడుతోంది.", "explanation": "A very specific day in the past."},
    {"en": "He is the only son of his parents.", "te": "అతను తన తల్లిదండ్రులకు ఏకైక కుమారుడు.", "explanation": "'The only' is a specific phrase indicating uniqueness."},
    {"en": "Let's go to the beach.", "te": "బీచ్‌కి వెళ్దాం.", "explanation": "Specific common location known to both."}
]

blanks_data = [
    {"question": "I saw ___ elephant in the zoo.", "correct_answer": "an", "telugu_meaning": "నేను జూలో ఒక ఏనుగును చూశాను.", "explanation": "Elephant starts with a vowel sound.", "options": ["a", "an", "the", "no article"]},
    {"question": "___ sun is very hot today.", "correct_answer": "The", "telugu_meaning": "ఈ రోజు సూర్యుడు చాలా వేడిగా ఉన్నాడు.", "explanation": "Sun is a unique object, so we use 'The'.", "options": ["A", "An", "The", "no article"]},
    {"question": "She wants to become ___ engineer.", "correct_answer": "an", "telugu_meaning": "ఆమె ఇంజనీర్ అవ్వాలనుకుంటోంది.", "explanation": "Engineer starts with a vowel sound.", "options": ["a", "an", "the", "no article"]},
    {"question": "He bought ___ new phone.", "correct_answer": "a", "telugu_meaning": "అతను కొత్త ఫోన్ కొన్నాడు.", "explanation": "New starts with a consonant sound.", "options": ["a", "an", "the", "no article"]},
    {"question": "Where is ___ book I gave you?", "correct_answer": "the", "telugu_meaning": "నేను నీకు ఇచ్చిన పుస్తకం ఎక్కడ ఉంది?", "explanation": "Referring to a specific book.", "options": ["a", "an", "the", "no article"]},
    {"question": "It takes ___ hour to complete this.", "correct_answer": "an", "telugu_meaning": "దీన్ని పూర్తి చేయడానికి ఒక గంట పడుతుంది.", "explanation": "Hour starts with a vowel sound (silent h).", "options": ["a", "an", "the", "no article"]},
    {"question": "She goes to ___ university in London.", "correct_answer": "a", "telugu_meaning": "ఆమె లండన్‌లోని ఒక విశ్వవిద్యాలయానికి వెళుతుంది.", "explanation": "University starts with a consonant 'y' sound.", "options": ["a", "an", "the", "no article"]},
    {"question": "I need ___ umbrella because it's raining.", "correct_answer": "an", "telugu_meaning": "వర్షం పడుతోంది కాబట్టి నాకు గొడుగు కావాలి.", "explanation": "Umbrella starts with a vowel sound.", "options": ["a", "an", "the", "no article"]},
    {"question": "___ Earth is round.", "correct_answer": "The", "telugu_meaning": "భూమి గుండ్రంగా ఉంటుంది.", "explanation": "Earth is a unique planet.", "options": ["A", "An", "The", "no article"]},
    {"question": "He is ___ tallest boy in the class.", "correct_answer": "the", "telugu_meaning": "అతను క్లాస్‌లో అందరికంటే పొడవైన అబ్బాయి.", "explanation": "Superlative degree (tallest) takes 'the'.", "options": ["a", "an", "the", "no article"]},
    {"question": "I want to eat ___ apple.", "correct_answer": "an", "telugu_meaning": "నేను ఒక ఆపిల్ తినాలనుకుంటున్నాను.", "explanation": "Apple starts with a vowel sound.", "options": ["a", "an", "the", "no article"]},
    {"question": "That is ___ cat.", "correct_answer": "a", "telugu_meaning": "అది ఒక పిల్లి.", "explanation": "Cat starts with a consonant sound.", "options": ["a", "an", "the", "no article"]},
    {"question": "Did you see ___ moon last night?", "correct_answer": "the", "telugu_meaning": "నువ్వు నిన్న రాత్రి చంద్రుడిని చూశావా?", "explanation": "Moon is a unique object.", "options": ["a", "an", "the", "no article"]},
    {"question": "I met ___ European man.", "correct_answer": "a", "telugu_meaning": "నేను ఒక యూరోపియన్ వ్యక్తిని కలిశాను.", "explanation": "European starts with a 'y' consonant sound.", "options": ["a", "an", "the", "no article"]},
    {"question": "He gave me ___ one-rupee coin.", "correct_answer": "a", "telugu_meaning": "అతను నాకు ఒక రూపాయి నాణెం ఇచ్చాడు.", "explanation": "One starts with a 'w' consonant sound.", "options": ["a", "an", "the", "no article"]},
    {"question": "She is ___ honest woman.", "correct_answer": "an", "telugu_meaning": "ఆమె నిజాయితీగల మహిళ.", "explanation": "Honest starts with a vowel sound (silent h).", "options": ["a", "an", "the", "no article"]},
    {"question": "___ Taj Mahal is in Agra.", "correct_answer": "The", "telugu_meaning": "తాజ్ మహల్ ఆగ్రాలో ఉంది.", "explanation": "Famous monuments take 'The'.", "options": ["A", "An", "The", "no article"]},
    {"question": "He plays ___ guitar well.", "correct_answer": "the", "telugu_meaning": "అతను గిటార్ బాగా వాయిస్తాడు.", "explanation": "Musical instruments take 'the'.", "options": ["a", "an", "the", "no article"]},
    {"question": "___ dogs are barking.", "correct_answer": "The", "telugu_meaning": "కుక్కలు అరుస్తున్నాయి.", "explanation": "Specific dogs that are barking right now.", "options": ["A", "An", "The", "no article"]},
    {"question": "I have ___ dog and ___ cat.", "correct_answer": "a", "telugu_meaning": "నాకు ఒక కుక్క మరియు ఒక పిల్లి ఉన్నాయి.", "explanation": "Introducing them for the first time.", "options": ["the", "an", "a", "no article"]},
    {"question": "My father is ___ doctor.", "correct_answer": "a", "telugu_meaning": "మా నాన్న డాక్టర్.", "explanation": "Professions take 'a' or 'an'.", "options": ["a", "an", "the", "no article"]},
    {"question": "Can you open ___ door?", "correct_answer": "the", "telugu_meaning": "తలుపు తీయగలరా?", "explanation": "Specific door in the room.", "options": ["a", "an", "the", "no article"]},
    {"question": "It is ___ beautiful painting.", "correct_answer": "a", "telugu_meaning": "ఇది చాలా అందమైన పెయింటింగ్.", "explanation": "Beautiful starts with a consonant.", "options": ["a", "an", "the", "no article"]},
    {"question": "I waited for ___ hour.", "correct_answer": "an", "telugu_meaning": "నేను ఒక గంట వేచి ఉన్నాను.", "explanation": "Hour starts with a vowel sound.", "options": ["a", "an", "the", "no article"]},
    {"question": "___ rich should help ___ poor.", "correct_answer": "The", "telugu_meaning": "ధనవంతులు పేదలకు సహాయం చేయాలి.", "explanation": "Adjectives used as nouns to represent a class take 'the'.", "options": ["A", "An", "The", "no article"]},
    {"question": "I read ___ book you recommended.", "correct_answer": "the", "telugu_meaning": "నువ్వు సిఫార్సు చేసిన పుస్తకం నేను చదివాను.", "explanation": "Specific book.", "options": ["a", "an", "the", "no article"]},
    {"question": "She is ___ MLA.", "correct_answer": "an", "telugu_meaning": "ఆమె ఒక ఎమ్మెల్యే.", "explanation": "MLA starts with the vowel sound 'em'.", "options": ["a", "an", "the", "no article"]},
    {"question": "He works in ___ office.", "correct_answer": "an", "telugu_meaning": "అతను ఒక ఆఫీసులో పనిచేస్తాడు.", "explanation": "Office starts with a vowel sound.", "options": ["a", "an", "the", "no article"]},
    {"question": "Let's go to ___ park.", "correct_answer": "the", "telugu_meaning": "పార్కుకి వెళ్దాం.", "explanation": "Specific known park.", "options": ["a", "an", "the", "no article"]},
    {"question": "Give me ___ pen.", "correct_answer": "a", "telugu_meaning": "నాకు ఒక పెన్ ఇవ్వు.", "explanation": "Any general pen.", "options": ["a", "an", "the", "no article"]}
]

speaking_data = [
    {"question": "I have an idea.", "telugu_meaning": "నాకు ఒక ఆలోచన ఉంది.", "explanation": "Focus on joining 'an' with 'idea'."},
    {"question": "The sun is shining brightly.", "telugu_meaning": "సూర్యుడు ప్రకాశవంతంగా మెరుస్తున్నాడు.", "explanation": "Use 'the' for unique objects like the sun."},
    {"question": "Can you pass the salt?", "telugu_meaning": "ఉప్పు అందించగలరా?", "explanation": "Use 'the' for specific objects on the table."},
    {"question": "She is an honest person.", "telugu_meaning": "ఆమె నిజాయితీగల వ్యక్తి.", "explanation": "Remember 'h' is silent, so use 'an'."},
    {"question": "He bought a new car.", "telugu_meaning": "అతను కొత్త కారు కొన్నాడు.", "explanation": "Use 'a' when mentioning something for the first time."},
    {"question": "The car is blue.", "telugu_meaning": "ఆ కారు నీలం రంగులో ఉంది.", "explanation": "Use 'the' when referring back to the car."},
    {"question": "I saw an elephant at the zoo.", "telugu_meaning": "నేను జూలో ఒక ఏనుగును చూశాను.", "explanation": "Use 'an' before vowel sounds."},
    {"question": "It takes an hour.", "telugu_meaning": "దీనికి ఒక గంట పడుతుంది.", "explanation": "'hour' starts with a vowel sound."},
    {"question": "He is a university student.", "telugu_meaning": "అతను ఒక విశ్వవిద్యాలయ విద్యార్థి.", "explanation": "'university' starts with a consonant 'yu' sound."},
    {"question": "The earth is round.", "telugu_meaning": "భూమి గుండ్రంగా ఉంటుంది.", "explanation": "Unique objects take 'the'."},
    {"question": "She plays the piano.", "telugu_meaning": "ఆమె పియానో వాయిస్తుంది.", "explanation": "Musical instruments take 'the'."},
    {"question": "I need a doctor.", "telugu_meaning": "నాకు ఒక డాక్టర్ కావాలి.", "explanation": "General reference to a profession."},
    {"question": "Where is the nearest hospital?", "telugu_meaning": "దగ్గరలో ఉన్న ఆసుపత్రి ఎక్కడ ఉంది?", "explanation": "Asking for a specific unique place nearby."},
    {"question": "He is the best teacher.", "telugu_meaning": "అతను ఉత్తమ ఉపాధ్యాయుడు.", "explanation": "Superlative 'best' takes 'the'."},
    {"question": "Give me an apple.", "telugu_meaning": "నాకు ఒక ఆపిల్ ఇవ్వు.", "explanation": "Simple use of 'an' before a vowel."},
    {"question": "I met a European.", "telugu_meaning": "నేను ఒక యూరోపియన్‌ను కలిశాను.", "explanation": "'European' starts with a 'yu' sound."},
    {"question": "It is a one-way street.", "telugu_meaning": "ఇది వన్-వే స్ట్రీట్.", "explanation": "'one' starts with a 'wa' sound."},
    {"question": "She is an MP.", "telugu_meaning": "ఆమె ఒక ఎంపీ.", "explanation": "Acronym 'MP' starts with vowel sound 'em'."},
    {"question": "The dog is barking.", "telugu_meaning": "కుక్క అరుస్తోంది.", "explanation": "Specific dog that you can hear."},
    {"question": "I want a dog.", "telugu_meaning": "నాకు కుక్క కావాలి.", "explanation": "Any dog, not specific."},
    {"question": "Let's go to the beach.", "telugu_meaning": "బీచ్‌కి వెళ్దాం.", "explanation": "Specific location known to speaker and listener."},
    {"question": "I read a book yesterday.", "telugu_meaning": "నేను నిన్న ఒక పుస్తకం చదివాను.", "explanation": "Introducing a new item."},
    {"question": "The book was good.", "telugu_meaning": "ఆ పుస్తకం బాగుంది.", "explanation": "Referring back to the book."},
    {"question": "Look at the moon.", "telugu_meaning": "చంద్రుడి వైపు చూడు.", "explanation": "Unique object in the sky."},
    {"question": "He is in the kitchen.", "telugu_meaning": "అతను వంటగదిలో ఉన్నాడు.", "explanation": "Specific room in the house."},
    {"question": "Open the door.", "telugu_meaning": "తలుపు తీయు.", "explanation": "Specific door in context."},
    {"question": "I need a pen.", "telugu_meaning": "నాకు ఒక పెన్ కావాలి.", "explanation": "Any pen."},
    {"question": "Please give me the red pen.", "telugu_meaning": "దయచేసి నాకు ఎరుపు రంగు పెన్ ఇవ్వు.", "explanation": "Specific pen."},
    {"question": "He is an old man.", "telugu_meaning": "అతను ఒక ముసలివాడు.", "explanation": "Vowel sound 'o'."},
    {"question": "The water is cold.", "telugu_meaning": "నీరు చల్లగా ఉంది.", "explanation": "Specific water, e.g., in a glass or pool."}
]

concept = Concept.objects.filter(name='Articles').first()
if concept:
    concept.examples = examples_data
    concept.save()
    
    # Delete existing to prevent duplicates if any
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
    print("Articles completed successfully.")
else:
    print("Concept 'Articles' not found.")
