import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept

def run():
    print("Updating Present Continuous Phase 2 (Examples)...")
    
    concept = Concept.objects.get(slug='present-continuous')
    
    examples = [
        {"en": "She is studying for her exams.", "te": "Ame exams kosam chadutundi.", "explanation": "Present moment lo action ongoing lo undi kabatti Present Continuous use chesam."},
        {"en": "I am drinking coffee now.", "te": "Nenu ippudu coffee tagutunnanu.", "explanation": "Current action jarugutundi kabatti “am drinking” use chesam."},
        {"en": "They are playing cricket outside.", "te": "Vallu bayata cricket aadutunnaru.", "explanation": "Plural subject “they” kabatti “are playing” use chesam."},
        {"en": "My mother is cooking dinner.", "te": "Na mother dinner prepare chestundi.", "explanation": "Present lo cooking action jarugutundi."},
        {"en": "We are attending an online class.", "te": "Memu online class attend chestunnam.", "explanation": "Current activity ongoing lo undi kabatti Present Continuous use chesam."},
        {"en": "The baby is sleeping peacefully.", "te": "Baby prashantanga nidrapotundi.", "explanation": "Present lo sleeping action continue avutundi."},
        {"en": "I am learning spoken English daily.", "te": "Nenu daily spoken English nerchukuntunnanu.", "explanation": "Learning process ongoing ga undi kabatti Present Continuous use chesam."},
        {"en": "She is talking to her friend.", "te": "Ame tana friend tho matladutundi.", "explanation": "Current conversation ni indicate chestundi."},
        {"en": "The students are writing the exam.", "te": "Students exam rastunnaru.", "explanation": "Exam writing present lo jarugutundi."},
        {"en": "My father is driving the car.", "te": "Na father car drive chestunnaru.", "explanation": "Driving action ippudu jarugutundi."},
        {"en": "The teacher is explaining the lesson.", "te": "Teacher lesson explain chestunnaru.", "explanation": "Present explanation ongoing lo undi."},
        {"en": "We are waiting for the bus.", "te": "Memu bus kosam wait chestunnam.", "explanation": "Waiting action current situation lo undi."},
        {"en": "My sister is cleaning her room.", "te": "Na sister tana room clean chestundi.", "explanation": "Cleaning action present lo jarugutundi."},
        {"en": "The dog is barking loudly.", "te": "Kukka gattiga morugutundi.", "explanation": "Current sound/action ni describe chestundi."},
        {"en": "I am preparing for my interview.", "te": "Nenu interview kosam prepare avutunnanu.", "explanation": "Preparation ongoing process kabatti Present Continuous use chesam."},
        {"en": "They are watching a movie now.", "te": "Vallu ippudu movie chustunnaru.", "explanation": "Movie watching present moment lo jarugutundi."},
        {"en": "The children are playing in the park.", "te": "Pillalu park lo aadutunnaru.", "explanation": "Present action plural subject tho use chesam."},
        {"en": "She is wearing a blue dress.", "te": "Ame blue dress vesukundi.", "explanation": "Temporary present situation ni describe chestundi."},
        {"en": "We are discussing the project.", "te": "Memu project gurinchi discuss chestunnam.", "explanation": "Discussion present lo continue avutundi."},
        {"en": "The rain is falling heavily.", "te": "Heavy rain padutundi.", "explanation": "Nature ongoing action ni describe chestundi."},
        {"en": "I am listening to music.", "te": "Nenu music vintunnanu.", "explanation": "Listening action current ga jarugutundi."},
        {"en": "My friend is learning Python.", "te": "Na friend Python nerchukuntunnadu.", "explanation": "Learning process ongoing ga undi."},
        {"en": "The workers are repairing the road.", "te": "Workers road repair chestunnaru.", "explanation": "Repair work present lo continue avutundi."},
        {"en": "She is practicing English pronunciation.", "te": "Ame English pronunciation practice chestundi.", "explanation": "Practice ongoing activity kabatti Present Continuous use chesam."},
        {"en": "I am searching for my mobile phone.", "te": "Nenu na mobile kosam vethukutunnanu.", "explanation": "Searching action ippudu jarugutundi."},
        {"en": "The boys are playing football.", "te": "Abbayilu football aadutunnaru.", "explanation": "Plural subject + ongoing action use chesam."},
        {"en": "My uncle is reading the newspaper.", "te": "Na uncle newspaper chadutunnaru.", "explanation": "Reading action current moment lo jarugutundi."},
        {"en": "We are planning a family trip.", "te": "Memu family trip plan chestunnam.", "explanation": "Future arrangement kosam kuda Present Continuous use chestaru."},
        {"en": "She is singing beautifully.", "te": "Ame andamga paadutundi.", "explanation": "Current performance/action ni describe chestundi."},
        {"en": "I am improving my communication skills.", "te": "Nenu communication skills improve cheskuntunnanu.", "explanation": "Improvement ongoing process kabatti Present Continuous use chesam."},
        {"en": "The chef is preparing delicious food.", "te": "Chef tasty food prepare chestunnaru.", "explanation": "Cooking process present lo jarugutundi."},
        {"en": "My brother is using the laptop now.", "te": "Na brother ippudu laptop use chestunnadu.", "explanation": "Current usage/action ni describe chestundi."},
        {"en": "The manager is speaking with employees.", "te": "Manager employees tho matladutunnaru.", "explanation": "Conversation present lo continue avutundi."},
        {"en": "We are practicing interview questions.", "te": "Memu interview questions practice chestunnam.", "explanation": "Practice ongoing action kabatti Present Continuous use chesam."},
        {"en": "The girl is drawing a picture.", "te": "A ammayi bomma draw chestundi.", "explanation": "Drawing action present lo jarugutundi."},
        {"en": "I am watching an English movie.", "te": "Nenu English movie chustunnanu.", "explanation": "Watching current activity ni indicate chestundi."},
        {"en": "My cousin is preparing for IELTS.", "te": "Na cousin IELTS kosam prepare avutunnadu.", "explanation": "Preparation ongoing ga undi."},
        {"en": "They are decorating the hall.", "te": "Vallu hall decorate chestunnaru.", "explanation": "Current work/action ni Present Continuous lo cheppam."},
        {"en": "She is typing an email now.", "te": "Ame ippudu email type chestundi.", "explanation": "Typing action present lo continue avutundi."},
        {"en": "The doctor is checking the patient.", "te": "Doctor patient ni check chestunnaru.", "explanation": "Current medical action ni indicate chestundi."},
        {"en": "I am attending a webinar.", "te": "Nenu webinar attend chestunnanu.", "explanation": ""},
        {"en": "My parents are talking about my future.", "te": "Na parents na future gurinchi matladutunnaru.", "explanation": ""},
        {"en": "The students are preparing a project.", "te": "Students project prepare chestunnaru.", "explanation": ""},
        {"en": "She is improving her English fluency.", "te": "Ame English fluency improve cheskuntundi.", "explanation": ""},
        {"en": "The bus is moving slowly.", "te": "Bus slow ga velthundi.", "explanation": ""},
        {"en": "We are celebrating my friend’s birthday.", "te": "Memu na friend birthday celebrate chestunnam.", "explanation": ""},
        {"en": "My father is watering the plants.", "te": "Na father mokkalaki neellu పోస్తున్నారు.", "explanation": ""},
        {"en": "The children are eating ice cream.", "te": "Pillalu ice cream tintunnaru.", "explanation": ""},
        {"en": "I am speaking in English confidently.", "te": "Nenu confidence tho English matladutunnanu.", "explanation": ""},
        {"en": "She is improving her pronunciation daily.", "te": "Ame daily pronunciation improve cheskuntundi.", "explanation": "Continuous improvement ni Present Continuous lo express chesam."}
    ]
    
    concept.examples = examples
    concept.save()

    print("Success! Present Continuous Phase 2 (Examples) has been updated with 50 examples.")

if __name__ == '__main__':
    run()
