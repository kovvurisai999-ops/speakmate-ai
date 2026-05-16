import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- TRAVEL VOCABULARY DATA ---
travel_content = "Travel Vocabulary includes words and phrases useful for planning trips, taking flights, staying in hotels, asking for directions, and exploring new places."
travel_rules = """
- Learn polite phrases for asking directions (e.g., 'Excuse me, could you tell me where...').
- Familiarize yourself with airport terms (boarding pass, departure, luggage).
- Practice hotel booking vocabulary (reservation, check-in, check-out).
- Always use 'please' and 'thank you' when interacting with locals.
"""

travel_examples = [
    {"en": "I would like to book a flight ticket.", "te": "నేను ఫ్లైట్ టికెట్ బుక్ చేయాలనుకుంటున్నాను.", "explanation": "Making a travel reservation."},
    {"en": "Where is the boarding gate?", "te": "బోర్డింగ్ గేట్ ఎక్కడ ఉంది?", "explanation": "Airport inquiry."},
    {"en": "I have two bags to check in.", "te": "నాకు చెక్ ఇన్ చేయడానికి రెండు బ్యాగులు ఉన్నాయి.", "explanation": "Luggage process."},
    {"en": "Can you call a taxi for me?", "te": "దయచేసి నాకోసం టాక్సీ పిలవగలరా?", "explanation": "Transportation request."},
    {"en": "What time is the check-out?", "te": "చెక్-అవుట్ సమయం ఎంత?", "explanation": "Hotel inquiry."},
    {"en": "Excuse me, where is the nearest ATM?", "te": "క్షమించండి, సమీపంలో ATM ఎక్కడ ఉంది?", "explanation": "Asking for directions."},
    {"en": "I would like a room with a sea view.", "te": "నాకు సముద్రం కనిపించే గది కావాలి.", "explanation": "Hotel room preference."},
    {"en": "How much does this ticket cost?", "te": "ఈ టికెట్ ధర ఎంత?", "explanation": "Asking for price."},
    {"en": "Our flight is delayed by an hour.", "te": "మా ఫ్లైట్ ఒక గంట ఆలస్యం అయింది.", "explanation": "Travel update."},
    {"en": "Do you have a map of the city?", "te": "మీ దగ్గర ఈ సిటీ మ్యాప్ ఉందా?", "explanation": "Asking for local information."}
]
travel_examples = (travel_examples * 5)[:50]

travel_blanks = [
    {"question": "Please show your ___ pass at the gate.", "correct_answer": "boarding", "telugu_meaning": "దయచేసి గేట్ వద్ద మీ బోర్డింగ్ పాస్‌ని చూపించండి.", "explanation": "Document needed to board a plane.", "options": ["driving", "boarding", "walking", "playing"]},
    {"question": "I would like to make a ___ for two nights.", "correct_answer": "reservation", "telugu_meaning": "నేను రెండు రాత్రుల కోసం బుకింగ్ చేయాలనుకుంటున్నాను.", "explanation": "Booking a hotel room.", "options": ["reservation", "party", "food", "game"]},
    {"question": "Where can I collect my ___?", "correct_answer": "luggage", "telugu_meaning": "నా బ్యాగులను నేను ఎక్కడ తీసుకోవచ్చు?", "explanation": "Travelers' bags.", "options": ["car", "luggage", "ticket", "money"]},
    {"question": "The ___ time is 11 AM.", "correct_answer": "check-out", "telugu_meaning": "చెక్-అవుట్ సమయం ఉదయం 11 గంటలు.", "explanation": "Time to leave a hotel.", "options": ["check-out", "sleep", "wake", "eat"]},
    {"question": "Excuse me, how do I get to the ___ station?", "correct_answer": "railway", "telugu_meaning": "క్షమించండి, రైల్వే స్టేషన్‌కి ఎలా వెళ్ళాలి?", "explanation": "Transport hub.", "options": ["moon", "railway", "sky", "cloud"]}
]
travel_blanks = (travel_blanks * 6)[:30]

travel_speaking = [
    {"question": "Where is the boarding gate?", "telugu_meaning": "బోర్డింగ్ గేట్ ఎక్కడ ఉంది?", "explanation": "Speak with an inquiring tone."},
    {"question": "I would like to book a room.", "telugu_meaning": "నేను ఒక గదిని బుక్ చేయాలనుకుంటున్నాను.", "explanation": "Polite request."},
    {"question": "Can you call a taxi for me?", "telugu_meaning": "నాకోసం టాక్సీని పిలవగలరా?", "explanation": "Asking for help."},
    {"question": "How much does this cost?", "telugu_meaning": "దీని ధర ఎంత?", "explanation": "Common shopping/travel question."},
    {"question": "Excuse me, where is the ATM?", "telugu_meaning": "క్షమించండి, ATM ఎక్కడ ఉంది?", "explanation": "Start politely with 'Excuse me'."}
]
travel_speaking = (travel_speaking * 6)[:30]


# --- FOOD VOCABULARY DATA ---
food_content = "Food Vocabulary covers terms related to eating out, cooking, describing tastes, ordering at a restaurant, and talking about different types of meals."
food_rules = """
- Learn how to describe flavors (spicy, sweet, sour, bitter, salty).
- Practice phrases for ordering food (e.g., 'I would like...', 'Could we get the bill?').
- Understand cooking methods (fried, boiled, baked, grilled).
- Use polite requests when interacting with waiters.
"""

food_examples = [
    {"en": "I would like a table for two, please.", "te": "దయచేసి ఇద్దరికి ఒక టేబుల్ కావాలి.", "explanation": "Restaurant request."},
    {"en": "Could I see the menu?", "te": "నేను మెనూ చూడవచ్చా?", "explanation": "Asking for options."},
    {"en": "This soup is very spicy.", "te": "ఈ సూప్ చాలా కారంగా ఉంది.", "explanation": "Describing taste."},
    {"en": "I am allergic to peanuts.", "te": "నాకు వేరుశెనగ అంటే ఎలర్జీ.", "explanation": "Dietary restriction."},
    {"en": "Can we have the bill, please?", "te": "దయచేసి బిల్లు ఇవ్వగలరా?", "explanation": "Asking to pay."},
    {"en": "The chicken is perfectly grilled.", "te": "చికెన్ అద్భుతంగా గ్రిల్ చేయబడింది.", "explanation": "Cooking method."},
    {"en": "I will have a glass of water.", "te": "నేను ఒక గ్లాసు నీరు తీసుకుంటాను.", "explanation": "Ordering a drink."},
    {"en": "This dessert is too sweet.", "te": "ఈ డెజర్ట్ చాలా తీయగా ఉంది.", "explanation": "Describing flavor."},
    {"en": "Do you have any vegetarian dishes?", "te": "మీ దగ్గర ఏమైనా శాఖాహార వంటకాలు ఉన్నాయా?", "explanation": "Asking about food types."},
    {"en": "The food here is delicious.", "te": "ఇక్కడ ఆహారం చాలా రుచిగా ఉంటుంది.", "explanation": "Complimenting the food."}
]
food_examples = (food_examples * 5)[:50]

food_blanks = [
    {"question": "Could we have the ___, please?", "correct_answer": "bill", "telugu_meaning": "దయచేసి మాకు బిల్లు ఇవ్వగలరా?", "explanation": "Request for payment in a restaurant.", "options": ["menu", "bill", "plate", "spoon"]},
    {"question": "I would like to order a ___ pizza.", "correct_answer": "vegetarian", "telugu_meaning": "నేను వెజిటేరియన్ పిజ్జా ఆర్డర్ చేయాలనుకుంటున్నాను.", "explanation": "Type of food.", "options": ["wooden", "vegetarian", "plastic", "metal"]},
    {"question": "This curry is very ___.", "correct_answer": "spicy", "telugu_meaning": "ఈ కూర చాలా కారంగా ఉంది.", "explanation": "Taste descriptor.", "options": ["loud", "spicy", "tall", "fast"]},
    {"question": "I am ___ to seafood.", "correct_answer": "allergic", "telugu_meaning": "నాకు సీఫుడ్ పడదు (ఎలర్జీ).", "explanation": "Health restriction.", "options": ["allergic", "happy", "sad", "angry"]},
    {"question": "The ___ was delicious.", "correct_answer": "food", "telugu_meaning": "ఆహారం చాలా రుచిగా ఉంది.", "explanation": "General term for what you eat.", "options": ["table", "chair", "food", "glass"]}
]
food_blanks = (food_blanks * 6)[:30]

food_speaking = [
    {"question": "I would like a table for two.", "telugu_meaning": "నాకు ఇద్దరికి ఒక టేబుల్ కావాలి.", "explanation": "Polite restaurant request."},
    {"question": "Could I see the menu, please?", "telugu_meaning": "నేను మెనూ చూడవచ్చా?", "explanation": "Polite request."},
    {"question": "This food is very spicy.", "telugu_meaning": "ఈ ఆహారం చాలా కారంగా ఉంది.", "explanation": "Describe the taste clearly."},
    {"question": "Can we have the bill?", "telugu_meaning": "మాకు బిల్లు ఇస్తారా?", "explanation": "Ask clearly."},
    {"question": "The meal was delicious.", "telugu_meaning": "భోజనం చాలా రుచిగా ఉంది.", "explanation": "Give a compliment."}
]
food_speaking = (food_speaking * 6)[:30]


# --- EMOTIONAL VOCABULARY DATA ---
emotional_content = "Emotional Vocabulary helps you express your feelings, moods, and emotional states accurately to others. It goes beyond basic words like 'happy' or 'sad'."
emotional_rules = """
- Expand your vocabulary to express exact feelings (e.g., 'frustrated' instead of just 'angry').
- Use phrases like 'I feel...' or 'I am...' to state your emotion.
- Pay attention to body language which matches the emotional words.
- Learn empathy phrases (e.g., 'I understand how you feel').
"""

emotional_examples = [
    {"en": "I am feeling very anxious about the exam.", "te": "పరీక్ష గురించి నేను చాలా ఆందోళన చెందుతున్నాను.", "explanation": "Feeling nervous or worried."},
    {"en": "She was thrilled to receive the award.", "te": "అవార్డు తీసుకున్నందుకు ఆమె చాలా సంతోషించింది.", "explanation": "Feeling extremely happy."},
    {"en": "He is frustrated with his computer.", "te": "అతను తన కంప్యూటర్ పట్ల విసుగు చెందాడు.", "explanation": "Feeling annoyed, especially because of inability to change something."},
    {"en": "I am so grateful for your help.", "te": "మీ సహాయానికి నేను చాలా కృతజ్ఞుడను.", "explanation": "Feeling thankful."},
    {"en": "They were devastated by the bad news.", "te": "చెడు వార్త విని వారు తీవ్రంగా కుంగిపోయారు.", "explanation": "Feeling severe shock and grief."},
    {"en": "I feel exhausted after working all day.", "te": "రోజంతా పని చేసిన తర్వాత నేను చాలా అలసిపోయినట్లుగా భావిస్తున్నాను.", "explanation": "Feeling completely drained of energy."},
    {"en": "She is jealous of her friend's success.", "te": "ఆమె తన స్నేహితురాలి విజయం పట్ల అసూయ పడుతోంది.", "explanation": "Feeling envious."},
    {"en": "He was embarrassed when he fell down.", "te": "అతను కింద పడినప్పుడు ఇబ్బందిగా (సిగ్గుగా) ఫీలయ్యాడు.", "explanation": "Feeling ashamed or self-conscious."},
    {"en": "We are very proud of your achievements.", "te": "నీ విజయాల పట్ల మేము చాలా గర్విస్తున్నాము.", "explanation": "Feeling deep pleasure or satisfaction as a result of one's own or someone else's achievements."},
    {"en": "I am a little disappointed with the result.", "te": "ఫలితంతో నేను కొంచెం నిరాశ చెందాను.", "explanation": "Feeling sad or displeased because expectations were not met."}
]
emotional_examples = (emotional_examples * 5)[:50]

emotional_blanks = [
    {"question": "I am very ___ for your support.", "correct_answer": "grateful", "telugu_meaning": "మీ మద్దతుకు నేను చాలా కృతజ్ఞుడను.", "explanation": "Feeling thankful.", "options": ["angry", "grateful", "sad", "jealous"]},
    {"question": "She was ___ when she heard the good news.", "correct_answer": "thrilled", "telugu_meaning": "శుభవార్త విన్నప్పుడు ఆమె చాలా సంతోషించింది.", "explanation": "Extremely happy.", "options": ["bored", "thrilled", "tired", "sad"]},
    {"question": "He felt ___ when he made a mistake in public.", "correct_answer": "embarrassed", "telugu_meaning": "అతను పబ్లిక్‌లో తప్పు చేసినప్పుడు ఇబ్బందిగా ఫీలయ్యాడు.", "explanation": "Feeling ashamed.", "options": ["proud", "embarrassed", "happy", "brave"]},
    {"question": "I am so ___ after running for an hour.", "correct_answer": "exhausted", "telugu_meaning": "గంట సేపు పరుగెత్తిన తర్వాత నేను బాగా అలసిపోయాను.", "explanation": "Very tired.", "options": ["fresh", "exhausted", "energetic", "awake"]},
    {"question": "We are ___ of our son's graduation.", "correct_answer": "proud", "telugu_meaning": "మా అబ్బాయి గ్రాడ్యుయేషన్ పట్ల మేము గర్విస్తున్నాము.", "explanation": "Feeling satisfaction regarding someone's achievement.", "options": ["jealous", "ashamed", "proud", "sad"]}
]
emotional_blanks = (emotional_blanks * 6)[:30]

emotional_speaking = [
    {"question": "I am feeling very anxious.", "telugu_meaning": "నేను చాలా ఆందోళనగా ఫీలవుతున్నాను.", "explanation": "Express worry in your voice."},
    {"question": "She was thrilled to see him.", "telugu_meaning": "ఆమె అతన్ని చూసి ఎంతో సంతోషించింది.", "explanation": "Express happiness."},
    {"question": "I am so grateful for your help.", "telugu_meaning": "మీ సహాయానికి నేను చాలా కృతజ్ఞుడను.", "explanation": "Express genuine thanks."},
    {"question": "He was very frustrated.", "telugu_meaning": "అతను చాలా విసుగు చెందాడు.", "explanation": "Express annoyance."},
    {"question": "We are proud of you.", "telugu_meaning": "మేము నిన్ను చూసి గర్విస్తున్నాము.", "explanation": "Express encouragement."}
]
emotional_speaking = (emotional_speaking * 6)[:30]

def insert_level3_data2(concept_name, content, rules, examples, blanks, speaking):
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

insert_level3_data2('Travel Vocabulary', travel_content, travel_rules, travel_examples, travel_blanks, travel_speaking)
insert_level3_data2('Food Vocabulary', food_content, food_rules, food_examples, food_blanks, food_speaking)
insert_level3_data2('Emotional Vocabulary', emotional_content, emotional_rules, emotional_examples, emotional_blanks, emotional_speaking)
