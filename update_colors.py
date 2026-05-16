import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept

def main():
    data = """
1
I bought a red shirt.
Meaning: Nenu red shirt konnanu.
Explanation
"red" adjective
"shirt" noun ni describe chestundi.
2
The sky is blue today.
Meaning: Eeroju aakasam blue gaa undi.
Explanation
"is" singular subject ki use chesam.
Natural color description.
3
My bike is black.
Meaning: Naa bike black color lo undi.
4
She likes pink dresses.
Meaning: Aame pink dresses istapadutundi.
5
The leaves are green.
Meaning: Aakulu green gaa unnayi.
Explanation
"leaves" plural kabatti "are" use chesam.
6
I painted my room white.
Meaning: Nenu naa room white color lo paint chesanu.
7
The mango is yellow.
Meaning: Mamidi pandu yellow gaa undi.
8
He wears a blue cap daily.
Meaning: Athanu daily blue cap vesukuntadu.
9
The rose flower is red.
Meaning: Rose flower red gaa untundi.
10
My sister bought a purple bag.
Meaning: Maa sister purple bag konnindi.
11
The cat has white fur.
Meaning: Pilli ki white fur undi.
12
I like brown shoes.
Meaning: Naku brown shoes nachutayi.
13
The traffic signal turned green.
Meaning: Traffic signal green ayindi.
Explanation
"turned" color change happened.
14
She uses a black mobile phone.
Meaning: Aame black mobile use chestundi.
15
The sunset looks orange.
Meaning: Sunset orange color lo kanipistundi.
16
My school bag is dark blue.
Meaning: Naa school bag dark blue color lo undi.
17
The wall is painted light green.
Meaning: Wall light green color lo paint chesaru.
18
He bought a silver watch.
Meaning: Athanu silver watch konnadu.
19
The baby is wearing a yellow dress.
Meaning: Baby yellow dress vesukundi.
Explanation
Present continuous tense.
Current action describe chestundi.
20
My friend drives a white car.
Meaning: Naa friend white car drive chestadu.
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
            current_item = {
                "word": f"Color #{line}",
                "en": "",
                "te": "",
                "sound": "Practice",
                "explanation": ""
            }
            i += 1
            if i < len(lines):
                current_item["en"] = lines[i]
                i += 1
            if i < len(lines) and lines[i].startswith("Meaning:"):
                current_item["te"] = lines[i].replace("Meaning:", "").strip()
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
        examples.append(current_item)

    print(f"Parsed {len(examples)} examples.")

    try:
        colors = Concept.objects.get(slug='colors')
    except Concept.DoesNotExist:
        print("Error: Concept 'colors' not found in database.")
        return

    colors.content = """Colors ante:
"Objects, clothes, nature, vehicles, fruits, places color ni describe cheyyadaniki use chese words."

Daily life lo:
- Dress colors
- Bike colors
- Fruits colors
- Room colors
- Sky colors

anni use chestham.

COMMON COLORS:
Color         | Telugu Meaning
--------------|-----------------
Red           | Erupu
Blue          | Neelam
Green         | Aakupacha
Black         | Nalupu
White         | Telupu
Yellow        | Pasupu
Pink          | Gulabi
Orange        | Orange
Brown         | Godhuma
Purple        | Ooda
"""

    colors.grammar_rules = """KEY RULES:

Rule 1: Color adjective laga noun mundhu vastundi.
✅ Red shirt       (correct)
❌ Shirt red       (wrong!)
Explanation: English lo adjective noun mundhu vastundi.

Rule 2: Color object ni describe chestundi.
✅ The sky is blue.
Explanation: "blue" sky color describe chestundi.

QUICK COLOR REFERENCE:
Red=Erupu | Blue=Neelam | Green=Aakupacha
Black=Nalupu | White=Telupu | Yellow=Pasupu
Pink=Gulabi | Orange=Orange | Brown=Godhuma | Purple=Ooda
"""

    colors.examples = examples
    colors.save()
    print(f"Database updated successfully with {len(examples)} Colors examples!")

if __name__ == "__main__":
    main()
