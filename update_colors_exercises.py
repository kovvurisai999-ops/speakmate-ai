import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept, Exercise

def main():
    data = """
1
The sky is _____.
Answer: blue
Meaning: Aakasam blue gaa untundi.
Explanation
Sky natural color blue.
2
I bought a _____ shirt.
Answer: red
Meaning: Nenu red shirt konnanu.
3
The leaves are _____.
Answer: green
Meaning: Aakulu green gaa untayi.
4
My bike is _____.
Answer: black
Meaning: Naa bike black color lo undi.
5
She likes _____ dresses.
Answer: pink
Meaning: Aame pink dresses istapadutundi.
6
The mango is _____.
Answer: yellow
Meaning: Mamidi pandu yellow gaa untundi.
7
I painted my room _____.
Answer: white
Meaning: Nenu room white color lo paint chesanu.
8
The rose flower is _____.
Answer: red
Meaning: Rose flower red gaa untundi.
9
He wears a _____ cap daily.
Answer: blue
Meaning: Athanu blue cap daily vesukuntadu.
10
My sister bought a _____ bag.
Answer: purple
Meaning: Maa sister purple bag konnindi.
11
The cat has _____ fur.
Answer: white
Meaning: Pilli ki white fur undi.
12
I like _____ shoes.
Answer: brown
Meaning: Naku brown shoes nachutayi.
13
The traffic signal turned _____.
Answer: green
Meaning: Traffic signal green ayindi.
Explanation
"turned" change indicate chestundi.
14
She uses a _____ mobile phone.
Answer: black
Meaning: Aame black mobile use chestundi.
15
The sunset looks _____.
Answer: orange
Meaning: Sunset orange color lo untundi.
16
My school bag is dark _____.
Answer: blue
Meaning: Naa school bag dark blue.
17
The wall is painted light _____.
Answer: green
Meaning: Wall light green color lo undi.
18
He bought a _____ watch.
Answer: silver
Meaning: Athanu silver watch konnadu.
19
The baby is wearing a _____ dress.
Answer: yellow
Meaning: Baby yellow dress vesukundi.
Explanation
Current action kabatti "is wearing".
20
My friend drives a _____ car.
Answer: white
Meaning: Naa friend white car drive chestadu.
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
        colors = Concept.objects.get(slug='colors')
    except Concept.DoesNotExist:
        print("Error: Concept 'colors' not found in database.")
        return

    deleted, _ = Exercise.objects.filter(concept=colors, type='FILL_BLANK').delete()
    print(f"Deleted {deleted} old FILL_BLANK exercises.")

    # MCQ options pool by answer
    options_map = {
        'blue':   ['blue', 'red', 'green'],
        'red':    ['red', 'blue', 'pink'],
        'green':  ['green', 'blue', 'yellow'],
        'black':  ['black', 'white', 'brown'],
        'pink':   ['pink', 'purple', 'red'],
        'yellow': ['yellow', 'orange', 'green'],
        'white':  ['white', 'black', 'silver'],
        'purple': ['purple', 'pink', 'blue'],
        'brown':  ['brown', 'black', 'orange'],
        'orange': ['orange', 'yellow', 'red'],
        'silver': ['silver', 'white', 'grey'],
    }

    created_count = 0
    for ex in exercises:
        ans = ex['answer'].lower()
        options = options_map.get(ans, [ex['answer'], 'red', 'blue'])
        if ex['answer'] not in options:
            options[0] = ex['answer']
        # Deduplicate
        seen = []
        for opt in options:
            if opt not in seen:
                seen.append(opt)
        options = seen[:3]
        while len(options) < 3:
            options.append('')

        Exercise.objects.create(
            concept=colors,
            type='FILL_BLANK',
            question=ex['question'],
            correct_answer=ex['answer'],
            hint=ex['hint'],
            explanation=ex['explanation'],
            options=options
        )
        created_count += 1

    print(f"Database updated! Created {created_count} FILL_BLANK exercises for Colors.")

if __name__ == "__main__":
    main()
