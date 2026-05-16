from roadmap.models import Concept

def update_vocabulary():
    # 1. Daily Vocabulary
    daily = Concept.objects.get(slug='daily-vocabulary')
    daily.content = "Mastering everyday words used in common situations like home, shopping, and commuting."
    daily.examples = [
        {"word": "Grocery", "en": "I need to buy some groceries.", "te": "Nenu konni sarakulu konali.", "sound": "Home", "explanation": "Common household items."},
        {"word": "Commute", "en": "How do you commute to work?", "te": "Meeru pani ki ela veltharu?", "sound": "Travel", "explanation": "Traveling between home and work."},
        {"word": "Errand", "en": "I have a few errands to run.", "te": "Naku konni chillara panulu unnayi.", "sound": "Task", "explanation": "Short trips to do jobs."},
    ]
    daily.save()

    # 2. Business Vocabulary
    business = Concept.objects.get(slug='business-vocabulary')
    business.content = "Professional English words used in office, meetings, and emails."
    business.examples = [
        {"word": "Agenda", "en": "What is the agenda for today's meeting?", "te": "Eeroju meeting agenda enti?", "sound": "Office", "explanation": "A list of items to be discussed."},
        {"word": "Deadline", "en": "The deadline for this project is Friday.", "te": "Ee project deadline sukravaram.", "sound": "Task", "explanation": "The latest time by which something must be done."},
        {"word": "Brainstorm", "en": "Let's brainstorm some new ideas.", "te": "Kotha ideas gurinchi alochincham.", "sound": "Creative", "explanation": "Group discussion to produce ideas."},
    ]
    business.save()

    print("Vocabulary sections updated!")

if __name__ == "__main__":
    update_vocabulary()
