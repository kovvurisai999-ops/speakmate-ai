import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- TRAVEL CONVERSATION DATA ---
travel_conv_content = "Travel Conversation focuses on the dialogues you have while journeying. It covers speaking with airport staff, taxi drivers, hotel receptionists, and asking locals for directions or recommendations."
travel_conv_rules = """
- Always carry basic local phrases or keep them handy if traveling internationally.
- Use 'Excuse me' before asking a stranger for directions.
- Speak clearly and simply when asking for information.
- Confirm details (like time, price, or location) by repeating them back.
"""

travel_conv_examples = [
    {"en": "Excuse me, how do I get to the museum?", "te": "క్షమించండి, నేను మ్యూజియంకు ఎలా వెళ్ళాలి?", "explanation": "Asking for directions."},
    {"en": "Go straight and turn left at the traffic light.", "te": "తిన్నగా వెళ్లి ట్రాఫిక్ లైట్ దగ్గర ఎడమవైపు తిరగండి.", "explanation": "Giving directions."},
    {"en": "Could you please help me with my luggage?", "te": "దయచేసి నా లగేజీకి సహాయం చేయగలరా?", "explanation": "Asking for assistance."},
    {"en": "What time is the next bus to the city center?", "te": "సిటీ సెంటర్‌కి తదుపరి బస్సు ఏ సమయానికి ఉంది?", "explanation": "Asking for transport schedules."},
    {"en": "I have a reservation under the name John.", "te": "జాన్ పేరు మీద నాకు బుకింగ్ ఉంది.", "explanation": "Checking in at a hotel."},
    {"en": "Could you recommend a good local restaurant?", "te": "మీరు ఏదైనా మంచి స్థానిక రెస్టారెంట్‌ని సూచించగలరా?", "explanation": "Asking for recommendations."},
    {"en": "How far is the airport from here?", "te": "ఇక్కడి నుండి విమానాశ్రయం ఎంత దూరంలో ఉంది?", "explanation": "Asking about distance."},
    {"en": "Take me to this address, please.", "te": "దయచేసి నన్ను ఈ చిరునామాకు తీసుకువెళ్ళండి.", "explanation": "Instructing a taxi driver."},
    {"en": "Can I have a map of the city, please?", "te": "దయచేసి నాకు సిటీ మ్యాప్ ఇవ్వగలరా?", "explanation": "Requesting tourist info."},
    {"en": "Is it safe to walk around here at night?", "te": "రాత్రిపూట ఇక్కడ నడవడం సురక్షితమేనా?", "explanation": "Asking about safety."}
]
travel_conv_examples = (travel_conv_examples * 5)[:50]

travel_conv_blanks = [
    {"question": "Excuse me, how do I ___ to the museum?", "correct_answer": "get", "telugu_meaning": "క్షమించండి, నేను మ్యూజియంకు ఎలా వెళ్ళాలి?", "explanation": "Common phrase for asking directions.", "options": ["make", "do", "get", "take"]},
    {"question": "Go ___ and turn left.", "correct_answer": "straight", "telugu_meaning": "తిన్నగా వెళ్లి ఎడమవైపు తిరగండి.", "explanation": "Direction instruction.", "options": ["back", "straight", "around", "over"]},
    {"question": "I have a ___ under the name Ram.", "correct_answer": "reservation", "telugu_meaning": "రామ్ పేరు మీద నాకు బుకింగ్ (రిజర్వేషన్) ఉంది.", "explanation": "Booking confirmation.", "options": ["ticket", "reservation", "seat", "bag"]},
    {"question": "Could you ___ a good restaurant?", "correct_answer": "recommend", "telugu_meaning": "మీరు ఒక మంచి రెస్టారెంట్‌ని సూచించగలరా?", "explanation": "Asking for advice.", "options": ["eat", "cook", "recommend", "hide"]},
    {"question": "Take me to this ___, please.", "correct_answer": "address", "telugu_meaning": "దయచేసి నన్ను ఈ అడ్రస్‌కి తీసుకువెళ్ళండి.", "explanation": "Location detail for a taxi.", "options": ["name", "address", "time", "price"]}
]
travel_conv_blanks = (travel_conv_blanks * 6)[:30]

travel_conv_speaking = [
    {"question": "How do I get to the station?", "telugu_meaning": "నేను స్టేషన్‌కి ఎలా వెళ్ళాలి?", "explanation": "Ask clearly."},
    {"question": "I have a reservation.", "telugu_meaning": "నాకు రిజర్వేషన్ ఉంది.", "explanation": "State this at the hotel reception."},
    {"question": "Could you recommend a restaurant?", "telugu_meaning": "ఒక రెస్టారెంట్‌ని సూచించగలరా?", "explanation": "Polite request for advice."},
    {"question": "Take me to this address, please.", "telugu_meaning": "దయచేసి నన్ను ఈ అడ్రస్‌కి తీసుకెళ్లండి.", "explanation": "Show the address and speak clearly."},
    {"question": "How far is the airport?", "telugu_meaning": "ఎయిర్‌పోర్ట్ ఎంత దూరంలో ఉంది?", "explanation": "Ask about distance."}
]
travel_conv_speaking = (travel_conv_speaking * 6)[:30]


# --- PRESENTATION DATA ---
presentation_content = "Presentation Conversation involves the language used when addressing an audience, delivering a speech, or presenting information in a formal setting."
presentation_rules = """
- Start with a strong hook and welcome the audience (e.g., 'Good morning, thank you for being here').
- Outline what you are going to talk about (e.g., 'Today, I will cover three main points').
- Use transition words to connect your ideas (e.g., 'Moving on to the next topic...').
- End with a summary and a Q&A session (e.g., 'To conclude...', 'Are there any questions?').
"""

presentation_examples = [
    {"en": "Good morning, everyone. Thank you for being here.", "te": "అందరికీ శుభోదయం. ఇక్కడ ఉన్నందుకు ధన్యవాదాలు.", "explanation": "Welcoming the audience."},
    {"en": "Today, I am going to talk about our new project.", "te": "ఈ రోజు నేను మన కొత్త ప్రాజెక్ట్ గురించి మాట్లాడబోతున్నాను.", "explanation": "Introducing the topic."},
    {"en": "Let's begin by looking at the current market trends.", "te": "ప్రస్తుత మార్కెట్ ట్రెండ్స్‌ను చూడటం ద్వారా ప్రారంభిద్దాం.", "explanation": "Starting the first point."},
    {"en": "Moving on to the next slide, you will see our sales data.", "te": "తదుపరి స్లయిడ్‌కి వెళుతున్నప్పుడు, మీరు మా విక్రయాల డేటాను చూస్తారు.", "explanation": "Transitioning to new information."},
    {"en": "As you can see from this chart, our profits have increased.", "te": "ఈ చార్ట్ ద్వారా మీరు చూడగలిగినట్లుగా, మా లాభాలు పెరిగాయి.", "explanation": "Explaining visual aids."},
    {"en": "Let me give you a brief overview of the plan.", "te": "ప్రణాళిక గురించి నేను మీకు సంక్షిప్త వివరణ ఇస్తాను.", "explanation": "Summarizing."},
    {"en": "To sum up, we need to focus on customer satisfaction.", "te": "సారాంశంలో, మనం కస్టమర్ సంతృప్తిపై దృష్టి పెట్టాలి.", "explanation": "Concluding the presentation."},
    {"en": "That brings me to the end of my presentation.", "te": "అది నా ప్రెజెంటేషన్ ముగింపుకు నన్ను తీసుకువచ్చింది.", "explanation": "Signaling the end."},
    {"en": "Thank you for your attention.", "te": "మీరు శ్రద్ధ వహించినందుకు ధన్యవాదాలు.", "explanation": "Thanking the audience."},
    {"en": "Does anyone have any questions?", "te": "ఎవరికైనా ఏమైనా ప్రశ్నలు ఉన్నాయా?", "explanation": "Opening the Q&A session."}
]
presentation_examples = (presentation_examples * 5)[:50]

presentation_blanks = [
    {"question": "Today, I am going to ___ about our new project.", "correct_answer": "talk", "telugu_meaning": "ఈ రోజు నేను మన కొత్త ప్రాజెక్ట్ గురించి మాట్లాడబోతున్నాను.", "explanation": "Introducing the topic.", "options": ["sing", "talk", "sleep", "eat"]},
    {"question": "Moving on to the next ___, you will see our sales.", "correct_answer": "slide", "telugu_meaning": "తదుపరి స్లయిడ్‌కి వెళుతున్నప్పుడు, మీరు మా విక్రయాలను చూస్తారు.", "explanation": "Presentation visual.", "options": ["room", "slide", "car", "street"]},
    {"question": "To ___ up, we need to focus on quality.", "correct_answer": "sum", "telugu_meaning": "సారాంశంలో, మనం నాణ్యతపై దృష్టి పెట్టాలి.", "explanation": "Phrase meaning 'to conclude'.", "options": ["sum", "add", "minus", "jump"]},
    {"question": "Thank you for your ___.", "correct_answer": "attention", "telugu_meaning": "మీ శ్రద్ధకు ధన్యవాదాలు.", "explanation": "Polite closing.", "options": ["money", "attention", "food", "anger"]},
    {"question": "Does anyone have any ___?", "correct_answer": "questions", "telugu_meaning": "ఎవరికైనా ఏమైనా ప్రశ్నలు ఉన్నాయా?", "explanation": "Asking for audience queries.", "options": ["questions", "answers", "jokes", "stories"]}
]
presentation_blanks = (presentation_blanks * 6)[:30]

presentation_speaking = [
    {"question": "Good morning, everyone.", "telugu_meaning": "అందరికీ శుభోదయం.", "explanation": "Speak confidently to the audience."},
    {"question": "Today, I will talk about our project.", "telugu_meaning": "ఈరోజు, నేను మన ప్రాజెక్ట్ గురించి మాట్లాడతాను.", "explanation": "Introduce the topic clearly."},
    {"question": "Moving on to the next slide.", "telugu_meaning": "తదుపరి స్లయిడ్‌కి వెళదాం.", "explanation": "Use this as a transition."},
    {"question": "Thank you for your attention.", "telugu_meaning": "మీ శ్రద్ధకు ధన్యవాదాలు.", "explanation": "Smile and thank the audience."},
    {"question": "Are there any questions?", "telugu_meaning": "ఏమైనా ప్రశ్నలు ఉన్నాయా?", "explanation": "Open the floor to the audience."}
]
presentation_speaking = (presentation_speaking * 6)[:30]


# --- SILENT LETTERS DATA (LEVEL 6) ---
silent_content = "Silent Letters are letters in a word that are written but not pronounced when speaking. English has many silent letters which can make pronunciation and spelling difficult."
silent_rules = """
- Learn common patterns: 'k' is silent before 'n' (know, knee).
- 'b' is often silent after 'm' at the end of a word (comb, bomb).
- 'w' is silent before 'r' (write, wrong).
- 'h' is silent in many words, especially after 'w' (what, when) or at the beginning of some words (hour, honest).
"""

silent_examples = [
    {"en": "I don't know the answer.", "te": "నాకు సమాధానం తెలియదు.", "explanation": "The 'k' in 'know' is silent."},
    {"en": "Please write your name.", "te": "దయచేసి మీ పేరు రాయండి.", "explanation": "The 'w' in 'write' is silent."},
    {"en": "He hurt his knee.", "te": "అతను తన మోకాలికి గాయం చేసుకున్నాడు.", "explanation": "The 'k' in 'knee' is silent."},
    {"en": "I need to comb my hair.", "te": "నేను నా జుట్టును దువ్వుకోవాలి.", "explanation": "The 'b' in 'comb' is silent."},
    {"en": "Listen to the music.", "te": "సంగీతం వినండి.", "explanation": "The 't' in 'listen' is silent."},
    {"en": "We walked around the castle.", "te": "మేము కోట చుట్టూ నడిచాము.", "explanation": "The 't' in 'castle' is silent."},
    {"en": "She is an honest person.", "te": "ఆమె నిజాయితీపరురాలు.", "explanation": "The 'h' in 'honest' is silent."},
    {"en": "It takes an hour to get there.", "te": "అక్కడికి చేరుకోవడానికి ఒక గంట పడుతుంది.", "explanation": "The 'h' in 'hour' is silent."},
    {"en": "He is my friend.", "te": "అతను నా స్నేహితుడు.", "explanation": "The 'i' in 'friend' is silent (pronounced frend)."},
    {"en": "That is the wrong answer.", "te": "అది తప్పు సమాధానం.", "explanation": "The 'w' in 'wrong' is silent."}
]
silent_examples = (silent_examples * 5)[:50]

silent_blanks = [
    {"question": "I don't ___ the answer.", "correct_answer": "know", "telugu_meaning": "నాకు సమాధానం తెలియదు.", "explanation": "Silent 'k'.", "options": ["now", "know", "no", "knot"]},
    {"question": "Please ___ your name on the paper.", "correct_answer": "write", "telugu_meaning": "దయచేసి కాగితంపై మీ పేరు రాయండి.", "explanation": "Silent 'w'.", "options": ["right", "write", "rite", "ride"]},
    {"question": "She is an ___ woman.", "correct_answer": "honest", "telugu_meaning": "ఆమె నిజాయితీ గల మహిళ.", "explanation": "Silent 'h'. Takes 'an' instead of 'a'.", "options": ["honest", "honor", "hour", "house"]},
    {"question": "I need to ___ my hair.", "correct_answer": "comb", "telugu_meaning": "నేను నా జుట్టు దువ్వుకోవాలి.", "explanation": "Silent 'b'.", "options": ["com", "comb", "come", "cone"]},
    {"question": "___ to the teacher carefully.", "correct_answer": "Listen", "telugu_meaning": "ఉపాధ్యాయుడి మాట జాగ్రత్తగా వినండి.", "explanation": "Silent 't'.", "options": ["Lissen", "Listen", "List", "Lost"]}
]
silent_blanks = (silent_blanks * 6)[:30]

silent_speaking = [
    {"question": "I don't know.", "telugu_meaning": "నాకు తెలియదు.", "explanation": "Do not pronounce the 'k'. (Say 'no')."},
    {"question": "Please write it down.", "telugu_meaning": "దయచేసి దానిని రాయండి.", "explanation": "Do not pronounce the 'w'. (Say 'rite')."},
    {"question": "Listen to me.", "telugu_meaning": "నా మాట విను.", "explanation": "Do not pronounce the 't'. (Say 'lissen')."},
    {"question": "She is honest.", "telugu_meaning": "ఆమె నిజాయితీపరురాలు.", "explanation": "Do not pronounce the 'h'. (Say 'on-est')."},
    {"question": "It takes one hour.", "telugu_meaning": "దీనికి ఒక గంట పడుతుంది.", "explanation": "Do not pronounce the 'h'. (Say 'our')."}
]
silent_speaking = (silent_speaking * 6)[:30]

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

insert_data('Travel', travel_conv_content, travel_conv_rules, travel_conv_examples, travel_conv_blanks, travel_conv_speaking)
insert_data('Presentation', presentation_content, presentation_rules, presentation_examples, presentation_blanks, presentation_speaking)
insert_data('Silent Letters', silent_content, silent_rules, silent_examples, silent_blanks, silent_speaking)
