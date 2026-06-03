import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept, Exercise

def update_basics():
    # 1. GREETINGS
    greetings = Concept.objects.get(slug='greetings')
    greetings.content = """
Greetings are the first step in any conversation. There are two types:
1. Formal: Use with Boss, Teachers, Strangers.
2. Informal: Use with Friends and Family.
    """
    greetings.grammar_rules = """
- Formal: Good morning, Good afternoon, How do you do?
- Informal: Hi, Hello, What's up?, Hey!
    """
    greetings.examples = [
        {"word": "Good Morning", "en": "Good morning! How are you today?", "te": "Subhodayam! Eeroju meeru ela unnaru?", "sound": "Formal", "explanation": "Use this from sunrise until 12:00 PM."},
        {"word": "Good Afternoon", "en": "Good afternoon, sir. Can I help you?", "te": "Madyahna vanakam sir. Nenu meeku help cheyacha?", "sound": "Formal", "explanation": "Use this from 12:00 PM to sunset."},
        {"word": "Hi / Hello", "en": "Hi Rahul! Long time no see.", "te": "Hi Rahul! Chala kalam tarvata kalustunnam.", "sound": "Informal", "explanation": "Standard way to start a friendly conversation."},
        {"word": "What's up?", "en": "Hey man, what's up?", "te": "Hey, em sangathi?", "sound": "Informal", "explanation": "Very casual, use only with close friends."},
        {"word": "How do you do?", "en": "How do you do? It's a pleasure to meet you.", "te": "Meerela unnaru? Mimmalni kalavadam chala santhoshamga undi.", "sound": "Formal", "explanation": "Used when meeting someone for the first time in a formal setting."},
    ]
    greetings.save()

    # 2. SELF INTRODUCTION
    self_intro = Concept.objects.get(slug='self-introduction')
    self_intro.content = """
Self-Introduction is telling people who you are. A good introduction includes:
1. Name
2. Place (Where you are from)
3. Education/Job
4. Hobbies
5. Goal (What you want to become)
    """
    self_intro.grammar_rules = """
- Start with a greeting: "Good morning everyone."
- Name: "I am [Name]" or "My name is [Name]"
- Place: "I am from [Place]" or "I belong to [Place]"
- Education: "I am studying [Degree]" or "I completed [Degree]"
- Hobby: "My hobbies are [Hobbies]"
    """
    self_intro.examples = [
        {"word": "The Opening", "en": "Good morning everyone. I would like to introduce myself.", "te": "Andariki subhodayam. Nannu nenu parichayam chesukovali anukuntunnanu.", "sound": "Step 1", "explanation": "Always start with a polite opening."},
        {"word": "Name & Place", "en": "My name is Kalyan and I am from Hyderabad.", "te": "Naa peru Kalyan mariyu nenu Hyderabad nundi vachanu.", "sound": "Step 2", "explanation": "Simple and clear identification."},
        {"word": "Education", "en": "I am currently pursuing my graduation in Computer Science.", "te": "Nenu prastutam Computer Science lo graduation chaduvutunnanu.", "sound": "Step 3", "explanation": "Tells about your current background."},
        {"word": "Hobbies", "en": "In my free time, I love listening to music and reading books.", "te": "Khali samayam lo, naku music vinadam mariyu books chaduvadam ishtam.", "sound": "Step 4", "explanation": "Shows your personality outside of work/study."},
        {"word": "Goal", "en": "My goal is to become a software engineer in a top company.", "te": "Oka top company lo software engineer avvadam naa lakshyam.", "sound": "Step 5", "explanation": "Shows your ambition and direction."},
    ]
    self_intro.save()
    print("Greetings and Self Introduction updated successfully!")

if __name__ == "__main__":
    update_basics()
