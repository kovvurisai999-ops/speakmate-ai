import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept, Exercise

def main():
    data = """
1
I have _____ brothers.
Answer: two
Meaning: Naku iddaru brothers unnaru.
Explanation
Quantity cheppadaniki number use chesam.
"brothers" plural noun.
2
My class starts at _____ AM.
Answer: 9
Meaning: Naa class 9 AM ki start avutundi.
3
She bought _____ apples from the market.
Answer: five
Meaning: Aame market nunchi 5 apples konnindi.
4
There are _____ students in our class.
Answer: thirty
Meaning: Maa class lo 30 students unnaru.
5
I drank _____ glasses of water.
Answer: two
Meaning: Nenu rendu glasses water taganu.
6
The movie starts at _____ PM.
Answer: 7
Meaning: Movie 7 PM ki start avutundi.
7
My grandmother is _____ years old.
Answer: seventy
Meaning: Maa ammamma 70 years old.
8
I solved _____ questions in the exam.
Answer: twenty
Meaning: Nenu exam lo 20 questions solve chesanu.
9
The bus arrived after _____ minutes.
Answer: ten
Meaning: Bus 10 minutes tarvata vachindi.
10
We planted _____ trees near our house.
Answer: ten
Meaning: Maa inti daggara 10 mokkalu natam.
11
I wake up at _____ AM daily.
Answer: 5
Meaning: Nenu daily 5 AM ki lestanu.
12
My brother bought _____ mobile phones.
Answer: two
Meaning: Maa brother rendu mobiles konnadu.
13
The meeting lasted for _____ hours.
Answer: two
Meaning: Meeting rendu gantalu jarigindi.
Explanation
"hours" plural because two.
14
I saved _____ hundred rupees this week.
Answer: five
Meaning: Nenu ee week 500 rupees save chesanu.
15
The train was delayed by _____ minutes.
Answer: fifteen
Meaning: Train 15 minutes late ayindi.
16
There are _____ days in a week.
Answer: seven
Meaning: Oka week lo 7 days untayi.
17
I watched _____ movies last weekend.
Answer: two
Meaning: Nenu last weekend rendu movies chusanu.
18
My father owns _____ bikes.
Answer: two
Meaning: Maa nanna ki rendu bikes unnayi.
19
The school has _____ thousand students.
Answer: one
Meaning: School lo 1000 students unnaru.
20
I completed my work in _____ minutes.
Answer: thirty
Meaning: Nenu naa work 30 minutes lo complete chesanu.
21
The shopping mall has _____ floors.
Answer: five
Meaning: Shopping mall lo 5 floors unnayi.
22
I bought _____ shirts yesterday.
Answer: three
Meaning: Nenu ninna 3 shirts konnanu.
23
The cricket match begins at _____ PM.
Answer: 6
Meaning: Cricket match 6 PM ki start avutundi.
24
My friend sent me _____ photos.
Answer: five
Meaning: Naa friend naku 5 photos pampadu.
25
I attended _____ online classes today.
Answer: three
Meaning: Nenu eeroju 3 online classes attend ayyanu.
Explanation
"classes" plural because three.
Present day activity sentence.
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
                    current_item["explanation"] = " | ".join(explanation_lines)
                    continue
            i += 1

    if current_item:
        exercises.append(current_item)

    print(f"Parsed {len(exercises)} exercises.")

    try:
        numbers = Concept.objects.get(slug='numbers')
    except Concept.DoesNotExist:
        print("Error: Concept 'numbers' does not exist in the database.")
        return

    # Delete existing fill-in-the-blank exercises to avoid duplicates
    deleted, _ = Exercise.objects.filter(concept=numbers, type='FILL_BLANK').delete()
    print(f"Deleted {deleted} old FILL_BLANK exercises.")

    # Number word options pool for generating MCQ choices
    number_options_map = {
        'one':     ['one', 'two', 'three'],
        'two':     ['two', 'three', 'four'],
        'three':   ['three', 'five', 'two'],
        'four':    ['four', 'three', 'six'],
        'five':    ['five', 'three', 'seven'],
        'six':     ['six', 'four', 'eight'],
        'seven':   ['seven', 'six', 'eight'],
        'eight':   ['eight', 'six', 'ten'],
        'nine':    ['nine', 'seven', 'ten'],
        'ten':     ['ten', 'five', 'fifteen'],
        'fifteen': ['fifteen', 'ten', 'twenty'],
        'twenty':  ['twenty', 'ten', 'thirty'],
        'thirty':  ['thirty', 'twenty', 'forty'],
        'forty':   ['forty', 'thirty', 'fifty'],
        'fifty':   ['fifty', 'forty', 'sixty'],
        'seventy': ['seventy', 'sixty', 'eighty'],
        '5':       ['5', '6', '7'],
        '6':       ['6', '7', '8'],
        '7':       ['7', '8', '9'],
        '9':       ['9', '10', '8'],
    }

    created_count = 0
    for ex in exercises:
        ans = ex['answer']
        options = number_options_map.get(ans.lower(), [ans, 'two', 'five'])
        # Make sure correct answer is always present
        if ans not in options:
            options[0] = ans
        # Deduplicate and limit to 3
        seen = []
        for opt in options:
            if opt not in seen:
                seen.append(opt)
        options = seen[:3]
        while len(options) < 3:
            options.append('')

        Exercise.objects.create(
            concept=numbers,
            type='FILL_BLANK',
            question=ex['question'],
            correct_answer=ex['answer'],
            hint=ex['hint'],
            explanation=ex['explanation'],
            options=options
        )
        created_count += 1

    print(f"Database updated successfully! Created {created_count} FILL_BLANK exercises for Numbers.")

if __name__ == "__main__":
    main()
