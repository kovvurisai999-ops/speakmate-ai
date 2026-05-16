import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept, Exercise

def main():
    exercises_data = [
        # 1-10: Morning Greetings
        ("Good _____, mom.", "morning", "Amma ki udayam cheppae greeting.", "Udayam lechi cheppae greeting 'Good morning'.", ["morning", "night", "evening"]),
        ("Good morning, sir. How _____ you?", "are", "Sir, meeru ela unnaru?", "'How are you?' anedi wellbeing adagadaniki standard phrase.", ["is", "am", "are"]),
        ("Good morning everyone. Please _____ a seat.", "have", "Andariki good morning. Kurchondi.", "'Have a seat' ante kurchondi ani artham.", ["take", "have", "sit"]),
        ("I wake up and say _____ to my dad.", "good morning", "Nanna ki udayam em chepthanu?", "Udayam lechi 'Good morning' antamu.", ["good morning", "good night", "hello"]),
        ("_____ morning, teacher.", "Good", "Teacher ki udayam cheppae greeting.", "Greeting mundu 'Good' vadutham.", ["Good", "Bad", "Nice"]),
        ("Good morning friends. Did you _____ well?", "sleep", "Friends, baga nidrapoyara?", "Udayam adige common question.", ["sleep", "ate", "went"]),
        ("Good _____ team, let's start the work.", "morning", "Team ki udayam cheppae greeting.", "Work start chesetappudu morning greeting vadutham.", ["morning", "evening", "night"]),
        ("Good morning uncle, how is your _____?", "health", "Uncle, mee arogyam ela undi?", "Elderly people ni health gurinchi adagatam maryada.", ["health", "car", "house"]),
        ("Good morning auntie, did you have _____?", "coffee", "Auntie, coffee tagara?", "Udayam adige casual question.", ["coffee", "lunch", "dinner"]),
        ("Good morning, welcome _____ our office.", "to", "Maa office ki swagatham.", "'Welcome to' anedi standard structure.", ["to", "at", "in"]),

        # 11-20: Afternoon & Evening
        ("Good _____, sir. Did you have lunch?", "afternoon", "Sir, madhyanam greeting.", "Lunch time (12 PM tarvata) 'Good afternoon' antam.", ["morning", "afternoon", "evening"]),
        ("Good afternoon everyone. How is your day _____?", "going", "Mee roju ela nadustundi?", "Ongoing day gurinchi adagadaniki 'going' vadutham.", ["going", "gone", "go"]),
        ("Good _____, madam. The meeting is at 3 PM.", "afternoon", "Madam ki 3 PM greeting.", "3 PM anedi afternoon time.", ["morning", "afternoon", "night"]),
        ("It's 2 PM, so I say _____.", "good afternoon", "Madhyanam 2 gantulaki em cheppali?", "Afternoon greeting.", ["good morning", "good afternoon", "good evening"]),
        ("Good _____, the sun is setting.", "evening", "Suryudu asthaminche samayam greeting.", "Suryudu asthaminche tappudu 'Good evening' antam.", ["morning", "afternoon", "evening"]),
        ("Good evening sir, how was your _____ today?", "day", "Sir, eeroju mee day ela undi?", "Day finish ayyeppudu adige question.", ["day", "night", "morning"]),
        ("Good evening everyone, welcome to the _____.", "party", "Party ki vachina variki greeting.", "Evening events lo party ki welcome cheptham.", ["party", "office", "school"]),
        ("Good evening mom, I am _____ from work.", "back", "Amma, nenu work nunchi vachanu.", "Evening intiki vachaka cheppe mata.", ["back", "go", "away"]),
        ("We say 'Good _____' after 4 PM.", "evening", "4 PM tarvata em cheppali?", "Sayantram greeting.", ["morning", "afternoon", "evening"]),
        ("Good evening, let's have some _____.", "snacks", "Sayantram snacks tindam.", "Evening tine tindi ni 'snacks' antam.", ["breakfast", "lunch", "snacks"]),

        # 21-30: Night & Goodbye
        ("Good _____, sweet dreams.", "night", "Padukonumundu cheppae greeting.", "Nidrapoyae mundu 'Good night' cheptham.", ["morning", "evening", "night"]),
        ("I am going to sleep, so I say _____.", "good night", "Nenu nidrapothunnanu, em cheppali?", "Sleep greeting.", ["hello", "good morning", "good night"]),
        ("Good night mom, _____ well.", "sleep", "Amma, baga nidrapo.", "Nidrapommani korukovatam.", ["eat", "sleep", "walk"]),
        ("Goodbye, see you _____.", "tomorrow", "Bye, repu kaluddam.", "Future meeting gurinchi 'tomorrow' antam.", ["yesterday", "tomorrow", "now"]),
        ("It was nice _____ you.", "meeting", "Mimmalni kalavadam santosham.", "Kalisi velleppudu cheppe maata.", ["meeting", "meet", "met"]),
        ("Take _____, see you soon.", "care", "Jagratta, tondaraga kaluddam.", "Velleppudu jagratta cheppadaniki 'Take care' antam.", ["care", "help", "time"]),
        ("Bye everyone, have a _____ weekend.", "nice", "Andariki bye, manchi weekend.", "Wishing someone a good time.", ["bad", "nice", "long"]),
        ("I must go now, _____.", "goodbye", "Nenu ippudu vellali, bye.", "Leaving greeting.", ["hello", "goodbye", "hi"]),
        ("See you _____, buddy.", "later", "Tarvata kaluddam.", "Casual goodbye.", ["later", "before", "never"]),
        ("Have a _____ night.", "peaceful", "Prasanthmaina ratri.", "Wishing someone well.", ["peaceful", "noisy", "busy"]),

        # 31-40: Formal Greetings
        ("How _____ you do, sir?", "do", "Formal greeting (Sir).", "'How do you do?' anedi formal greeting.", ["do", "are", "is"]),
        ("It is a _____ to meet you, madam.", "pleasure", "Mimmalni kalavadam naa adrustam.", "Formal way of showing respect.", ["pleasure", "happy", "good"]),
        ("Welcome to our _____, please come in.", "company", "Maa company ki swagatham.", "Professional welcome.", ["company", "house", "park"]),
        ("Good morning, how can I _____ you today?", "help", "Nenu meeku ela help cheyyagalanu?", "Service greeting.", ["help", "give", "take"]),
        ("I am _____ to meet you.", "delighted", "Mimmalni kalavadam chala santosham.", "Very formal happy greeting.", ["delighted", "sad", "angry"]),
        ("Please _____ yourself, sir.", "introduce", "Mee gurinchi cheppandi.", "Formal request to start intro.", ["introduce", "speak", "tell"]),
        ("Thank you for _____ us.", "joining", "Matho kalisinanduku thanks.", "Professional closing greeting.", ["joining", "eating", "going"]),
        ("Good afternoon, is the manager _____?", "available", "Manager unnara?", "Office query greeting.", ["available", "gone", "busy"]),
        ("May I _____ who is calling?", "ask", "Evaru maatladuthunnaru?", "Telephone formal greeting.", ["ask", "tell", "say"]),
        ("Welcome _____ the conference.", "to", "Conference ki swagatham.", "Professional event welcome.", ["to", "at", "on"]),

        # 41-50: Informal Greetings
        ("Hey bro, _____ up?", "what's", "Bro, em chestunnav?", "Casual friend greeting.", ["what's", "how's", "who's"]),
        ("Hi dude, _____ time no see.", "long", "Chala rojula tarvata chustunnanu.", "Casual way to say we met after a long time.", ["long", "short", "big"]),
        ("Hey buddy, how are _____?", "things", "Anni ela unnayi?", "Casual wellbeing check.", ["things", "it", "that"]),
        ("Hi! _____ is it going?", "How", "Ela nadustundi?", "Casual 'How are you?'.", ["How", "What", "Why"]),
        ("Yo! Ready _____ the match?", "for", "Match ki ready aa?", "Casual excitement greeting.", ["for", "to", "at"]),
        ("Hey friend, nice to _____ you here.", "see", "Ninnu ikkada choodadam santosham.", "Casual meeting greeting.", ["see", "look", "watch"]),
        ("Hi everyone, what are you _____?", "doing", "Andaru em chestunnaru?", "Casual group greeting.", ["doing", "done", "do"]),
        ("Hello! How have you _____?", "been", "Inni rojulu ela unnaru?", "Asking about the past time.", ["been", "be", "being"]),
        ("Hey, you _____ great today!", "look", "Eeroju nuvvu chala bagunnav.", "Compliment greeting.", ["look", "see", "watch"]),
        ("Hi, _____ is your family?", "how", "Mee family ela undi?", "Caring casual greeting.", ["how", "who", "where"]),
    ]

    print("Updating Greetings exercises...")
    try:
        concept = Concept.objects.get(slug='greetings')
        Exercise.objects.filter(concept=concept, type='FILL_BLANK').delete()
        
        for q, ans, hint, exp, opts in exercises_data:
            # Generate options if not provided correctly, but I provided them
            Exercise.objects.create(
                concept=concept,
                type='FILL_BLANK',
                question=q,
                correct_answer=ans,
                hint=hint,
                explanation=exp,
                options=opts
            )
        print(f"Finished Greetings. Total: {len(exercises_data)}")
    except Concept.DoesNotExist:
        print("Concept 'greetings' not found.")

if __name__ == "__main__":
    main()
