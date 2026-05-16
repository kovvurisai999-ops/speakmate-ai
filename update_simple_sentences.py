import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept

def main():
    data = """
1
I drink coffee every morning.
Meaning: Nenu prati morning coffee taguthanu.
Explanation
Daily habit sentence.
Present simple tense use chesam.
2
She goes to college daily.
Meaning: Aame daily college ki velthundi.
Explanation
"She" singular kabatti "goes" use chesam.
3
My father works in a bank.
Meaning: Maa nanna bank lo work chestaru.
4
I play cricket with friends.
Meaning: Nenu friends tho cricket aaduthanu.
5
We watch movies together.
Meaning: Memu kalisi movies chustham.
Explanation
"We" plural subject.
Base verb "watch" use chesam.
6
My mother cooks tasty food.
Meaning: Maa amma tasty food chestundi.
7
The baby is sleeping.
Meaning: Baby nidrapothundi.
Explanation
Current action kabatti present continuous tense.
8
I wake up at 6 AM.
Meaning: Nenu 6 AM ki lestanu.
9
He drives carefully.
Meaning: Athanu jagrathaga drive chestadu.
10
My sister likes music.
Meaning: Maa sister ki music istam.
11
The bus arrived late.
Meaning: Bus late gaa vachindi.
Explanation
Completed action kabatti past tense.
12
I completed my homework.
Meaning: Nenu naa homework complete chesanu.
13
They are playing football.
Meaning: Vallu football aadutunnaru.
14
My friend bought a laptop.
Meaning: Naa friend laptop konnadu.
15
The teacher explained the lesson.
Meaning: Teacher lesson explain chesaru.
16
I am learning spoken English.
Meaning: Nenu spoken English nerchukuntunnanu.
Explanation
Ongoing action.
"am learning" present continuous tense.
17
My brother watches YouTube daily.
Meaning: Maa brother daily YouTube chustadu.
18
We visited Hyderabad last month.
Meaning: Memu last month Hyderabad vellam.
19
The dog barked loudly.
Meaning: Kukka gattiga arichindi.
20
She speaks English fluently.
Meaning: Aame English fluently maatladutundi.
Explanation
Skill/action sentence.
"fluently" adverb action ni describe chestundi.
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
                "word": f"Sentence #{line}",
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
        concept = Concept.objects.get(slug='simple-sentences')
    except Concept.DoesNotExist:
        print("Error: Concept 'simple-sentences' not found in database.")
        return

    concept.content = """Simple Sentences ante:
"Oka complete idea ni easy English lo cheppe small sentences."

Simple sentence lo usually:
- Subject (who?)
- Verb  (action?)
- Object/Meaning (what?)

untayi.

EXAMPLE STRUCTURE:
  I   eat   rice.
  |    |      |
Subject Verb  Object

WHY SIMPLE SENTENCES IMPORTANT?
- Spoken English foundation
- Daily conversations easy avutayi
- Grammar basics improve avutayi
- Confidence periguthundi

COMMON SENTENCE PATTERNS:
Pattern                  | Example
-------------------------|--------------------
Subject + Verb           | I run.
Subject + Verb + Object  | I read books.
Subject + is/am/are      | She is happy.
"""

    concept.grammar_rules = """KEY RULES:

Rule 1: Sentence lo subject + verb compulsory undali.
Correct : She sings.
Wrong   : She beautiful.
(Verb lekapothe sentence complete kaadu.)

Rule 2: Present habits/simple truths ki simple present tense.
Correct : I drink coffee daily.

Rule 3: Singular subject (he/she/it) tho verb s/es add cheyyali.
Correct : She goes to school.
Wrong   : She go to school.

Rule 4: Past events ki past tense verb use cheyyali.
Correct : The bus arrived late.
Wrong   : The bus arrive late.
"""

    concept.examples = examples
    concept.save()
    print(f"Database updated successfully with {len(examples)} Simple Sentences examples!")

if __name__ == "__main__":
    main()
