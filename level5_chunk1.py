import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- DAILY CONVERSATION DATA ---
daily_conv_content = "Daily Conversation involves the casual, everyday interactions we have with family, friends, neighbors, and strangers. It includes greetings, asking about well-being, and discussing daily routines."
daily_conv_rules = """
- Start with a polite greeting (e.g., 'Hi, how are you?').
- Use small talk to keep the conversation going (e.g., 'Nice weather today, isn't it?').
- Show active listening by using words like 'Oh', 'Really?', 'That's interesting'.
- End the conversation politely (e.g., 'It was nice talking to you', 'See you later').
"""

daily_conv_examples = [
    {"en": "Hi, how are you doing today?", "te": "హాయ్, ఈ రోజు మీరు ఎలా ఉన్నారు?", "explanation": "Common greeting."},
    {"en": "I'm doing well, thank you. And you?", "te": "నేను బాగున్నాను, ధన్యవాదాలు. మరియు మీరు?", "explanation": "Standard polite response."},
    {"en": "What did you have for breakfast?", "te": "మీరు అల్పాహారంగా ఏమి తీసుకున్నారు?", "explanation": "Casual morning question."},
    {"en": "I had some idli and coffee.", "te": "నేను ఇడ్లీ మరియు కాఫీ తీసుకున్నాను.", "explanation": "Answering about meals."},
    {"en": "How is your family doing?", "te": "మీ కుటుంబం ఎలా ఉంది?", "explanation": "Asking about loved ones."},
    {"en": "Everyone is fine, thanks for asking.", "te": "అందరూ బాగున్నారు, అడిగినందుకు ధన్యవాదాలు.", "explanation": "Responding about family."},
    {"en": "Did you watch the match last night?", "te": "మీరు నిన్న రాత్రి మ్యాచ్ చూశారా?", "explanation": "Making small talk."},
    {"en": "No, I was too tired and went to sleep.", "te": "లేదు, నేను బాగా అలసిపోయి నిద్రపోయాను.", "explanation": "Explaining your action."},
    {"en": "It looks like it might rain later.", "te": "తర్వాత వర్షం పడేలా కనిపిస్తోంది.", "explanation": "Talking about the weather."},
    {"en": "Yeah, we should probably take an umbrella.", "te": "అవును, మనం బహుశా గొడుగు తీసుకువెళ్లాలి.", "explanation": "Agreeing and suggesting an action."}
]
daily_conv_examples = (daily_conv_examples * 5)[:50]

daily_conv_blanks = [
    {"question": "Hi, how are you ___ today?", "correct_answer": "doing", "telugu_meaning": "హాయ్, ఈ రోజు మీరు ఎలా ఉన్నారు?", "explanation": "Common greeting phrase.", "options": ["making", "doing", "playing", "going"]},
    {"question": "I'm fine, ___ for asking.", "correct_answer": "thanks", "telugu_meaning": "నేను బాగున్నాను, అడిగినందుకు ధన్యవాదాలు.", "explanation": "Polite acknowledgment.", "options": ["sorry", "thanks", "please", "welcome"]},
    {"question": "___ did you do over the weekend?", "correct_answer": "What", "telugu_meaning": "మీరు వారాంతంలో (వీకెండ్) ఏమి చేసారు?", "explanation": "Asking about activities.", "options": ["Where", "When", "What", "Who"]},
    {"question": "It was ___ talking to you.", "correct_answer": "nice", "telugu_meaning": "మీతో మాట్లాడటం ఆనందంగా ఉంది.", "explanation": "Polite way to end a conversation.", "options": ["bad", "nice", "sad", "angry"]},
    {"question": "See you ___!", "correct_answer": "later", "telugu_meaning": "తర్వాత కలుద్దాం!", "explanation": "Common farewell.", "options": ["before", "later", "after", "never"]}
]
daily_conv_blanks = (daily_conv_blanks * 6)[:30]

daily_conv_speaking = [
    {"question": "Hi, how are you doing?", "telugu_meaning": "హాయ్, మీరు ఎలా ఉన్నారు?", "explanation": "Speak with a friendly, welcoming tone."},
    {"question": "I am doing well, thank you.", "telugu_meaning": "నేను బాగున్నాను, ధన్యవాదాలు.", "explanation": "Respond politely."},
    {"question": "Nice weather today, isn't it?", "telugu_meaning": "ఈ రోజు వాతావరణం బాగుంది, కదా?", "explanation": "Use a questioning tone at the end."},
    {"question": "It was nice talking to you.", "telugu_meaning": "మీతో మాట్లాడటం బాగుంది.", "explanation": "Express genuine pleasure."},
    {"question": "Catch you later!", "telugu_meaning": "తర్వాత కలుద్దాం!", "explanation": "Say it casually."}
]
daily_conv_speaking = (daily_conv_speaking * 6)[:30]


# --- SHOPPING DATA ---
shopping_content = "Shopping Conversation involves vocabulary and dialogue used when buying items at a store, market, or mall. It includes asking for prices, sizes, discounts, and making payments."
shopping_rules = """
- Always greet the shopkeeper politely (e.g., 'Excuse me, do you have...').
- Learn to ask about price (e.g., 'How much does this cost?').
- Know how to ask for different sizes or colors.
- Use polite phrases for bargaining if appropriate (e.g., 'Can you give me a discount?').
"""

shopping_examples = [
    {"en": "Excuse me, where is the clothing section?", "te": "క్షమించండి, బట్టల సెక్షన్ ఎక్కడ ఉంది?", "explanation": "Asking for store directions."},
    {"en": "How much does this shirt cost?", "te": "ఈ చొక్కా ధర ఎంత?", "explanation": "Asking the price."},
    {"en": "Do you have this in a larger size?", "te": "మీ దగ్గర ఇది కొంచెం పెద్ద సైజులో ఉందా?", "explanation": "Asking for a different size."},
    {"en": "Can I try this on?", "te": "నేను దీనిని వేసుకుని చూడవచ్చా?", "explanation": "Asking to use the fitting room."},
    {"en": "The fitting room is over there.", "te": "ఫిట్టింగ్ రూమ్ అక్కడ ఉంది.", "explanation": "Shop assistant's reply."},
    {"en": "Is there any discount on this item?", "te": "ఈ వస్తువుపై ఏదైనా డిస్కౌంట్ ఉందా?", "explanation": "Asking for a lower price."},
    {"en": "I'll take it. Where can I pay?", "te": "నేను ఇది తీసుకుంటాను. నేను ఎక్కడ డబ్బులు చెల్లించాలి?", "explanation": "Deciding to buy."},
    {"en": "Do you accept credit cards?", "te": "మీరు క్రెడిట్ కార్డులను అంగీకరిస్తారా?", "explanation": "Asking about payment methods."},
    {"en": "I am just browsing, thank you.", "te": "నేను ఊరికే చూస్తున్నాను, ధన్యవాదాలు.", "explanation": "When you don't want help from the staff."},
    {"en": "Can you give me a bill for this?", "te": "దీనికి మీరు నాకు బిల్లు ఇవ్వగలరా?", "explanation": "Asking for the receipt."}
]
shopping_examples = (shopping_examples * 5)[:50]

shopping_blanks = [
    {"question": "___ much does this bag cost?", "correct_answer": "How", "telugu_meaning": "ఈ బ్యాగ్ ధర ఎంత?", "explanation": "Question word for price.", "options": ["What", "Where", "How", "When"]},
    {"question": "Do you have this in a different ___?", "correct_answer": "color", "telugu_meaning": "మీ దగ్గర ఇది వేరే రంగులో ఉందా?", "explanation": "Asking for variety.", "options": ["taste", "color", "sound", "smell"]},
    {"question": "Can I ___ this on?", "correct_answer": "try", "telugu_meaning": "నేను దీనిని వేసుకుని (ట్రై చేసి) చూడవచ్చా?", "explanation": "Testing clothes before buying.", "options": ["try", "cry", "fly", "buy"]},
    {"question": "Is there any ___ on these shoes?", "correct_answer": "discount", "telugu_meaning": "ఈ బూట్లపై ఏదైనా డిస్కౌంట్ (తగ్గింపు) ఉందా?", "explanation": "Asking for a price reduction.", "options": ["tax", "discount", "extra", "fee"]},
    {"question": "Do you accept credit ___?", "correct_answer": "cards", "telugu_meaning": "మీరు క్రెడిట్ కార్డులను అంగీకరిస్తారా?", "explanation": "Payment method.", "options": ["coins", "cards", "notes", "paper"]}
]
shopping_blanks = (shopping_blanks * 6)[:30]

shopping_speaking = [
    {"question": "How much does this cost?", "telugu_meaning": "దీని ధర ఎంత?", "explanation": "Ask clearly when inquiring about price."},
    {"question": "Can I try this on?", "telugu_meaning": "నేను దీనిని వేసుకుని చూడవచ్చా?", "explanation": "Polite request for the fitting room."},
    {"question": "Do you have a smaller size?", "telugu_meaning": "మీ దగ్గర చిన్న సైజు ఉందా?", "explanation": "Emphasize 'smaller'."},
    {"question": "I am just browsing, thank you.", "telugu_meaning": "నేను ఊరికే చూస్తున్నాను, ధన్యవాదాలు.", "explanation": "Say it politely with a smile."},
    {"question": "I will pay by card.", "telugu_meaning": "నేను కార్డు ద్వారా చెల్లిస్తాను.", "explanation": "State your payment method clearly."}
]
shopping_speaking = (shopping_speaking * 6)[:30]


# --- OFFICE DATA ---
office_content = "Office Conversation involves professional dialogue with colleagues, managers, and clients. It covers meetings, project updates, asking for leave, and general workplace communication."
office_rules = """
- Use professional greetings (e.g., 'Good morning, team').
- Be clear and concise when giving updates.
- Use polite phrases when asking for help (e.g., 'Could you please assist me with...').
- Be respectful of others' time (e.g., 'Do you have a minute to discuss...').
"""

office_examples = [
    {"en": "Good morning, everyone. Let's start the meeting.", "te": "అందరికీ శుభోదయం. మనం మీటింగ్‌ని ప్రారంభిద్దాం.", "explanation": "Starting a formal meeting."},
    {"en": "Could you please send me the latest report?", "te": "దయచేసి మీరు నాకు తాజా రిపోర్ట్ పంపగలరా?", "explanation": "Polite professional request."},
    {"en": "I have finished my part of the project.", "te": "నేను ప్రాజెక్టులో నా భాగాన్ని పూర్తి చేసాను.", "explanation": "Giving a status update."},
    {"en": "We are facing a small issue with the software.", "te": "సాఫ్ట్‌వేర్‌తో మేము ఒక చిన్న సమస్యను ఎదుర్కొంటున్నాము.", "explanation": "Reporting a problem."},
    {"en": "Let's brainstorm some new ideas.", "te": "కొన్ని కొత్త ఆలోచనల కోసం మనం బ్రెయిన్ స్టామింగ్ చేద్దాం.", "explanation": "Encouraging team collaboration."},
    {"en": "I need to take a day off tomorrow.", "te": "నేను రేపు ఒక రోజు సెలవు తీసుకోవాలి.", "explanation": "Asking for leave."},
    {"en": "Can we reschedule our meeting to 3 PM?", "te": "మనం మన మీటింగ్‌ని మధ్యాహ్నం 3 గంటలకు మార్చుకోగలమా?", "explanation": "Changing an appointment time."},
    {"en": "Great job on the presentation today!", "te": "ఈరోజు ప్రెజెంటేషన్‌లో చాలా బాగా చేసారు!", "explanation": "Praising a colleague."},
    {"en": "I will look into this matter immediately.", "te": "నేను వెంటనే ఈ విషయం గురించి పరిశీలిస్తాను.", "explanation": "Promising action."},
    {"en": "Let me know if you need any help.", "te": "మీకు ఏమైనా సహాయం కావాలంటే నాకు తెలియజేయండి.", "explanation": "Offering assistance."}
]
office_examples = (office_examples * 5)[:50]

office_blanks = [
    {"question": "Let's ___ the meeting now.", "correct_answer": "start", "telugu_meaning": "మనం మీటింగ్‌ని ఇప్పుడు ప్రారంభిద్దాం.", "explanation": "Beginning an event.", "options": ["end", "start", "leave", "sleep"]},
    {"question": "Could you please ___ me the report?", "correct_answer": "send", "telugu_meaning": "దయచేసి మీరు నాకు రిపోర్ట్ పంపగలరా?", "explanation": "Requesting a document.", "options": ["eat", "send", "throw", "hide"]},
    {"question": "I need to take a day ___ tomorrow.", "correct_answer": "off", "telugu_meaning": "నేను రేపు ఒక రోజు సెలవు తీసుకోవాలి.", "explanation": "Phrase for taking leave.", "options": ["on", "off", "up", "down"]},
    {"question": "We need to meet the project ___.", "correct_answer": "deadline", "telugu_meaning": "మనం ప్రాజెక్ట్ గడువును చేరుకోవాలి.", "explanation": "Time limit.", "options": ["start", "deadline", "name", "price"]},
    {"question": "Let me know if you need any ___.", "correct_answer": "help", "telugu_meaning": "మీకు ఏమైనా సహాయం కావాలంటే నాకు తెలియజేయండి.", "explanation": "Offering support.", "options": ["trouble", "help", "pain", "sadness"]}
]
office_blanks = (office_blanks * 6)[:30]

office_speaking = [
    {"question": "Good morning, everyone.", "telugu_meaning": "అందరికీ శుభోదయం.", "explanation": "Speak clearly and professionally."},
    {"question": "Could you send me the report?", "telugu_meaning": "మీరు నాకు రిపోర్ట్ పంపగలరా?", "explanation": "Polite workplace request."},
    {"question": "I have completed my task.", "telugu_meaning": "నేను నా పనిని పూర్తి చేశాను.", "explanation": "Give the update confidently."},
    {"question": "Can we reschedule the meeting?", "telugu_meaning": "మనం మీటింగ్‌ని మార్చుకోగలమా?", "explanation": "Ask politely."},
    {"question": "Let me know if you need help.", "telugu_meaning": "సహాయం కావాలంటే నాకు చెప్పండి.", "explanation": "Offer support with a friendly tone."}
]
office_speaking = (office_speaking * 6)[:30]

def insert_level5_data(concept_name, content, rules, examples, blanks, speaking):
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

insert_level5_data('Daily Conversation', daily_conv_content, daily_conv_rules, daily_conv_examples, daily_conv_blanks, daily_conv_speaking)
insert_level5_data('Shopping', shopping_content, shopping_rules, shopping_examples, shopping_blanks, shopping_speaking)
insert_level5_data('Office', office_content, office_rules, office_examples, office_blanks, office_speaking)
