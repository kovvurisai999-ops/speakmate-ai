from django.core.management.base import BaseCommand
from roadmap.models import Level, Concept

class Command(BaseCommand):
    help = 'Seeds the updated 7-category Spoken English Roadmap'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Level.objects.all().delete()
        
        roadmap_data = [
            {
                "number": 1,
                "title": "BASIC ENGLISH CONCEPTS",
                "description": "Foundational blocks for beginners",
                "concepts": [
                    {"name": "Alphabets", "slug": "alphabets"},
                    {"name": "Phonics", "slug": "phonics"},
                    {"name": "Greetings", "slug": "greetings"},
                    {"name": "Self Introduction", "slug": "self-introduction"},
                    {"name": "Daily Words", "slug": "daily-words"},
                    {"name": "Family Vocabulary", "slug": "family-vocabulary"},
                    {"name": "Numbers", "slug": "numbers"},
                    {"name": "Colors", "slug": "colors"},
                    {"name": "Days & Months", "slug": "days-months"},
                    {"name": "Simple Sentences", "slug": "simple-sentences"},
                ]
            },
            {
                "number": 2,
                "title": "GRAMMAR CONCEPTS (MOST IMPORTANT)",
                "description": "Mastering Tenses and Sentence formation",
                "concepts": [
                    {"name": "Simple Present", "slug": "simple-present", "formula": "Subject + Verb(s/es) + Object"},
                    {"name": "Present Continuous", "slug": "present-continuous", "formula": "Subject + is/am/are + V1+ing + Object"},
                    {"name": "Present Perfect", "slug": "present-perfect", "formula": "Subject + has/have + V3 + Object"},
                    {"name": "Present Perfect Continuous", "slug": "present-perfect-continuous"},
                    {"name": "Simple Past", "slug": "simple-past", "formula": "Subject + V2 + Object"},
                    {"name": "Past Continuous", "slug": "past-continuous"},
                    {"name": "Past Perfect", "slug": "past-perfect"},
                    {"name": "Past Perfect Continuous", "slug": "past-perfect-continuous"},
                    {"name": "Simple Future", "slug": "simple-future", "formula": "Subject + will/shall + V1 + Object"},
                    {"name": "Future Continuous", "slug": "future-continuous"},
                    {"name": "Future Perfect", "slug": "future-perfect"},
                    {"name": "Future Perfect Continuous", "slug": "future-perfect-continuous"},
                    {"name": "Nouns", "slug": "nouns"},
                    {"name": "Pronouns", "slug": "pronouns"},
                    {"name": "Verbs", "slug": "verbs"},
                    {"name": "Helping Verbs", "slug": "helping-verbs"},
                    {"name": "Articles", "slug": "articles"},
                    {"name": "Prepositions", "slug": "prepositions"},
                ]
            },
            {
                "number": 3,
                "title": "VOCABULARY TYPES",
                "description": "Expand your word bank for different situations",
                "concepts": [
                    {"name": "Daily Vocabulary", "slug": "daily-vocabulary"},
                    {"name": "Business Vocabulary", "slug": "business-vocabulary"},
                    {"name": "Travel Vocabulary", "slug": "travel-vocabulary"},
                    {"name": "Food Vocabulary", "slug": "food-vocabulary"},
                    {"name": "Emotional Vocabulary", "slug": "emotional-vocabulary"},
                ]
            },
            {
                "number": 4,
                "title": "SPEAKING SKILL TYPES",
                "description": "Master the art of speaking fluently",
                "concepts": [
                    {"name": "Fluency", "slug": "fluency"},
                    {"name": "Pronunciation", "slug": "pronunciation"},
                    {"name": "Accent", "slug": "accent"},
                    {"name": "Voice Clarity", "slug": "voice-clarity"},
                    {"name": "Confidence", "slug": "confidence"},
                ]
            },
            {
                "number": 5,
                "title": "CONVERSATION TYPES",
                "description": "Real-world interaction practice",
                "concepts": [
                    {"name": "Daily Conversation", "slug": "daily-conversation"},
                    {"name": "Shopping", "slug": "shopping-convo"},
                    {"name": "Office", "slug": "office-convo"},
                    {"name": "Travel", "slug": "travel-convo"},
                    {"name": "Presentation", "slug": "presentation-skills"},
                ]
            },
            {
                "number": 6,
                "title": "PRONUNCIATION TYPES",
                "description": "Speak like a native with correct sounds",
                "concepts": [
                    {"name": "Silent Letters", "slug": "silent-letters"},
                    {"name": "Word Stress", "slug": "word-stress"},
                    {"name": "Tongue Twisters", "slug": "tongue-twisters"},
                    {"name": "Difficult Words", "slug": "difficult-words"},
                ]
            },
            {
                "number": 7,
                "title": "WRITING TYPES",
                "description": "Master professional and creative writing",
                "concepts": [
                    {"name": "Email Writing", "slug": "email-writing"},
                    {"name": "Formal Writing", "slug": "formal-writing"},
                    {"name": "Story Writing", "slug": "story-writing"},
                ]
            }
        ]

        for l_data in roadmap_data:
            level = Level.objects.create(
                number=l_data["number"],
                title=l_data["title"],
                description=l_data["description"]
            )
            for c_data in l_data["concepts"]:
                Concept.objects.create(
                    level=level,
                    name=c_data["name"],
                    slug=c_data["slug"],
                    formula=c_data.get("formula", ""),
                    content=f"Detailed learning material for {c_data['name']}.",
                    grammar_rules="1. Rule one.\n2. Rule two.",
                    examples=[
                        {"en": f"I {c_data['name']} daily.", "te": f"Nenu daily {c_data['name']} chestanu.", "explanation": f"Basic use of {c_data['name']}."}
                    ],
                    common_mistakes=[
                        {"wrong": f"He {c_data['name']}", "right": f"He {c_data['name']}s", "why": "Singular subject verb rule."}
                    ]
                )
        
        self.stdout.write(self.style.SUCCESS('Roadmap successfully updated to the new 7-category structure!'))
