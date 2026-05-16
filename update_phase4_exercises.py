import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept, Exercise

def add_read_aloud_exercises(concept_slug, phrases):
    try:
        concept = Concept.objects.get(slug=concept_slug)
        print(f"Updating Phase 4 (Read Aloud) for {concept_slug}...")
        # Overwrite existing READ_ALOUD exercises for this concept
        Exercise.objects.filter(concept=concept, type='READ_ALOUD').delete()
        
        for phrase in phrases:
            Exercise.objects.create(
                concept=concept,
                type='READ_ALOUD',
                question=phrase,
                correct_answer=phrase # For READ_ALOUD, the question is the target phrase
            )
        print(f"Finished {concept_slug}. Total: {len(phrases)}")
    except Concept.DoesNotExist:
        print(f"Concept {concept_slug} not found.")

def main():
    data = {
        "alphabets": [
            "A is for Apple.", "B is for Ball.", "C is for Cat.", "D is for Dog.", "E is for Elephant.",
            "F is for Fish.", "G is for Goat.", "H is for House.", "I is for Ice cream.", "J is for Juice.",
            "K is for Kite.", "L is for Lion.", "M is for Mango.", "N is for Nest.", "O is for Orange.",
            "P is for Pencil.", "Q is for Queen.", "R is for Rabbit.", "S is for Sun.", "T is for Tiger."
        ],
        "phonics": [
            "The cat sat on the mat.", "Sam sells soft socks.", "The ship is near the shore.", "Fish swim in fresh water.", "The boy plays with toys.",
            "I see three trees.", "The clock clicks loudly.", "She drinks hot tea.", "The bird sings sweetly.", "Please close the door quietly.",
            "The train travels fast.", "Tom threw the ball.", "The baby sleeps peacefully.", "Green grass grows quickly.", "The black dog barked loudly.",
            "A big bus stopped suddenly.", "The king wore a crown.", "The rain falls heavily.", "She smiled happily.", "The school bell rang loudly."
        ],
        "greetings": [
            "Good morning, Sir.", "Hello, how are you?", "Good evening, everyone.", "Nice to meet you.", "How is your day going?",
            "Welcome to our college.", "Hey, what’s up?", "Good afternoon, Madam.", "Have a nice day.", "See you tomorrow.",
            "Thank you for coming.", "Good night, take care.", "How have you been?", "It’s good to see you again.", "Please come inside.",
            "Glad to meet you.", "Wish you a happy birthday.", "Good luck for your exam.", "Hope you are doing well.", "Have a safe journey."
        ],
        "self-introduction": [
            "My name is Sai Krishna.", "I am from Andhra Pradesh.", "I completed my degree recently.", "I am learning spoken English.", "My hobby is playing cricket.",
            "I want to become a software engineer.", "My father is a farmer.", "I have one elder sister.", "I enjoy learning new skills.", "I am good at communication.",
            "I can work under pressure.", "I like teamwork.", "I am a quick learner.", "I completed my project successfully.", "My goal is to get a good job.",
            "I love coding and technology.", "I am improving my confidence daily.", "I believe in hard work.", "Thank you for this opportunity.", "This is all about me."
        ],
        "daily-words": [
            "I drink water every morning.", "She eats breakfast at 8 AM.", "I go to college daily.", "My mother cooks food.", "The baby is sleeping.",
            "I clean my room daily.", "My father reads newspapers.", "I use my laptop for study.", "The bus arrived late today.", "I completed my homework.",
            "She watches television at night.", "The teacher explained the lesson.", "I bought vegetables from the market.", "My friend called me yesterday.", "We play games together.",
            "I charge my phone daily.", "The fan is rotating slowly.", "The lights are very bright.", "I switched off the computer.", "My brother studies at night."
        ],
        "family-vocabulary": [
            "My father works hard every day.", "My mother makes delicious food.", "My sister is preparing for exams.", "My brother plays football.", "My grandparents live in a village.",
            "I love my family very much.", "My uncle owns a business.", "My aunt teaches at school.", "My cousin studies engineering.", "We celebrate festivals together.",
            "My father drives carefully.", "My mother wakes up early.", "My sister sings beautifully.", "My brother repaired the computer.", "My grandmother tells stories.",
            "My grandfather reads books daily.", "We eat dinner together.", "My family supports my dreams.", "My parents encourage me always.", "I feel happy with my family."
        ],
        "numbers": [
            "I have two brothers.", "My class starts at 9 AM.", "I bought three notebooks.", "There are five chairs in the room.", "My sister is ten years old.",
            "I drank two glasses of water.", "The movie starts at 7 PM.", "We planted ten trees.", "The meeting lasted for two hours.", "I solved twenty questions.",
            "My father owns two bikes.", "The train arrived after fifteen minutes.", "There are seven days in a week.", "I attended three online classes.", "My grandmother is seventy years old.",
            "I paid one hundred rupees.", "The library has one thousand books.", "I completed my work in thirty minutes.", "My friend sent five photos.", "The mall has five floors."
        ],
        "colors": [
            "I bought a red shirt.", "The sky is blue today.", "My bike is black.", "The leaves are green.", "She likes pink dresses.",
            "The mango is yellow.", "I painted my room white.", "The rose flower is red.", "He wears a blue cap.", "My sister bought a purple bag.",
            "The cat has white fur.", "I like brown shoes.", "The signal turned green.", "She uses a black mobile phone.", "The sunset looks orange.",
            "My school bag is dark blue.", "The wall is painted light green.", "He bought a silver watch.", "The baby is wearing a yellow dress.", "My friend drives a white car."
        ],
        "days-months": [
            "My exam starts on Monday.", "I was born in August.", "We have a meeting on Friday.", "My birthday is in December.", "The office is closed on Saturday.",
            "Schools reopen in June.", "I play cricket every Sunday.", "The festival comes in October.", "I have an interview on Tuesday.", "We celebrate Christmas in December.",
            "My sister got married in February.", "The movie releases on Friday.", "I submitted my project on Wednesday.", "My college reopens in June.", "We visited Tirupati in May.",
            "My brother joined college in September.", "I clean my room every Saturday.", "We celebrate Independence Day in August.", "The shop opens on Monday.", "New classes start in July."
        ],
        "simple-sentences": [
            "I drink coffee every morning.", "She goes to college daily.", "My father works in a bank.", "I play cricket with friends.", "We watch movies together.",
            "My mother cooks tasty food.", "The baby is sleeping.", "I wake up at 6 AM.", "He drives carefully.", "My sister likes music.",
            "The bus arrived late.", "I completed my homework.", "They are playing football.", "My friend bought a laptop.", "The teacher explained the lesson.",
            "I am learning spoken English.", "My brother watches YouTube daily.", "We visited Hyderabad last month.", "The dog barked loudly.", "She speaks English fluently"
        ]
    }

    for slug, phrases in data.items():
        add_read_aloud_exercises(slug, phrases)

if __name__ == "__main__":
    main()
