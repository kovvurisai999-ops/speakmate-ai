import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

# --- VOICE CLARITY DATA ---
clarity_content = "Voice Clarity means speaking in a way that is easy to hear and understand. It involves proper volume, pacing, and enunciation (pronouncing words clearly)."
clarity_rules = """
- Do not mumble; open your mouth sufficiently when speaking.
- Adjust your volume based on the room and the distance of the listener.
- Speak at a moderate pace—not too fast and not too slow.
- Practice reading aloud to improve your articulation and breath control.
"""

clarity_examples = [
    {"en": "Please speak a bit louder.", "te": "దయచేసి కొంచెం గట్టిగా మాట్లాడండి.", "explanation": "Adjusting volume for clarity."},
    {"en": "He mumbled his words.", "te": "అతను తన మాటలను గొణిగాడు.", "explanation": "Opposite of speaking clearly."},
    {"en": "Her voice is very clear and pleasant.", "te": "ఆమె స్వరం చాలా స్పష్టంగా మరియు ఆహ్లాదకరంగా ఉంటుంది.", "explanation": "Good voice clarity."},
    {"en": "Don't speak too fast.", "te": "చాలా వేగంగా మాట్లాడకండి.", "explanation": "Pacing advice for clarity."},
    {"en": "Enunciate every word clearly.", "te": "ప్రతి పదాన్ని స్పష్టంగా ఉచ్చరించండి.", "explanation": "Advice for articulation."},
    {"en": "I couldn't hear you over the noise.", "te": "శబ్దం వల్ల నేను మీ మాట వినలేకపోయాను.", "explanation": "A volume issue."},
    {"en": "Take a deep breath before speaking.", "te": "మాట్లాడే ముందు దీర్ఘ శ్వాస తీసుకోండి.", "explanation": "Breath control tip."},
    {"en": "Clear communication avoids misunderstandings.", "te": "స్పష్టమైన కమ్యూనికేషన్ అపార్థాలను నివారిస్తుంది.", "explanation": "Benefit of clarity."},
    {"en": "She projected her voice to the back of the room.", "te": "ఆమె తన గొంతును గది వెనుక వరకు వినిపించేలా చేసింది.", "explanation": "Good voice projection."},
    {"en": "Reading aloud improves voice clarity.", "te": "బిగ్గరగా చదవడం వల్ల వాయిస్ క్లారిటీ మెరుగుపడుతుంది.", "explanation": "A practice technique."}
]
clarity_examples = (clarity_examples * 5)[:50]

clarity_blanks = [
    {"question": "Please speak a bit ___.", "correct_answer": "louder", "telugu_meaning": "దయచేసి కొంచెం గట్టిగా మాట్లాడండి.", "explanation": "Request for more volume.", "options": ["softer", "louder", "faster", "slower"]},
    {"question": "Do not ___ your words; speak clearly.", "correct_answer": "mumble", "telugu_meaning": "మీ మాటలను గొణగకండి; స్పష్టంగా మాట్లాడండి.", "explanation": "Speaking quietly and unclearly.", "options": ["shout", "sing", "mumble", "yell"]},
    {"question": "You need to ___ every word clearly.", "correct_answer": "enunciate", "telugu_meaning": "మీరు ప్రతి పదాన్ని స్పష్టంగా ఉచ్చరించాలి.", "explanation": "To pronounce clearly.", "options": ["hide", "mumble", "enunciate", "forget"]},
    {"question": "Speak at a moderate ___.", "correct_answer": "pace", "telugu_meaning": "మితమైన వేగంతో మాట్లాడండి.", "explanation": "Speed of speaking.", "options": ["volume", "pace", "pitch", "tone"]},
    {"question": "Take a deep ___ before speaking.", "correct_answer": "breath", "telugu_meaning": "మాట్లాడే ముందు దీర్ఘ శ్వాస తీసుకోండి.", "explanation": "Air taken into the lungs.", "options": ["break", "breath", "step", "look"]}
]
clarity_blanks = (clarity_blanks * 6)[:30]

clarity_speaking = [
    {"question": "Please speak a bit louder.", "telugu_meaning": "దయచేసి కొంచెం గట్టిగా మాట్లాడండి.", "explanation": "Speak with sufficient volume."},
    {"question": "Do not mumble your words.", "telugu_meaning": "మీ మాటలను గొణగకండి.", "explanation": "Enunciate clearly."},
    {"question": "Speak at a normal pace.", "telugu_meaning": "సాధారణ వేగంతో మాట్లాడండి.", "explanation": "Control your speed."},
    {"question": "I can hear you clearly now.", "telugu_meaning": "నేను ఇప్పుడు మీ మాట స్పష్టంగా వినగలను.", "explanation": "Speak with a pleasant tone."},
    {"question": "Voice projection is important.", "telugu_meaning": "గొంతును స్పష్టంగా వినిపించడం ముఖ్యం.", "explanation": "Project your voice confidently."}
]
clarity_speaking = (clarity_speaking * 6)[:30]


# --- CONFIDENCE DATA ---
confidence_content = "Confidence in speaking means believing in your ability to communicate effectively in English, even if you make mistakes. It is about expressing your thoughts without fear or hesitation."
confidence_rules = """
- Accept that making mistakes is a normal part of learning.
- Maintain good eye contact and positive body language.
- Celebrate your small wins and progress.
- Practice in low-pressure environments (like with a mirror or AI) before speaking in public.
"""

confidence_examples = [
    {"en": "She spoke with great confidence.", "te": "ఆమె ఎంతో ఆత్మవిశ్వాసంతో మాట్లాడింది.", "explanation": "Describing confident speech."},
    {"en": "Don't be afraid to make mistakes.", "te": "తప్పులు చేయడానికి భయపడకండి.", "explanation": "Rule for building confidence."},
    {"en": "He maintained eye contact during the presentation.", "te": "ప్రెజెంటేషన్ సమయంలో అతను ఐ కాంటాక్ట్ మెయింటైన్ చేశాడు.", "explanation": "Body language showing confidence."},
    {"en": "Believe in yourself and your abilities.", "te": "మిమ్మల్ని మరియు మీ సామర్థ్యాలను విశ్వసించండి.", "explanation": "Self-motivation."},
    {"en": "I feel nervous when I speak in public.", "te": "నేను పబ్లిక్‌లో మాట్లాడేటప్పుడు భయంగా ఫీలవుతాను.", "explanation": "Opposite of confidence."},
    {"en": "Taking a deep breath calms the nerves.", "te": "దీర్ఘ శ్వాస తీసుకోవడం వల్ల నరాలు శాంతిస్తాయి (భయం పోతుంది).", "explanation": "Tip for nervousness."},
    {"en": "Practice builds confidence.", "te": "ప్రాక్టీస్ చేయడం వల్ల ఆత్మవిశ్వాసం పెరుగుతుంది.", "explanation": "The relationship between practice and confidence."},
    {"en": "Speak clearly and confidently.", "te": "స్పష్టంగా మరియు ఆత్మవిశ్వాసంతో మాట్లాడండి.", "explanation": "Encouraging instruction."},
    {"en": "He gave a confident smile.", "te": "అతను ఆత్మవిశ్వాసంతో కూడిన చిరునవ్వు నవ్వాడు.", "explanation": "Non-verbal confidence."},
    {"en": "Your English is better than you think.", "te": "మీరు అనుకున్నదానికంటే మీ ఇంగ్లీష్ మెరుగ్గా ఉంది.", "explanation": "Reassurance."}
]
confidence_examples = (confidence_examples * 5)[:50]

confidence_blanks = [
    {"question": "Don't be ___ to make mistakes.", "correct_answer": "afraid", "telugu_meaning": "తప్పులు చేయడానికి భయపడవద్దు.", "explanation": "Feeling fear.", "options": ["happy", "proud", "afraid", "glad"]},
    {"question": "Maintain good eye ___ when speaking.", "correct_answer": "contact", "telugu_meaning": "మాట్లాడేటప్పుడు మంచి ఐ కాంటాక్ట్ (కంటి చూపు) నిర్వహించండి.", "explanation": "Looking directly at someone.", "options": ["sight", "contact", "vision", "look"]},
    {"question": "___ builds confidence.", "correct_answer": "Practice", "telugu_meaning": "ప్రాక్టీస్ చేయడం వల్ల ఆత్మవిశ్వాసం పెరుగుతుంది.", "explanation": "Doing something repeatedly to improve.", "options": ["Fear", "Sleep", "Practice", "Worry"]},
    {"question": "She spoke with great ___.", "correct_answer": "confidence", "telugu_meaning": "ఆమె ఎంతో ఆత్మవిశ్వాసంతో మాట్లాడింది.", "explanation": "Belief in oneself.", "options": ["fear", "doubt", "confidence", "hesitation"]},
    {"question": "Take a deep breath to calm your ___.", "correct_answer": "nerves", "telugu_meaning": "మీ భయాన్ని తగ్గించుకోవడానికి దీర్ఘ శ్వాస తీసుకోండి.", "explanation": "Feelings of nervousness.", "options": ["nerves", "eyes", "hands", "feet"]}
]
confidence_blanks = (confidence_blanks * 6)[:30]

confidence_speaking = [
    {"question": "Don't be afraid to make mistakes.", "telugu_meaning": "తప్పులు చేయడానికి భయపడకండి.", "explanation": "Speak with an encouraging tone."},
    {"question": "I believe in myself.", "telugu_meaning": "నేను నన్ను నమ్ముతున్నాను.", "explanation": "Speak with strong conviction."},
    {"question": "Practice builds confidence.", "telugu_meaning": "ప్రాక్టీస్ ఆత్మవిశ్వాసాన్ని పెంచుతుంది.", "explanation": "State it confidently."},
    {"question": "Maintain good eye contact.", "telugu_meaning": "మంచి ఐ కాంటాక్ట్ నిర్వహించండి.", "explanation": "Give advice clearly."},
    {"question": "Speak clearly and confidently.", "telugu_meaning": "స్పష్టంగా మరియు ఆత్మవిశ్వాసంతో మాట్లాడండి.", "explanation": "Demonstrate confidence in your voice."}
]
confidence_speaking = (confidence_speaking * 6)[:30]

def insert_level4_data2(concept_name, content, rules, examples, blanks, speaking):
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

insert_level4_data2('Voice Clarity', clarity_content, clarity_rules, clarity_examples, clarity_blanks, clarity_speaking)
insert_level4_data2('Confidence', confidence_content, confidence_rules, confidence_examples, confidence_blanks, confidence_speaking)
