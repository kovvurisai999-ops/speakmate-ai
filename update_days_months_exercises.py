import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept, Exercise

def main():
    data = """
1
My exam starts on _____.
Answer: Monday
Meaning: Naa exam Monday start avutundi.
2
I was born in _____.
Answer: August
Meaning: Nenu August lo puttanu.
Explanation
Month kabatti "in".
3
We have a meeting on _____.
Answer: Friday
Meaning: Friday meeting undi.
4
My birthday is in _____.
Answer: December
Meaning: Naa birthday December lo untundi.
5
The office is closed on _____.
Answer: Saturday
Meaning: Saturday office close untundi.
6
Schools reopen in _____.
Answer: June
Meaning: Schools June lo reopen avutayi.
7
I play cricket every _____.
Answer: Sunday
Meaning: Prati Sunday cricket aaduthanu.
8
The festival comes in _____.
Answer: October
Meaning: Festival October lo vastundi.
9
I have an interview on _____.
Answer: Tuesday
Meaning: Tuesday interview undi.
10
We celebrate Christmas in _____.
Answer: December
Meaning: Christmas December lo celebrate chestham.
11
My sister got married in _____.
Answer: February
Meaning: Maa sister February lo marriage chesukundi.
12
The movie releases on _____.
Answer: Friday
Meaning: Movie Friday release avutundi.
13
I submitted my project on _____.
Answer: Wednesday
Meaning: Wednesday project submit chesanu.
Explanation
Specific day kabatti "on".
14
My college reopens in _____.
Answer: June
Meaning: College June lo reopen avutundi.
15
We visited Tirupati in _____.
Answer: May
Meaning: Memu May lo Tirupati vellam.
16
My brother joined college in _____.
Answer: September
Meaning: Maa brother September lo college join ayyadu.
17
I clean my room every _____.
Answer: Saturday
Meaning: Prati Saturday room clean chestanu.
18
We celebrate Independence Day in _____.
Answer: August
Meaning: August lo Independence Day celebrate chestham.
19
The shop opens on _____.
Answer: Monday
Meaning: Shop Monday open avutundi.
20
New classes start in _____.
Answer: July
Meaning: July lo kottha classes start avutayi.
Explanation
Month mundhu "in" use chestham.
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
        concept = Concept.objects.get(slug='days-months')
    except Concept.DoesNotExist:
        print("Error: Concept 'days-months' not found in database.")
        return

    deleted, _ = Exercise.objects.filter(concept=concept, type='FILL_BLANK').delete()
    print(f"Deleted {deleted} old FILL_BLANK exercises.")

    # MCQ options pool
    options_map = {
        'Monday':    ['Monday', 'Tuesday', 'Wednesday'],
        'Tuesday':   ['Tuesday', 'Monday', 'Thursday'],
        'Wednesday': ['Wednesday', 'Tuesday', 'Friday'],
        'Thursday':  ['Thursday', 'Wednesday', 'Friday'],
        'Friday':    ['Friday', 'Thursday', 'Saturday'],
        'Saturday':  ['Saturday', 'Friday', 'Sunday'],
        'Sunday':    ['Sunday', 'Saturday', 'Monday'],
        'January':   ['January', 'February', 'March'],
        'February':  ['February', 'January', 'March'],
        'March':     ['March', 'February', 'April'],
        'April':     ['April', 'March', 'May'],
        'May':       ['May', 'April', 'June'],
        'June':      ['June', 'May', 'July'],
        'July':      ['July', 'June', 'August'],
        'August':    ['August', 'July', 'September'],
        'September': ['September', 'August', 'October'],
        'October':   ['October', 'September', 'November'],
        'November':  ['November', 'October', 'December'],
        'December':  ['December', 'November', 'January'],
    }

    created_count = 0
    for ex in exercises:
        ans = ex['answer']
        options = options_map.get(ans, [ans, 'Monday', 'June'])
        if ans not in options:
            options[0] = ans
        seen = []
        for opt in options:
            if opt not in seen:
                seen.append(opt)
        options = seen[:3]
        while len(options) < 3:
            options.append('')

        Exercise.objects.create(
            concept=concept,
            type='FILL_BLANK',
            question=ex['question'],
            correct_answer=ex['answer'],
            hint=ex['hint'],
            explanation=ex['explanation'],
            options=options
        )
        created_count += 1

    print(f"Database updated! Created {created_count} FILL_BLANK exercises for Days & Months.")

if __name__ == "__main__":
    main()
