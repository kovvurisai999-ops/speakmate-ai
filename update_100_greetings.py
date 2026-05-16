import os
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept

def main():
    data = """
1
Good morning, mom.
Meaning: Amma, good morning.
Explanation
Morning greeting
Respectful family greeting
2
Good morning, sir. How are you?
Meaning: Sir, meeru ela unnaru?
Why formed?
“Good morning” → greeting
“How are you?” → wellbeing asking
3
Good morning everyone.
Meaning: Andariki good morning.
4
Good morning teacher.
Meaning: Good morning teacher.
5
Good morning friends.
Meaning: Friends andariki good morning.
6
Good morning dad, did you sleep well?
Meaning: Nanna, baga nidrapoyara?
Explanation
Past tense question
Caring conversation
7
Good morning team.
Meaning: Team ki good morning.
8
Good morning uncle.
Meaning: Uncle ki good morning.
9
Good morning auntie.
Meaning: Auntie ki good morning.
10
Good morning, welcome to our office.
Meaning: Maa office ki swagatham.
11
Good afternoon, sir.
Meaning: Good afternoon sir.
12
Good afternoon everyone.
Meaning: Andariki good afternoon.
13
Good afternoon madam.
Meaning: Good afternoon madam.
14
Did you have lunch?
Meaning: Meeru lunch chesara?
Explanation
Present perfect tense
Daily caring conversation
15
How is your day going?
Meaning: Mee roju ela nadustundi?
16
Welcome to our college.
Meaning: Maa college ki swagatham.
17
Nice to see you again.
Meaning: Mimmalni malli choodadam santosham.
18
How are your classes going?
Meaning: Mee classes ela unnayi?
19
Are you free now?
Meaning: Ippudu free gaa unnava?
20
Let's have coffee together.
Meaning: Kalisi coffee taguddam.
21
Good evening, sir.
Meaning: Good evening sir.
22
Good evening everyone.
Meaning: Andariki good evening.
23
How was your day?
Meaning: Nee day ela undi?
Explanation
Past tense
Completed day gurinchi adagadam
24
Did you finish your work?
Meaning: Nee work complete chesava?
25
Good evening friends.
Meaning: Friends ki good evening.
26
Welcome back home.
Meaning: Intiki malli swagatham.
27
How was the meeting?
Meaning: Meeting ela jarigindi?
28
Did you enjoy today?
Meaning: Eeroju enjoy chesava?
29
Good evening teacher.
Meaning: Good evening teacher.
30
How is everything?
Meaning: Anni ela unnayi?
31
Good night, mom.
Meaning: Amma good night.
32
Sleep well.
Meaning: Baga nidrapo.
33
Sweet dreams.
Meaning: Manchi kalalu ravali.
34
Good night everyone.
Meaning: Andariki good night.
35
Take care and sleep early.
Meaning: Jagratta, tondaraga nidrapo.
36
See you tomorrow.
Meaning: Repu kaluddam.
37
Talk to you later.
Meaning: Tarvata matladuddam.
38
It was nice talking to you.
Meaning: Neetho maatladadam bagundi.
Explanation
Past tense because conversation completed.
39
Have a peaceful night.
Meaning: Mee ratri santhoshamgaa undali.
40
Good night dad.
Meaning: Nanna good night.
41
Hey bro, what's up?
Meaning: Bro em chestunnav?
42
Hi dude, long time no see.
Meaning: Chala rojulu ayindi ninnu chusi.
43
Hey friend, how are you?
Meaning: Friend ela unnava?
44
Yo! Ready for the game?
Meaning: Game ki ready aa?
45
Hey buddy, where are you going?
Meaning: Ekkadiki velthunnav?
46
Hi bro, did you eat?
Meaning: Tinnava bro?
47
What's happening?
Meaning: Em jaruguthundi?
48
Hey! Nice shirt.
Meaning: Nee shirt bagundi.
49
Let's hang out today.
Meaning: Eeroju bayataki veldham.
50
Where have you been?
Meaning: Ekkada unnava inni rojulu?
Explanation
Present perfect tense
Long time tarvata adige question
51
Welcome to the meeting.
Meaning: Meeting ki swagatham.
52
How may I help you?
Meaning: Nenu meeku ela help cheyyagalanu?
53
Please have a seat.
Meaning: Dayachesi kurchondi.
54
Hope you're doing well.
Meaning: Meeru bagunnaru ani anukuntunnanu.
55
Thank you for coming.
Meaning: Vachinanduku dhanyavadhamulu.
56
Good to see you again.
Meaning: Mimmalni malli choodadam santosham.
57
Let's begin the meeting.
Meaning: Meeting start cheddam.
58
Can we discuss the project?
Meaning: Project gurinchi discuss cheddama?
59
Please introduce yourself.
Meaning: Mee gurinchi cheppandi.
60
Have a productive day.
Meaning: Mee roju productive gaa undali.
61
Hello, who is speaking?
Meaning: Evaru maatladuthunnaru?
62
Can you hear me clearly?
Meaning: Naa voice clear gaa vinipistunda?
63
Thanks for calling.
Meaning: Call chesinanduku thanks.
64
Please hold for a moment.
Meaning: Konchem wait cheyyandi.
65
I'll call you back later.
Meaning: Tarvata malli call chestanu.
66
Welcome to Hyderabad.
Meaning: Hyderabad ki swagatham.
67
Have a safe journey.
Meaning: Safe journey.
68
Enjoy your trip.
Meaning: Mee trip enjoy cheyyandi.
69
Where are you traveling?
Meaning: Meeru ekkadiki travel chestunnaru?
70
Take care while traveling.
Meaning: Travel lo jagratta.
71
Welcome to our store.
Meaning: Maa shop ki swagatham.
72
How can I help you?
Meaning: Meeku ela help cheyyali?
73
Are you looking for something?
Meaning: Meeru emaina vetukuthunnara?
74
Thank you for visiting.
Meaning: Visit chesinanduku thanks.
75
Please come again.
Meaning: Malli randi.
76
Hi classmates!
Meaning: Hi classmates!
77
Did you complete the assignment?
Meaning: Assignment complete chesava?
78
Are you ready for exams?
Meaning: Exams ki ready aa?
79
Let's study together.
Meaning: Kalisi chaduddam.
80
How was today's lecture?
Meaning: Eeroju lecture ela undi?
81
Hello! I'm happy to talk with you.
Meaning: Neetho maatladadam santosham.
82
Don't worry, you're improving daily.
Meaning: Nuvvu daily improve avutunnav.
83
Let's practice English together.
Meaning: Kalisi English practice cheddam.
84
You are speaking very well today.
Meaning: Eeroju nuvvu baga maatladuthunnav.
85
Keep smiling while speaking.
Meaning: Maatladetappudu navvuthu undu.
86
Welcome home, dad.
Meaning: Intiki swagatham nanna.
87
How was your office today?
Meaning: Office ela undi?
88
Did you eat dinner?
Meaning: Dinner chesava?
89
Good to have you here.
Meaning: Nuvvu ikkada undadam santosham.
90
Take rest and relax.
Meaning: Rest teesuko.
91
Bye, take care.
Meaning: Bye jagratta.
92
See you soon.
Meaning: Tondaralo kaluddam.
93
Have a wonderful day.
Meaning: Mee roju bagundali.
94
Goodbye everyone.
Meaning: Andariki goodbye.
95
See you next week.
Meaning: Next week kaluddam.
96
How have you been?
Meaning: Ela unnaru inni rojulu?
97
I'm glad to meet you.
Meaning: Mimmalni kalavadam santosham.
98
It's my pleasure to meet you.
Meaning: Mimmalni kalavadam naa adrustam.
99
Hope your family is doing well.
Meaning: Mee family bagundali ani korukuntunnanu.
100
Thank you, have a great day ahead.
Meaning: Thank you, mee mundu roju bagundali.
Explanation
Future positive wish
Professional ending sentence
"""

    examples = []
    lines = [line.strip() for line in data.strip().split('\n') if line.strip()]
    
    current_item = {}
    
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.isdigit():
            if current_item:
                examples.append(current_item)
            current_item = {"word": f"Greeting #{line}", "en": "", "te": "", "sound": "Practice", "explanation": ""}
            i += 1
            if i < len(lines):
                current_item["en"] = lines[i]
                i += 1
            if i < len(lines) and lines[i].startswith("Meaning:"):
                current_item["te"] = lines[i].replace("Meaning:", "").strip()
                i += 1
        else:
            if current_item:
                if line == "Explanation" or line == "Why formed?":
                    explanation_lines = []
                    i += 1
                    while i < len(lines) and not lines[i].isdigit():
                        explanation_lines.append(lines[i])
                        i += 1
                    current_item["explanation"] = " ".join(explanation_lines)
                    continue
            i += 1

    if current_item:
        examples.append(current_item)

    print(f"Parsed {len(examples)} examples.")

    greetings = Concept.objects.get(slug='greetings')
    greetings.content = """
Greetings ante: "Conversation start cheyyadaniki use chese polite words and sentences."

Manam:
• friends ni kalisinappudu
• teacher tho maatladetappudu
• office lo
• phone call lo
• travel lo
• guests ni welcome cheyyetappudu
greetings use chestham.

TYPES OF GREETINGS
• Formal Greetings (Boss, Teacher, Office): Good morning, How do you do?
• Informal Greetings (Friends, Family): Hi, Hello, What's up?
"""
    greetings.grammar_rules = """
KEY RULES:

Rule 1: Formal people tho respectful words use cheyyali.
✅ Good morning sir.
❌ Hey bro!

Rule 2: Friends tho casual language okay.
✅ Hey! What's up?

Rule 3: Situation batti greeting change avvali.
Morning: Good morning
Night: Good night
"""
    greetings.examples = examples
    greetings.save()
    print("Database updated successfully with 100 examples!")

if __name__ == "__main__":
    main()
