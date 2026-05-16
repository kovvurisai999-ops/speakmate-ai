import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept, Exercise

def main():
    data = """
1
_____ morning, sir.
Answer: Good
Meaning: Good morning sir.
Explanation
Morning greeting kabatti “Good” use chestham.
2
Hi, how _____ you?
Answer: are
Meaning: Hi, ela unnaru?
Explanation
“You” tho helping verb “are”.
3
Good _____, everyone.
Answer: evening
Meaning: Andariki good evening.
4
How _____ your day going?
Answer: is
Meaning: Mee roju ela nadustundi?
5
_____ you sleep well?
Answer: Did
Meaning: Baga nidrapoyava?
Explanation
Past tense question.
6
Nice to _____ you.
Answer: meet
Meaning: Mimmalni kalavadam santosham.
7
How are you _____ today?
Answer: doing
Meaning: Eeroju ela unnaru?
8
Please _____ a seat.
Answer: have
Meaning: Dayachesi kurchondi.
9
Good _____, teacher.
Answer: afternoon
Meaning: Good afternoon teacher.
10
What's _____?
Answer: up
Meaning: Em chestunnav?
11
See you _____.
Answer: later
Meaning: Tarvata kaluddam.
12
Have a safe _____.
Answer: journey
Meaning: Safe journey.
13
Welcome _____ our office.
Answer: to
Meaning: Maa office ki swagatham.
14
How _____ everything?
Answer: is
Meaning: Anni ela unnayi?
15
Good _____, mom.
Answer: night
Meaning: Amma good night.
16
Take _____.
Answer: care
Meaning: Jagratta.
17
How _____ your classes going?
Answer: are
Meaning: Mee classes ela unnayi?
18
Did you _____ lunch?
Answer: have
Meaning: Lunch chesava?
19
Good to _____ you again.
Answer: see
Meaning: Mimmalni malli choodadam santosham.
20
Please come _____.
Answer: in
Meaning: Lopalaki randi.
21
How may I _____ you?
Answer: help
Meaning: Nenu meeku ela help cheyyali?
22
Let's _____ the meeting.
Answer: start
Meaning: Meeting start cheddam.
23
Can you hear me _____?
Answer: clearly
Meaning: Naa voice clear gaa vinipistunda?
24
Hello, who is _____?
Answer: speaking
Meaning: Evaru maatladuthunnaru?
25
Have a nice _____.
Answer: day
Meaning: Mee roju bagundali.
26
Good _____, friends.
Answer: morning
Meaning: Friends ki good morning.
27
Thank you for _____.
Answer: coming
Meaning: Vachinanduku thanks.
28
Where are you _____?
Answer: going
Meaning: Ekkadiki velthunnav?
29
_____ your trip.
Answer: Enjoy
Meaning: Mee trip enjoy cheyyandi.
30
Let's practice English _____.
Answer: together
Meaning: Kalisi English practice cheddam.
31
You are doing _____.
Answer: great
Meaning: Nuvvu chala baga chestunnav.
32
Hope you are _____ well.
Answer: doing
Meaning: Meeru bagunnaru ani anukuntunnanu.
33
Did you finish your _____?
Answer: work
Meaning: Nee work complete chesava?
34
See you _____ week.
Answer: next
Meaning: Next week kaluddam.
35
It was nice _____ to you.
Answer: talking
Meaning: Neetho maatladadam bagundi.
36
Good evening _____.
Answer: everyone
Meaning: Andariki good evening.
37
How _____ your office today?
Answer: was
Meaning: Office ela undi?
38
Please _____ for a moment.
Answer: wait
Meaning: Konchem wait cheyyandi.
39
How have you _____?
Answer: been
Meaning: Ela unnaru inni rojulu?
40
Have a wonderful _____.
Answer: day
Meaning: Mee roju bagundali.
41
Good morning _____.
Answer: sir
Meaning: Good morning sir.
42
How are you _____?
Answer: today
Meaning: Eeroju ela unnaru?
43
See you _____.
Answer: tomorrow
Meaning: Repu kaluddam.
44
Welcome _____ home.
Answer: back
Meaning: Intiki malli swagatham.
45
Good _____ everyone.
Answer: night
Meaning: Andariki good night.
46
Please introduce _____.
Answer: yourself
Meaning: Mee gurinchi cheppandi.
47
How _____ your meeting?
Answer: was
Meaning: Meeting ela jarigindi?
48
Take rest and _____.
Answer: relax
Meaning: Relax avvu.
49
Thanks for _____.
Answer: calling
Meaning: Call chesinanduku thanks.
50
Have a great day _____.
Answer: ahead
Meaning: Mee mundu roju bagundali.
"""

    lines = [line.strip() for line in data.strip().split('\n') if line.strip()]
    
    exercises = []
    current_item = {}
    
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.isdigit():
            if current_item:
                exercises.append(current_item)
            current_item = {"question": "", "answer": "", "hint": "", "explanation": ""}
            i += 1
            if i < len(lines):
                current_item["question"] = lines[i]
                i += 1
            if i < len(lines) and lines[i].startswith("Answer:"):
                current_item["answer"] = lines[i].replace("Answer:", "").strip()
                i += 1
            if i < len(lines) and lines[i].startswith("Meaning:"):
                current_item["hint"] = lines[i].replace("Meaning:", "").strip()
                i += 1
        else:
            if current_item:
                if line == "Explanation":
                    explanation_lines = []
                    i += 1
                    while i < len(lines) and not lines[i].isdigit():
                        explanation_lines.append(lines[i])
                        i += 1
                    current_item["explanation"] = " ".join(explanation_lines)
                    continue
            i += 1

    if current_item:
        exercises.append(current_item)

    print(f"Parsed {len(exercises)} exercises.")

    try:
        greetings = Concept.objects.get(slug='greetings')
    except Concept.DoesNotExist:
        print("Error: Concept 'greetings' does not exist.")
        return

    # Delete existing fill-in-the-blank exercises for greetings to avoid duplicates
    Exercise.objects.filter(concept=greetings, type='FILL_BLANK').delete()

    created_count = 0
    for ex in exercises:
        # Some simple options generation
        ans = ex['answer']
        options = [ans]
        if ans.lower() == 'is': options.extend(['are', 'am'])
        elif ans.lower() == 'are': options.extend(['is', 'am'])
        elif ans.lower() == 'was': options.extend(['were', 'is'])
        elif ans.lower() == 'were': options.extend(['was', 'are'])
        elif ans.lower() == 'did': options.extend(['do', 'does'])
        elif ans.lower() == 'have': options.extend(['has', 'had'])
        elif ans.lower() == 'good': options.extend(['bad', 'well'])
        elif ans.lower() == 'meet': options.extend(['see', 'talk'])
        elif ans.lower() == 'start': options.extend(['stop', 'end'])
        else: options.extend(['___', '___']) # Dummy options if not matched
        
        # ensure unique options
        options = list(set(options))

        Exercise.objects.create(
            concept=greetings,
            type='FILL_BLANK',
            question=ex['question'],
            correct_answer=ex['answer'],
            hint=ex['hint'],
            explanation=ex['explanation'],
            options=options[:3] if len(options) >= 3 else options + [''] * (3 - len(options))
        )
        created_count += 1

    print(f"Database updated successfully! Created {created_count} FILL_BLANK exercises.")

if __name__ == "__main__":
    main()
