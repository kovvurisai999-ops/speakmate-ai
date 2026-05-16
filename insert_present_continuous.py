import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

def run():
    print("Adding Present Continuous...")
    
    level2, _ = Level.objects.get_or_create(
        number=2, 
        defaults={'title': 'Grammar Concepts', 'description': 'Mastering Tenses and Sentence formation'}
    )
    
    concept, _ = Concept.objects.get_or_create(
        name="Present Continuous",
        defaults={
            'slug': 'present-continuous',
            'level': level2
        }
    )
    
    concept.content = """# Phase 1 Concept Learning: Present Continuous Tense
Present Continuous tense present moment lo ippudu jarugutunna action ni cheppadaniki use chestaru.

## Structure
**Subject + am/is/are + verb+ing**

### Examples:
* I **am** eating.
* She **is** studying.
* They **are** playing."""
    
    # Phase 2 Examples (we'll just reuse phase 3 sentences for examples since none were provided)
    examples = [
        {"en": "I am eating.", "te": "Nenu tintunnanu.", "explanation": "Present action", "category": "general"},
        {"en": "She is studying.", "te": "Ame chadutundi.", "explanation": "Present action", "category": "education"},
        {"en": "They are playing.", "te": "Vallu aadutunnaru.", "explanation": "Present action", "category": "sports"},
    ]
    concept.examples = examples
    concept.save()

    # Clear old exercises
    Exercise.objects.filter(concept=concept).delete()

    # Phase 3
    fb_data = [
        ("She ___ studying for her exams now.", "is", "Ame ippudu exams kosam chadutundi.", "“She” singular subject kabatti “is” use chesam."),
        ("I ___ drinking coffee right now.", "am", "Nenu ippudu coffee tagutunnanu.", "“I” subject ki Present Continuous lo “am” use chestaru."),
        ("They ___ playing cricket in the ground.", "are", "Vallu ground lo cricket aadutunnaru.", "“They” plural subject kabatti “are” use chesam."),
        ("My brother ___ watching YouTube videos.", "is", "Na brother YouTube videos chustunnadu.", "“My brother” singular kabatti “is” use chesam."),
        ("We ___ attending an online class now.", "are", "Memu ippudu online class attend chestunnam.", "“We” plural subject kabatti “are” use chesam."),
        ("The baby ___ sleeping peacefully.", "is", "Baby prashantanga nidrapotundi.", "“The baby” singular subject kabatti “is” use chesam."),
        ("I ___ learning spoken English.", "am", "Nenu spoken English nerchukuntunnanu.", "Present lo ongoing action kabatti Present Continuous use chesam."),
        ("She ___ talking to her friend on the phone.", "is", "Ame phone lo friend tho matladutundi.", "Current action jarugutundi kabatti “is talking” use chesam."),
        ("The students ___ writing the test now.", "are", "Students ippudu test rastunnaru.", "“Students” plural kabatti “are” use chesam."),
        ("My mother ___ cooking dinner in the kitchen.", "is", "Na mother kitchen lo dinner cook chestundi.", "Present action ongoing lo undi kabatti Present Continuous use chesam."),
        ("The dog ___ barking loudly.", "is", "Kukka gattiga morugutundi.", "Single animal subject kabatti “is” use chesam."),
        ("We ___ waiting for the bus.", "are", "Memu bus kosam wait chestunnam.", "“We” plural subject kabatti “are waiting” use chesam."),
        ("My father ___ driving the car carefully.", "is", "Na father jagrathaga car drive chestunnaru.", "Current driving action jarugutundi kabatti Present Continuous use chesam."),
        ("The teacher ___ explaining the lesson.", "is", "Teacher lesson explain chestunnaru.", "Singular subject “teacher” ki “is” use chestaru."),
        ("They ___ watching a movie tonight.", "are", "Vallu eeroju night movie chustunnaru.", "Future arrangement kosam kuda Present Continuous use chestaru."),
        ("I ___ preparing for my interview.", "am", "Nenu interview kosam prepare avutunnanu.", "Present lo jarugutunna preparation ni indicate chestundi."),
        ("The children ___ playing in the park.", "are", "Pillalu park lo aadutunnaru.", "Plural subject “children” kabatti “are” use chesam."),
        ("She ___ wearing a blue dress today.", "is", "Ame eeroju blue dress vesukundi.", "Temporary present situation ni cheppadaniki use chesam."),
        ("We ___ discussing the project now.", "are", "Memu ippudu project gurinchi discuss chestunnam.", "Current discussion ongoing lo undi."),
        ("The rain ___ falling heavily outside.", "is", "Bayata heavy rain padutundi.", "Nature ongoing action ni Present Continuous lo cheppam."),
        ("My sister ___ cleaning her room.", "is", "Ame room clean chestundi.", "Singular subject"),
        ("They ___ studying together in the library.", "are", "Vallu library lo chaduvutunnaru.", "Plural subject"),
        ("I ___ listening to music now.", "am", "Nenu music vintunnanu.", "I verb"),
        ("The chef ___ preparing delicious food.", "is", "Chef food prepare chestunnadu.", "Singular subject"),
        ("We ___ planning a trip for next month.", "are", "Memu trip plan chestunnam.", "Plural subject"),
        ("My friend ___ learning Python programming.", "is", "Na friend Python nerchukuntunnadu.", "Singular subject"),
        ("The workers ___ repairing the road.", "are", "Workers road repair chestunnaru.", "Plural subject"),
        ("She ___ practicing English daily.", "is", "Ame English practice chestundi.", "Singular subject"),
        ("I ___ searching for my mobile phone.", "am", "Nenu na phone vetukutunnanu.", "I verb"),
        ("The boys ___ playing football after school.", "are", "Boys football aadutunnaru.", "Plural subject"),
    ]

    for q, a, te, exp in fb_data:
        Exercise.objects.create(
            concept=concept,
            type='FILL_BLANK',
            question=q,
            correct_answer=a,
            telugu_meaning=te,
            explanation=exp,
            category='General'
        )

    # Phase 4
    sp_sentences = [
        "I am learning spoken English every day.",
        "She is talking to her teacher now.",
        "They are playing cricket in the ground.",
        "My mother is cooking dinner.",
        "We are attending an online meeting.",
        "The students are writing the exam.",
        "I am practicing English pronunciation.",
        "My brother is watching television.",
        "The baby is sleeping peacefully.",
        "She is preparing for her interview.",
        "We are waiting for the train.",
        "The teacher is explaining grammar concepts.",
        "I am improving my communication skills.",
        "My friends are discussing the project.",
        "The dog is barking loudly outside.",
        "They are learning new vocabulary words.",
        "My father is driving carefully.",
        "The children are playing happily.",
        "I am reading an English newspaper.",
        "She is speaking confidently in English.",
        "We are planning a family trip.",
        "The rain is falling heavily today.",
        "I am listening to English podcasts.",
        "My sister is learning coding online.",
        "They are practicing for the competition.",
        "The workers are repairing the building.",
        "She is wearing a beautiful dress.",
        "We are cleaning our classroom now.",
        "I am preparing for my final exams.",
        "The manager is speaking with the employees."
    ]

    for sentence in sp_sentences:
        Exercise.objects.create(
            concept=concept,
            type='READ_ALOUD',
            question=sentence,
            difficulty='Beginner',
            category='General'
        )

    print("Success! Present Continuous has been populated.")

if __name__ == '__main__':
    run()
