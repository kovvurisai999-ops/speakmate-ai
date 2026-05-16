import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept

def main():
    content = """What is Family Vocabulary?

Family Vocabulary ante:

"Family members gurinchi English lo use chese words."

Examples:
- Father
- Mother
- Brother
- Sister
- Uncle
- Aunt
- Grandfather
- Cousin

Ivi manam daily conversations lo chala use chestham.

Why Family Vocabulary Important?

✅ Family gurinchi English lo maatladagalugutaru
✅ Self introduction improve avutundi
✅ Daily communication easy avutundi
✅ Spoken English confidence perugutundi

Common Family Vocabulary:
- Father: Nanna
- Mother: Amma
- Brother: Annayya / Thammudu
- Sister: Akka / Chelli
- Uncle: Babai
- Aunt: Pinni / Atta
- Grandfather: Thatha
- Grandmother: Ammamma
- Cousin: Cousin
- Family: Kutumbam"""

    rules = """KEY RULES

Rule 1: Family member name ki correct relationship word use cheyyali.
Example: My father is a farmer.

Rule 2: Singular/plural correct gaa use cheyyali.
✅ I have one brother.
✅ I have two sisters."""

    raw_data = """
1
My father goes to work early.
Naa nanna tondaraga work ki veltharu.
AI Analysis: Why this sentence?
“My father” → singular subject
“goes” → singular verb
Daily life action sentence
2
My mother cooks delicious food.
Maa amma tasty food chestundi.
AI Analysis
Present simple tense
Habit/action sentence
3
My brother plays cricket every evening.
Maa brother prati evening cricket aadutadu.
AI Analysis
“plays” because singular subject
“every evening” → routine
4
My sister helps me with homework.
Maa sister naa homework lo help chestundi.
AI Analysis
Helping action
Present tense usage
5
We are a family of four members.
Memu naluguru family members.
AI Analysis
“are” because “we”
Family introduction sentence
6
My grandfather reads newspapers daily.
Maa thatha daily newspaper chadutaaru.
AI Analysis
Habit sentence
“reads” singular verb
7
My grandmother tells interesting stories.
Maa ammamma manchi stories cheptundi.
8
My uncle lives in Hyderabad.
Maa babai Hyderabad lo untaru.
AI Analysis
Location sentence
“lives” singular verb
9
My aunt teaches at a school.
Maa atta school lo teaching chestundi.
10
My cousin studies engineering.
Naa cousin engineering chadutunnadu.
AI Analysis
Present continuous learning action
11
My parents support me always.
Maa parents eppudu support chestaru.
AI Analysis
“parents” plural
So “support” base verb
12
I love spending time with my family.
Nenu naa family tho time spend cheyadam istapadthanu.
13
My brother bought a new bike.
Maa brother kottha bike konnadu.
AI Analysis
“bought” → past tense
14
My mother wakes me up every morning.
Maa amma prati morning nannu lepistundi.
15
My father drives carefully.
Maa nanna jagrathaga drive chestaru.
16
My sister sings very well.
Maa sister chala baga paadutundi.
17
My grandparents live in a village.
Maa grandparents village lo untaru.
AI Analysis
“grandparents” plural
“live” plural verb
18
We eat dinner together every night.
Memu prati night kalisi dinner chestam.
19
My cousin works in an IT company.
Naa cousin IT company lo work chestadu.
20
My younger brother watches cartoons.
Maa chinna brother cartoons chustadu.
21
My elder sister completed her degree.
Maa akka degree complete chesindi.
AI Analysis
“completed” → completed past action
22
My family celebrates festivals happily.
Maa family festivals happy gaa celebrate chestundi.
23
My father drinks coffee every morning.
Maa nanna prati morning coffee tagutaru.
24
My mother keeps the house clean.
Maa amma illu clean gaa unchutundi.
25
My sister is preparing for exams.
Maa sister exams ki prepare avutundi.
AI Analysis
Present continuous tense
26
My brother repairs mobile phones.
Maa brother mobile phones repair chestadu.
27
My uncle owns a small business.
Maa babai small business own chestunnaru.
28
My aunt makes beautiful dresses.
Maa atta manchi dresses chestundi.
29
My father teaches me discipline.
Maa nanna naku discipline nerpistharu.
30
My mother cares about everyone.
Maa amma andarini care chestundi.
31
My cousin loves playing football.
Naa cousin football aadadam istapadthadu.
32
My sister bought new clothes yesterday.
Maa sister ninna kottha battalu konnindi.
33
My grandfather wakes up at 5 AM.
Maa thatha 5 AM ki lestaru.
34
My grandmother prepares traditional food.
Maa ammamma traditional food chestundi.
35
My brother studies late at night.
Maa brother night late gaa chadutadu.
36
My father pays the electricity bill online.
Maa nanna current bill online lo pay chestaru.
37
My mother waters the plants daily.
Maa amma daily mokkalaki neellu postundi.
38
My sister dances very gracefully.
Maa sister chala baga dance chestundi.
39
My cousin traveled to Chennai last week.
Naa cousin last week Chennai ki velladu.
40
My uncle drives a big truck.
Maa babai pedda truck drive chestaru.
41
My aunt teaches yoga classes.
Maa atta yoga classes cheptundi.
42
My family enjoys watching movies together.
Maa family kalisi movies choodadam enjoy chestundi.
43
My father encouraged me to learn English.
Maa nanna nannu English nerchukomani encourage chesaru.
AI Analysis
“encouraged” → past tense motivation action
44
My mother packed my lunch box.
Maa amma naa lunch box pack chesindi.
45
My brother fixed the computer problem.
Maa brother computer problem solve chesadu.
46
My sister talks politely with everyone.
Maa sister andaritho polite gaa maatladutundi.
47
My grandparents love spending time with us.
Maa grandparents maatho time spend cheyadam istapadtharu.
48
My cousin is learning spoken English.
Naa cousin spoken English nerchukuntunnadu.
49
My family motivates me every day.
Maa family nannu daily motivate chestundi.
50
I feel happy when my family is together.
Naa family andaru kalisi unnappudu nenu happy gaa feel avutanu.
AI Analysis
Emotional sentence
“when” used for condition/time relation
"""

    examples = []
    lines = [line.strip() for line in raw_data.strip().split('\n') if line.strip()]
    
    current_item = {}
    
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.isdigit():
            if current_item:
                examples.append(current_item)
            current_item = {"word": "Family", "en": "", "te": "", "sound": "Practice", "explanation": ""}
            i += 1
            if i < len(lines):
                current_item["en"] = lines[i]
                # Try to extract the first word or two for "word" field
                words = lines[i].split()
                if len(words) > 1:
                    if words[0].lower() in ["my", "our"]:
                        current_item["word"] = words[0] + " " + words[1]
                    else:
                        current_item["word"] = words[0]
                i += 1
            if i < len(lines) and not lines[i].startswith("AI Analysis"):
                current_item["te"] = lines[i]
                i += 1
        else:
            if current_item:
                if line.startswith("AI Analysis"):
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

    level1, _ = Level.objects.get_or_create(number=1, defaults={'title': 'Basics', 'description': 'Learn basics'})

    family_words, created = Concept.objects.get_or_create(
        slug='family-vocabulary',
        defaults={
            'name': 'Family Vocabulary',
            'level': level1,
            'formula': 'Subject + Verb + Object'
        }
    )

    family_words.content = content
    family_words.grammar_rules = rules
    family_words.examples = examples
    family_words.save()
    
    print(f"Database updated successfully! Concept {'created' if created else 'updated'} with 50 examples.")

if __name__ == "__main__":
    main()
