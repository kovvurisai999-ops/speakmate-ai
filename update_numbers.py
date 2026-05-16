import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept

def main():
    data = """
1
I have two brothers.
Meaning: Naku iddaru brothers unnaru.
Explanation
"two" quantity
"brothers" plural because more than one
2
My class starts at 9 AM.
Meaning: Naa class 9 AM ki start avutundi.
Explanation
Time expression
Daily routine sentence
3
I bought three notebooks yesterday.
Meaning: Nenu ninna moodu notebooks konnanu.
Explanation
"three" quantity
"notebooks" plural noun
4
My phone number has ten digits.
Meaning: Naa phone number lo padi digits unnayi.
5
She scored ninety marks in English.
Meaning: Aame English lo 90 marks techindi.
6
We waited for five minutes.
Meaning: Memu 5 minutes wait chesam.
Explanation
Time duration sentence
7
There are four chairs in the room.
Meaning: Room lo nalugu chairs unnayi.
8
My father earns fifty thousand rupees per month.
Meaning: Maa nanna month ki 50,000 earn chestaru.
9
I drank two glasses of water.
Meaning: Nenu rendu glasses water taganu.
10
The bus arrived after ten minutes.
Meaning: Bus 10 minutes tarvata vachindi.
11
My younger sister is eight years old.
Meaning: Maa chelli 8 years old.
12
I paid one hundred rupees for lunch.
Meaning: Lunch kosam 100 rupees pay chesanu.
13
There are thirty students in our class.
Meaning: Maa class lo 30 students unnaru.
14
The movie starts at 7 PM.
Meaning: Movie 7 PM ki start avutundi.
15
I completed five tasks today.
Meaning: Nenu eeroju 5 tasks complete chesanu.
16
She bought six mangoes from the market.
Meaning: Aame market nunchi 6 mamidipandlu konnindi.
17
The meeting lasted for two hours.
Meaning: Meeting rendu gantalu jarigindi.
Explanation
Duration sentence
"hours" plural noun
18
I wake up at 5 AM daily.
Meaning: Nenu daily 5 AM ki lestanu.
19
My college has three computer labs.
Meaning: Maa college lo 3 computer labs unnayi.
20
I solved twenty questions in the exam.
Meaning: Nenu exam lo 20 questions solve chesanu.
21
The train was delayed by fifteen minutes.
Meaning: Train 15 minutes late ayindi.
22
My brother bought two mobile phones.
Meaning: Maa brother rendu mobiles konnadu.
23
We planted ten trees near our house.
Meaning: Maa inti daggara 10 mokkalu natam.
24
I attended three online classes today.
Meaning: Nenu eeroju 3 online classes attend ayyanu.
25
My grandmother is seventy years old.
Meaning: Maa ammamma 70 years old.
26
I saved five hundred rupees this week.
Meaning: Nenu ee week 500 rupees save chesanu.
27
The shop opens at 10 o'clock.
Meaning: Shop 10 ki open avutundi.
28
I have one younger brother.
Meaning: Naku oka thammudu unnadu.
29
The teacher asked ten questions.
Meaning: Teacher 10 questions adigaru.
30
My mother bought twelve eggs.
Meaning: Maa amma 12 eggs konnindi.
31
I watched two movies last weekend.
Meaning: Nenu last weekend rendu movies chusanu.
32
The restaurant has twenty tables.
Meaning: Restaurant lo 20 tables unnayi.
33
We traveled for six hours.
Meaning: Memu 6 hours travel chesam.
34
My friend sent me five photos.
Meaning: Naa friend naku 5 photos pampadu.
35
I answered forty questions correctly.
Meaning: Nenu 40 questions correct gaa answer chesanu.
36
The water bottle costs twenty rupees.
Meaning: Water bottle cost 20 rupees.
37
There are seven days in a week.
Meaning: Oka week lo 7 days untayi.
Explanation
General fact sentence
Present simple tense
38
I ate three bananas after gym.
Meaning: Gym tarvata nenu 3 bananas tinnanu.
39
The exam starts in five minutes.
Meaning: Exam 5 minutes lo start avutundi.
40
My father owns two bikes.
Meaning: Maa nanna ki rendu bikes unnayi.
41
We invited fifty guests to the function.
Meaning: Memu function ki 50 guests ni pilicham.
42
The school has one thousand students.
Meaning: School lo 1000 students unnaru.
43
I drink four bottles of water daily.
Meaning: Nenu daily 4 bottles water taguthanu.
44
My sister completed eight assignments.
Meaning: Maa sister 8 assignments complete chesindi.
45
The cricket match begins at 6 PM.
Meaning: Cricket match 6 PM ki start avutundi.
46
I bought two shirts and one pant.
Meaning: Nenu rendu shirts mariyu oka pant konnanu.
47
My friend has three pet dogs.
Meaning: Naa friend daggara 3 pet dogs unnayi.
48
The library contains hundreds of books.
Meaning: Library lo vandala books unnayi.
49
I completed my work in thirty minutes.
Meaning: Nenu naa work 30 minutes lo complete chesanu.
50
The shopping mall has five floors.
Meaning: Shopping mall lo 5 floors unnayi.
Explanation
"floors" plural because five
Real-life place example
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
                "word": f"Number #{line}",
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
                if line == "Explanation" or line == "Why formed?":
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

    numbers = Concept.objects.get(slug='numbers')

    numbers.content = """Numbers ante:
"Counting, quantity, age, money, time, marks, phone numbers, prices, measurements cheppadaniki use chese English number words."

Daily life lo:
• Mobile number
• Bus number
• Age
• Money
• Marks
• Dates
• Prices

anni numbers tho untayi.

TYPES OF NUMBERS
• Cardinal Numbers  — One, Two, Three (quantity cheppataniki)
• Ordinal Numbers   — First, Second, Third (order cheppataniki)
• Money Numbers     — ₹100, ₹500
• Time Numbers      — 7 AM, 10 PM
• Counting Numbers  — 1 to 100
"""

    numbers.grammar_rules = """KEY RULES:

Rule 1: Singular/Plural correct gaa use cheyyali.
✅ One apple      (singular)
✅ Two apples     (plural — more than one)
❌ Two apple      (wrong!)

Rule 2: Numbers usually noun mundu vastayi.
✅ I bought three books.
❌ I bought books three.

COMMON NUMBER WORDS:
1 → One      |  2 → Two      |  3 → Three
10 → Ten     |  20 → Twenty  |  50 → Fifty
100 → Hundred |  1000 → Thousand
"""

    numbers.examples = examples
    numbers.save()
    print("Database updated successfully with 50 Numbers examples!")

if __name__ == "__main__":
    main()
