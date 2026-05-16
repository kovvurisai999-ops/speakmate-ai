import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept, Exercise

def update_alphabets():
    concept = Concept.objects.get(slug='alphabets')
    
    # 50 Structured Examples
    alphabet_examples = [
        {"en": "I eat an apple every day.", "te": "Nenu prati roju apple tintanu.", "explanation": "A for Apple: 'I' is subject, 'eat' is verb, 'apple' is object."},
        {"en": "The aeroplane is flying in the sky.", "te": "Aeroplane aakasam lo eguruthundi.", "explanation": "A for Aeroplane: Describes a continuous action in the sky."},
        {"en": "The boy is playing with a ball.", "te": "Abbayi ball tho aaduthunnadu.", "explanation": "B for Ball: 'The boy' is subject, 'is playing' is action."},
        {"en": "She is reading a book.", "te": "Ame book chaduthundi.", "explanation": "B for Book: 'She' is subject, 'book' is object."},
        {"en": "The cat is sleeping on the sofa.", "te": "Pilli sofa pai padukundi.", "explanation": "C for Cat: Shows position using preposition 'on'."},
        {"en": "My father drives a car.", "te": "Naa father car naduptharu.", "explanation": "C for Car: 'Drives' is the verb for vehicle operation."},
        {"en": "The dog is barking loudly.", "te": "Kukka gattiga arustundi.", "explanation": "D for Dog: 'Loudly' is an adverb describing the barking."},
        {"en": "Please close the door.", "te": "Dayachesi door close cheyyi.", "explanation": "D for Door: This is an imperative sentence (request)."},
        {"en": "The elephant is very big.", "te": "Enugu chala pedda ga untundi.", "explanation": "E for Elephant: Uses adjective 'big' to describe size."},
        {"en": "I eat boiled eggs every morning.", "te": "Nenu prati morning boiled eggs tintanu.", "explanation": "E for Egg: Describes a daily habit."},
        {"en": "The fish is swimming in water.", "te": "Chepa neetilo swim chestundi.", "explanation": "F for Fish: Shows an ongoing action."},
        {"en": "The fan is rotating fast.", "te": "Fan fast gaa tiruguthundi.", "explanation": "F for Fan: 'Fast' describes the speed of rotation."},
        {"en": "The girl is singing a song.", "te": "Ammayi paata paaduthundi.", "explanation": "G for Girl: 'Singing' is the present continuous action."},
        {"en": "There are many flowers in the garden.", "te": "Garden lo chala puvvulu unnayi.", "explanation": "G for Garden: Uses 'There are' to show existence."},
        {"en": "Their house is very beautiful.", "te": "Valla illu chala andamga undi.", "explanation": "H for House: Describes ownership and beauty."},
        {"en": "The hen lays eggs daily.", "te": "Kodi prati roju eggs peduthundi.", "explanation": "H for Hen: 'Lays' is the specific verb for eggs."},
        {"en": "Children love ice cream.", "te": "Pillalu ice cream ni ishtapadtharu.", "explanation": "I for Ice Cream: Shows a general preference."},
        {"en": "The pen has blue ink.", "te": "Pen lo blue ink undi.", "explanation": "I for Ink: Describes the content of the pen."},
        {"en": "She drinks orange juice daily.", "te": "Ame orange juice taguthundi.", "explanation": "J for Juice: Describes a healthy daily habit."},
        {"en": "The joker made everyone laugh.", "te": "Joker andarini navvinchadu.", "explanation": "J for Joker: Shows how someone influenced others' emotions."},
        {"en": "The kite is flying high.", "te": "Gaalipata ekkuvaga eguruthundi.", "explanation": "K for Kite: 'High' is the adverb of position."},
        {"en": "I lost my room key.", "te": "Naa room key pogottanu.", "explanation": "K for Key: Describes a past event (losing something)."},
        {"en": "The lion is the king of the jungle.", "te": "Simham adavi raju.", "explanation": "L for Lion: A well-known fact/title."},
        {"en": "I use my laptop for study.", "te": "Nenu study kosam laptop use chestanu.", "explanation": "L for Laptop: Shows the purpose of an object."},
        {"en": "Mango is my favorite fruit.", "te": "Mamidi naa favorite fruit.", "explanation": "M for Mango: Expresses personal taste."},
        {"en": "My mobile battery is low.", "te": "Naa mobile battery takkuvaga undi.", "explanation": "M for Mobile: Describes the current state of a device."},
        {"en": "Birds build nests on trees.", "te": "Pakshulu chetla pai nests kattukuntayi.", "explanation": "N for Nest: Describes a natural behavior of birds."},
        {"en": "The nurse helped the patient.", "te": "Nurse patient ki help chesindi.", "explanation": "N for Nurse: A past action of helping someone."},
        {"en": "The orange tastes sweet.", "te": "Orange sweet gaa untundi.", "explanation": "O for Orange: Describes the sensory taste of food."},
        {"en": "The owl can see at night.", "te": "Gudlaguba ratri choostundi.", "explanation": "O for Owl: Describes a specific ability ('can see')."},
        {"en": "This pen writes smoothly.", "te": "Ee pen smooth gaa rayuthundi.", "explanation": "P for Pen: 'Smoothly' describes the quality of writing."},
        {"en": "My phone is ringing.", "te": "Naa phone ring avutundi.", "explanation": "P for Phone: An immediate action happening now."},
        {"en": "The queen wore a golden crown.", "te": "Rani golden crown dharinchindi.", "explanation": "Q for Queen: Describes the appearance of royalty."},
        {"en": "The teacher asked a question.", "te": "Teacher oka question adigaru.", "explanation": "Q for Question: A past action in a classroom."},
        {"en": "The rabbit is eating carrots.", "te": "Kundelu carrots tintundi.", "explanation": "R for Rabbit: Shows the diet of an animal."},
        {"en": "It is raining heavily today.", "te": "Eeroju chala varsham paduthundi.", "explanation": "R for Rain: Describes weather intensity."},
        {"en": "The sun rises in the east.", "te": "Suryudu turpu lo udhayistadu.", "explanation": "S for Sun: A universal geographical fact."},
        {"en": "Students go to school daily.", "te": "Students prati roju school ki veltharu.", "explanation": "S for School: A regular routine for learners."},
        {"en": "The tiger runs very fast.", "te": "Puli chala fast gaa parigeduthundi.", "explanation": "T for Tiger: Highlights the speed of the animal."},
        {"en": "The books are on the table.", "te": "Books table pai unnayi.", "explanation": "T for Table: Uses 'on' to show location."},
        {"en": "I carry an umbrella during rain.", "te": "Varsham lo umbrella teesukuntanu.", "explanation": "U for Umbrella: Shows preparation for weather."},
        {"en": "Students wear uniforms at school.", "te": "Students school lo uniforms vestharu.", "explanation": "U for Uniform: Describes a mandatory dress code."},
        {"en": "The van stopped near the gate.", "te": "Van gate daggara aagindi.", "explanation": "V for Van: Describes a past action of stopping."},
        {"en": "My grandparents live in a village.", "te": "Naa grandparents village lo untaru.", "explanation": "V for Village: Describes residence/location."},
        {"en": "We should drink enough water.", "te": "Manam saripoyina neeru tagali.", "explanation": "W for Water: Uses 'should' for a healthy advice."},
        {"en": "My watch shows the correct time.", "te": "Naa watch correct time chupisthundi.", "explanation": "W for Watch: Describes the function of a timekeeper."},
        {"en": "The child is playing the xylophone.", "te": "Pillavadu xylophone aaduthunnadu.", "explanation": "X for Xylophone: Describes a musical activity."},
        {"en": "The yacht is floating on the sea.", "te": "Yacht samudram pai teeluthundi.", "explanation": "Y for Yacht: Shows a state of floating."},
        {"en": "Yellow is my favorite color.", "te": "Pasupu naa favorite color.", "explanation": "Y for Yellow: Expresses color preference."},
        {"en": "The zebra has black and white stripes.", "te": "Zebra ki black and white lines untayi.", "explanation": "Z for Zebra: Describes the physical pattern of the animal."},
    ]
    
    concept.examples = alphabet_examples
    concept.content = """# Phase 1: Concept Learning — Alphabets

## What are Alphabets?

Alphabets ante:

**“English language lo unna basic letters.”**

English lo total:

**26 Alphabets untayi.**

From:

**A to Z**

I alphabets words, sentences, communication, spoken English anni build cheyyadaniki foundation."""
    concept.save()
    
    # Also add some exercises for Phase 3
    for ex in alphabet_examples[:10]:
        q = ex['en'].replace(" ", " ___ ", 1) # Simple fill blank
        ans = ex['en'].split()[1]
        Exercise.objects.get_or_create(
            concept=concept,
            question=ex['en'].replace(ans, "___"),
            defaults={'correct_answer': ans, 'explanation': ex['explanation'], 'type': 'FILL_BLANK'}
        )
    print("Alphabets successfully updated with 50 examples!")

if __name__ == "__main__":
    update_alphabets()
