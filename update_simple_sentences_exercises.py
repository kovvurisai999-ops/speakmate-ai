import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept, Exercise

def main():
    data = """
1
I _____ coffee every morning.
Answer: drink
Meaning: Nenu prati morning coffee taguthanu.
2
She _____ to college daily.
Answer: goes
Meaning: Aame daily college ki velthundi.
Explanation
"She" singular subject kabatti "goes".
3
My father _____ in a bank.
Answer: works
Meaning: Maa nanna bank lo work chestaru.
4
I _____ cricket with friends.
Answer: play
Meaning: Nenu friends tho cricket aaduthanu.
5
We _____ movies together.
Answer: watch
Meaning: Memu kalisi movies chustham.
6
My mother _____ tasty food.
Answer: cooks
Meaning: Maa amma tasty food chestundi.
7
The baby is _____.
Answer: sleeping
Meaning: Baby nidrapothundi.
8
I _____ up at 6 AM.
Answer: wake
Meaning: Nenu 6 AM ki lestanu.
9
He _____ carefully.
Answer: drives
Meaning: Athanu jagrathaga drive chestadu.
10
My sister _____ music.
Answer: likes
Meaning: Maa sister ki music istam.
11
The bus _____ late.
Answer: arrived
Meaning: Bus late gaa vachindi.
12
I _____ my homework.
Answer: completed
Meaning: Nenu homework complete chesanu.
13
They are _____ football.
Answer: playing
Meaning: Vallu football aadutunnaru.
14
My friend _____ a laptop.
Answer: bought
Meaning: Naa friend laptop konnadu.
15
The teacher _____ the lesson.
Answer: explained
Meaning: Teacher lesson explain chesaru.
Explanation
Past completed action kabatti past tense verb.
16
I am _____ spoken English.
Answer: learning
Meaning: Nenu spoken English nerchukuntunnanu.
17
My brother _____ YouTube daily.
Answer: watches
Meaning: Maa brother daily YouTube chustadu.
18
We _____ Hyderabad last month.
Answer: visited
Meaning: Memu Hyderabad vellam.
19
The dog _____ loudly.
Answer: barked
Meaning: Kukka gattiga arichindi.
20
She speaks English _____.
Answer: fluently
Meaning: Aame English fluently maatladutundi.
Explanation
"fluently" adverb.
Speaking style ni describe chestundi.
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
        concept = Concept.objects.get(slug='simple-sentences')
    except Concept.DoesNotExist:
        print("Error: Concept 'simple-sentences' not found in database.")
        return

    deleted, _ = Exercise.objects.filter(concept=concept, type='FILL_BLANK').delete()
    print(f"Deleted {deleted} old FILL_BLANK exercises.")

    # MCQ options per answer verb
    options_map = {
        'drink':     ['drink', 'eat', 'sleep'],
        'goes':      ['goes', 'go', 'went'],
        'works':     ['works', 'work', 'worked'],
        'play':      ['play', 'plays', 'played'],
        'watch':     ['watch', 'watches', 'watched'],
        'cooks':     ['cooks', 'cook', 'cooked'],
        'sleeping':  ['sleeping', 'running', 'eating'],
        'wake':      ['wake', 'woke', 'sleep'],
        'drives':    ['drives', 'drive', 'drove'],
        'likes':     ['likes', 'like', 'liked'],
        'arrived':   ['arrived', 'arrive', 'comes'],
        'completed': ['completed', 'complete', 'finish'],
        'playing':   ['playing', 'played', 'plays'],
        'bought':    ['bought', 'buy', 'buys'],
        'explained': ['explained', 'explain', 'teaches'],
        'learning':  ['learning', 'learned', 'teaches'],
        'watches':   ['watches', 'watch', 'watched'],
        'visited':   ['visited', 'visit', 'go'],
        'barked':    ['barked', 'bark', 'runs'],
        'fluently':  ['fluently', 'loudly', 'slowly'],
    }

    created_count = 0
    for ex in exercises:
        ans = ex['answer']
        options = options_map.get(ans, [ans, 'is', 'was'])
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

    print(f"Database updated! Created {created_count} FILL_BLANK exercises for Simple Sentences.")

if __name__ == "__main__":
    main()
