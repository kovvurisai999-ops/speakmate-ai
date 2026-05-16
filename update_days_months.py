import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept

def main():
    data = """
1
My exam starts on Monday.
Meaning: Naa exam Monday start avutundi.
Explanation
"on" day mundhu use chesam.
Specific day kabatti.
2
I was born in August.
Meaning: Nenu August lo puttanu.
Explanation
"in" month kosam use chestham.
3
We have a meeting on Friday.
Meaning: Maaku Friday meeting undi.
4
My college reopens in June.
Meaning: Maa college June lo reopen avutundi.
5
I play cricket every Sunday.
Meaning: Nenu prati Sunday cricket aaduthanu.
6
My birthday is in December.
Meaning: Naa birthday December lo untundi.
7
The office is closed on Saturday.
Meaning: Office Saturday close untundi.
8
We celebrate Independence Day in August.
Meaning: Memu August lo Independence Day celebrate chestham.
9
My sister got married in February.
Meaning: Maa sister February lo marriage chesukundi.
Explanation
Past event kabatti "got married".
10
I have an interview on Tuesday.
Meaning: Naaku Tuesday interview undi.
11
Schools reopen in June.
Meaning: Schools June lo reopen avutayi.
12
We visited Tirupati in May.
Meaning: Memu May lo Tirupati vellam.
13
My father goes to market on Sunday.
Meaning: Maa nanna Sunday market ki veltharu.
14
The festival comes in October.
Meaning: Festival October lo vastundi.
15
I submitted my project on Wednesday.
Meaning: Nenu Wednesday project submit chesanu.
Explanation
Specific completed action.
Past tense usage.
16
We start new classes in July.
Meaning: Memu July lo kottha classes start chestham.
17
The movie releases on Friday.
Meaning: Movie Friday release avutundi.
18
My brother joined college in September.
Meaning: Maa brother September lo college join ayyadu.
19
I clean my room every Saturday.
Meaning: Nenu prati Saturday room clean chestanu.
20
We celebrate Christmas in December.
Meaning: Memu December lo Christmas celebrate chestham.
Explanation
Festivals mostly months tho use chestham.
"in December" correct usage.
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
                "word": f"Day/Month #{line}",
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
        concept = Concept.objects.get(slug='days-months')
    except Concept.DoesNotExist:
        print("Error: Concept 'days-months' not found in database.")
        return

    concept.content = """Days & Months ante:
"Week days mariyu year months ni English lo cheppadam."

Daily life lo:
- Dates
- Birthdays
- Exams
- Meetings
- Holidays
- Schedules

anni days & months tho untayi.

DAYS OF THE WEEK:
Day        | Telugu Meaning
-----------|----------------
Monday     | Somavaram
Tuesday    | Mangalavaram
Wednesday  | Budhavaram
Thursday   | Guruvaaram
Friday     | Sukravaaram
Saturday   | Sanivaaram
Sunday     | Aadivaaram

MONTHS OF THE YEAR:
January | February | March    | April
May     | June     | July     | August
September | October | November | December
"""

    concept.grammar_rules = """KEY RULES:

Rule 1: Days & Months first letter CAPITAL gaa rayali.
Correct : Monday, August, Friday
Wrong   : monday, august, friday
(Days and months are proper nouns.)

Rule 2: Prepositions
"ON"  → Days kosam use chestham.
"IN"  → Months kosam use chestham.

Correct :
  The meeting is on Monday.
  My birthday is in May.

Wrong :
  The meeting is in Monday.
  My birthday is on May.
"""

    concept.examples = examples
    concept.save()
    print(f"Database updated successfully with {len(examples)} Days & Months examples!")

if __name__ == "__main__":
    main()
