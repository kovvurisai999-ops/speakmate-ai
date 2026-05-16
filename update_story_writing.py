import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- STORY WRITING DATA ---
content = "Story Writing involves creating a sequence of events using imagination, emotions, characters, and situations. It improves creativity, English fluency, sentence formation, and vocabulary."
rules = """
- Structure: Beginning -> Problem -> Action -> Ending -> Moral.
- Story ki clear beginning undali mariyu ending meaningful ga undali.
- Simple English use cheyali mariyu sentences logical ga connect avvali.
- Characters understandable ga undali.
"""

# Story examples follow the 10-line pattern
examples = [
    {
        "en": "Rahul found a wallet on the road. There was a lot of money inside it. His friends told him to keep it. But Rahul wanted to return it. He checked the ID card inside. Then he called the owner. The owner was very worried. Rahul returned it safely. The owner thanked him with tears. Honesty made Rahul feel proud.",
        "te": "Rahul wallet దొరికినా దానిని నిజాయితీగా తిరిగి ఇచ్చాడు.",
        "explanation": "Simple past tense + moral value + real-life situation."
    },
    {
        "en": "Sai wanted to improve his spoken English. He downloaded an AI learning app. Every day he practiced speaking with the AI. The app corrected his grammar mistakes. At first, he was nervous to speak. Slowly, his confidence increased. He practiced interviews daily. After three months, he spoke fluently. He attended a company interview confidently. Finally, he got selected for the job.",
        "te": "AI app practice వల్ల Sai fluent English నేర్చుకున్నాడు.",
        "explanation": "Motivational story structure."
    },
    {
        "en": "Anitha was getting late for college. She ran to the bus stop quickly. But the bus had already left. She felt very sad. Then her friend offered a bike ride. Both reached the college on time. Anitha thanked her friend happily. The teacher appreciated their punctuality. They attended all classes properly. Good friends always help each other.",
        "te": "Friend సహాయం వల్ల Anitha college కి time కి చేరుకుంది.",
        "explanation": "Friendship and punctuality theme."
    },
    {
        "en": "Kiran spent many hours using his mobile phone. He ignored his studies and family. His exam marks became very low. His parents became worried. One day, his teacher advised him. Kiran realized his mistake. He reduced mobile usage gradually. He started studying regularly. His marks improved in the next exam. Balance is important in life.",
        "te": "Excess mobile usage వల్ల problems వచ్చాయి.",
        "explanation": "Real-world problem and solution."
    },
    {
        "en": "Meena attended her first job interview. She felt nervous in the waiting hall. She practiced answers silently. The interviewer asked simple questions. Meena answered confidently. She spoke politely and clearly. The interviewer appreciated her communication skills. After two days, she received a call. She got selected for the company. Confidence helped her succeed.",
        "te": "Confidence వల్ల Meena interview crack చేసింది.",
        "explanation": "Career success theme."
    },
    {
        "en": "Heavy rain started in the evening. Many people were stuck on the roads. A small tea shop became crowded. People shared umbrellas and helped each other. One old man slipped on the road. Two students helped him immediately. Everyone appreciated their kindness. The rain stopped after some time. People returned home safely. Humanity is more important than money.",
        "te": "మానవత్వం విలువను చాటిచెప్పే కథ.",
        "explanation": "Social value story."
    },
    {
        "en": "Ramu was a hardworking farmer. Every morning he woke up early. He worked in the fields all day. Sometimes the weather became difficult. Still, he never lost hope. His family supported him always. After many months, the crops grew well. He sold the crops in the market. His family became very happy. Hard work always gives results.",
        "te": "కష్టపడి పనిచేసే రైతు కథ.",
        "explanation": "Work ethics theme."
    },
    {
        "en": "Priya wanted to learn graphic design. She joined an online course. Every night she watched tutorials. She practiced designs daily. Sometimes she made many mistakes. But she never stopped learning. After six months, she became skilled. She started freelancing online. Now she earns money from home. Learning new skills changes life.",
        "te": "కొత్త నైపుణ్యాలు నేర్చుకోవడం జీవితాన్ని మారుస్తుంది.",
        "explanation": "Skill development theme."
    },
    {
        "en": "Arjun lost his phone in the market. He searched everywhere nervously. A shopkeeper found the phone. He called Arjun's friend from the contact list. Arjun rushed to the shop quickly. The shopkeeper returned the phone safely. Arjun thanked him sincerely. He felt very relieved. The shopkeeper refused any reward. Kind people still exist everywhere.",
        "te": "నిజాయితీ గల దుకాణదారుడి కథ.",
        "explanation": "Trust and kindness theme."
    },
    {
        "en": "Nikhil was afraid of exams. He worried every day. His teacher gave him study tips. Nikhil followed a timetable regularly. He revised lessons carefully. Slowly, his fear disappeared. He attended the exam confidently. The questions were easier than expected. He scored good marks finally. Preparation removes fear.",
        "te": "ప్రిపరేషన్ వల్ల పరీక్షా భయం తొలగుతుంది.",
        "explanation": "Preparation theme."
    }
]

# Adding placeholder stories up to 50
for i in range(11, 51):
    examples.append({
        "en": f"Story Example {i}: Once upon a time, a small bird lived in a large forest. It worked hard to build a strong nest. One day, a storm came. But the nest was safe because of its hard work. The bird felt happy. Every day is a new opportunity. Patience and effort bring success. The forest animals praised the bird. Moral: Effort never goes waste.",
        "te": f"Story example {i} in Telugu.",
        "explanation": "Simple moral story."
    })

blanks = [
    {"question": "Rahul found a ___ on the road.", "correct_answer": "wallet", "telugu_meaning": "రాహుల్ కు రోడ్డుపై వాలెట్ దొరికింది.", "explanation": "Item from story.", "options": ["wallet", "bag", "key", "phone"]},
    {"question": "Sai practiced speaking with the ___ app.", "correct_answer": "AI", "telugu_meaning": "సాయి AI యాప్ తో ప్రాక్టీస్ చేశాడు.", "explanation": "Technology tool.", "options": ["AI", "games", "music", "chat"]},
    {"question": "Anitha ran to the ___ stop.", "correct_answer": "bus", "telugu_meaning": "అనిత బస్టాప్ కి పరుగెత్తింది.", "explanation": "Location.", "options": ["bus", "train", "car", "auto"]},
    {"question": "Kiran reduced mobile ___ gradually.", "correct_answer": "usage", "telugu_meaning": "కిరణ్ మొబైల్ వాడకాన్ని తగ్గించాడు.", "explanation": "Action term.", "options": ["usage", "price", "color", "size"]},
    {"question": "Meena attended her first job ___.", "correct_answer": "interview", "telugu_meaning": "మీనా తన మొదటి ఇంటర్వ్యూకి హాజరయ్యింది.", "explanation": "Career event.", "options": ["interview", "party", "class", "trip"]},
    {"question": "The heavy ___ started in the evening.", "correct_answer": "rain", "telugu_meaning": "సాయంత్రం భారీ వర్షం మొదలైంది.", "explanation": "Weather event.", "options": ["rain", "snow", "wind", "sun"]},
    {"question": "Ramu worked in the ___ all day.", "correct_answer": "fields", "telugu_meaning": "రాము పొలంలో రోజంతా పనిచేశాడు.", "explanation": "Workplace.", "options": ["fields", "office", "shop", "school"]},
    {"question": "Priya joined an online ___.", "correct_answer": "course", "telugu_meaning": "ప్రియ ఆన్‌లైన్ కోర్సులో చేరింది.", "explanation": "Learning activity.", "options": ["course", "group", "game", "meeting"]},
    {"question": "Arjun lost his ___ in the market.", "correct_answer": "phone", "telugu_meaning": "అర్జున్ మార్కెట్లో తన ఫోన్ పోగొట్టుకున్నాడు.", "explanation": "Personal item.", "options": ["phone", "bag", "money", "watch"]},
    {"question": "Preparation removes ___.", "correct_answer": "fear", "telugu_meaning": "సిద్ధపడటం వల్ల భయం తొలగుతుంది.", "explanation": "Abstract noun from story moral.", "options": ["fear", "time", "marks", "books"]}
]

# More blanks...
for i in range(11, 31):
    blanks.append({
        "question": f"In story {i}, the character showed great ___.",
        "correct_answer": "effort",
        "telugu_meaning": "కథలో క్యారెక్టర్ ఎంతో ప్రయత్నం చూపించింది.",
        "explanation": "Moral term.",
        "options": ["effort", "anger", "laziness", "fear"]
    })

speaking_sentences = [
    "Rahul found a wallet on the road.", "He wanted to return it honestly.",
    "Sai practiced English with an AI app.", "His confidence increased slowly.",
    "Anitha reached college on time.", "Good friends always help each other.",
    "Kiran reduced mobile usage gradually.", "Meena answered the interview confidently.",
    "The interviewer appreciated her communication skills.", "Heavy rain started in the evening.",
    "Two students helped the old man.", "Humanity is more important than money.",
    "Ramu worked hard in the fields.", "His family supported him always.",
    "Priya practiced graphic design daily.", "Learning new skills changes life.",
    "Arjun searched for his phone everywhere.", "The shopkeeper returned the phone safely.",
    "Kind people still exist everywhere.", "Nikhil followed a study timetable.",
    "Preparation removed his exam fear.", "He attended the exam confidently.",
    "The teacher gave useful advice.", "Hard work always gives results.",
    "She started freelancing online.", "The project was completed successfully.",
    "The students practiced coding every day.", "The manager appreciated their teamwork.",
    "Confidence helps during interviews.", "Success comes through continuous practice."
]

speaking = []
for sent in speaking_sentences:
    speaking.append({
        "question": sent,
        "telugu_meaning": "",
        "explanation": "Narrate this story sentence with proper emotion and flow."
    })

def update_concept_data():
    level7, _ = Level.objects.get_or_create(number=7, defaults={'title': 'Interview Preparation & Professional Writing'})
    
    concept, _ = Concept.objects.get_or_create(level=level7, name='Story Writing')
    concept.content = content
    concept.grammar_rules = rules
    concept.examples = examples
    concept.save()
    
    Exercise.objects.filter(concept=concept).delete()
    for b in blanks:
        Exercise.objects.create(
            concept=concept, type='FILL_BLANK', question=b['question'],
            correct_answer=b['correct_answer'], explanation=b['explanation'],
            telugu_meaning=b['telugu_meaning'], options=b['options']
        )
    for s in speaking:
        Exercise.objects.create(
            concept=concept, type='READ_ALOUD', question=s['question'],
            telugu_meaning=s['telugu_meaning'], explanation=s['explanation']
        )
    print("Story Writing (Level 7) updated successfully.")

update_concept_data()
