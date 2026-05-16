from django.core.management.base import BaseCommand
from roadmap.models import Level, Concept
from django.utils.text import slugify

LEVELS = [
    {"number": 1, "title": "BASIC ENGLISH", "description": "The foundation of your journey.", "color": "#6366f1"},
    {"number": 2, "title": "GRAMMAR FOUNDATION", "description": "Master the rules of the language.", "color": "#ec4899"},
    {"number": 3, "title": "DAILY CONVERSATION", "description": "Practical speaking for everyday life.", "color": "#8b5cf6"},
    {"number": 4, "title": "SPEAKING SKILLS", "description": "Improve your flow and confidence.", "color": "#f59e0b"},
    {"number": 5, "title": "ADVANCED COMMUNICATION", "description": "Professional and creative expression.", "color": "#10b981"},
    {"number": 6, "title": "PROFESSIONAL ENGLISH", "description": "Excel in your career and workplace.", "color": "#3b82f6"},
    {"number": 7, "title": "AI PRACTICE MODULES", "description": "Interactive AI-driven training.", "color": "#ef4444"},
    {"number": 8, "title": "SPECIAL TRAINING", "description": "Advanced personal development.", "color": "#06b6d4"},
    {"number": 9, "title": "ADVANCED AI FEATURES", "description": "Cutting-edge AI analytics.", "color": "#f43f5e"},
]

CONCEPTS = [
    # ─── LEVEL 1 ─────────────────────────────────────────────────────────────
    {
        "level": 1, "practice_url": "/pronunciation/",
        "name": "Alphabets & Pronunciation",
        "content": """
# Alphabets & Pronunciation

The English alphabet has **26 letters** — 5 vowels (**A E I O U**) and 21 consonants.

---

## Vowels vs Consonants

| Type | Letters |
|------|---------|
| Vowels | A, E, I, O, U |
| Consonants | All remaining 21 letters |

---

## How Sounds Work (Phonics)

Every letter has a **name** (what you call it) and a **sound** (how it is used in words).

- **B** = name "bee", sound like **b**all
- **C** = name "see", sound like **c**at
- **G** = name "jee", sound like **g**irl
- **H** = name "aitch", sound like **h**at

> **Tip:** Focus on the *sound*, not the name. When you read a word, your brain uses sounds, not names.

---

## Tricky Letters

| Letter | Example 1 | Example 2 |
|--------|-----------|-----------|
| C | **C**at (hard) | **C**ity (soft = S) |
| G | **G**irl (hard) | **G**em (soft = J) |
| Q | always with U → **Qu**een | |

---

## Practice Exercise

Say each of these aloud 3 times:
- **Apple, Ball, Cat, Dog, Elephant**
- **Fish, Girl, House, Ice, Juice**
"""
    },
    {
        "level": 1, "practice_url": "/chat/",
        "name": "Basic Vocabulary",
        "content": """
# Basic Vocabulary

Vocabulary is the collection of words you know. The more words you know, the better you can express yourself!

---

## Daily Essential Words

### Colors
**Red, Blue, Green, Yellow, Orange, Purple, Pink, White, Black, Brown**

### Numbers
**One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten**

### Family Words
| Telugu Meaning | English Word |
|----------------|--------------|
| అమ్మ | Mother |
| నాన్న | Father |
| అన్న/అక్క | Brother / Sister |
| తాత | Grandfather |
| నానమ్మ | Grandmother |

### Common Objects
**Book, Pen, Chair, Table, Phone, Door, Window, Bag, Clock, Key**

---

## Tips to Build Vocabulary

1. **Learn 5 new words every day**
2. **Use them in sentences** — don't just memorize lists
3. **Stick sticky notes** around your room with English labels
4. **Read anything** — apps, menus, signs — in English

> **Remember:** You don't need to know every word. Know the *right* words for your daily life first!
"""
    },
    {
        "level": 1, "practice_url": "/chat/",
        "name": "Greetings",
        "content": """
# Greetings in English

Greetings are the first words you say when you meet someone. A warm greeting creates a great first impression!

---

## Formal Greetings (Office / College)

| Situation | What to Say |
|-----------|-------------|
| Morning | "Good morning!" |
| Afternoon | "Good afternoon!" |
| Evening | "Good evening!" |
| Meeting someone | "Nice to meet you." |
| Asking how someone is | "How are you?" / "How do you do?" |

## Informal Greetings (Friends)

- "Hey! What's up?"
- "Hi! How's it going?"
- "Hello! Long time no see!"

---

## Responding to Greetings

| They say | You say |
|----------|---------|
| "How are you?" | "I'm fine, thank you! And you?" |
| "Nice to meet you." | "Nice to meet you too!" |
| "What's up?" | "Not much, just chilling!" |

---

## Goodbye Expressions

- "Goodbye!" / "Bye!"
- "See you later!"
- "Take care!"
- "Have a great day!"

> **Practice:** Greet at least 3 people in English today — even if it feels awkward, it gets easier every time!
"""
    },
    {
        "level": 1, "practice_url": "/chat/",
        "name": "Self Introduction",
        "content": """
# Self Introduction

A powerful self-introduction opens doors. Use this simple 4-part structure every time.

---

## The GHPA Formula

| Step | What to Say |
|------|-------------|
| **G** — Greeting | "Hello, Good morning!" |
| **H** — Hello & Name | "My name is Rajesh." |
| **P** — Place & Profession | "I am from Hyderabad. I work as a software engineer." |
| **A** — About (Hobbies) | "I love cricket and reading books." |

---

## Full Example

> "Hello everyone! My name is **Priya**. I am from **Visakhapatnam**, Andhra Pradesh.
> I am currently pursuing my **MCA** at XYZ College.
> In my free time, I love **dancing and listening to music**.
> I am very excited to be here. Thank you!"

---

## Key Phrases to Memorize

- "My name is ___"
- "I am from ___"
- "I work as a / I am studying ___"
- "My hobbies are ___"
- "Nice to meet you all!"

---

## Common Mistakes to Avoid

❌ "I am **Rajesh** here." → ✅ "My name is Rajesh." or "I am Rajesh."

❌ "I have interested in cricket." → ✅ "I am **interested** in cricket."

> **Practice tip:** Record yourself introducing yourself on your phone. Listen back and improve!
"""
    },
    {
        "level": 1, "practice_url": "/grammar/",
        "name": "Simple Sentences",
        "content": """
# Simple Sentences

Every English sentence needs two things: a **Subject** and a **Verb**.

`Subject + Verb + (Object)` — this is the basic sentence structure.

---

## Examples

| Sentence | Subject | Verb | Object |
|----------|---------|------|--------|
| I am happy. | I | am | happy |
| He plays cricket. | He | plays | cricket |
| She reads books. | She | reads | books |
| They are students. | They | are | students |

---

## Positive, Negative & Question

Take the sentence: **"He is my friend."**

| Type | Sentence |
|------|----------|
| ✅ Positive | He **is** my friend. |
| ❌ Negative | He **is not** my friend. |
| ❓ Question | **Is** he my friend? |

---

## Practice Sentences

Say these aloud and then make them negative:
1. I am a student.
2. She is a teacher.
3. They are happy.
4. He works in an office.

> **Rule of thumb:** When confused, just use `Subject + is/am/are + word`. That alone covers hundreds of situations!
"""
    },
    {
        "level": 1, "practice_url": "/grammar/",
        "name": "Parts of Speech",
        "content": """
# Parts of Speech

Every word in English belongs to a category called a "Part of Speech". Knowing these helps you build correct sentences.

---

## The 5 Key Parts

### 1. Noun — A Person, Place or Thing
> **Examples:** Rajesh, Hyderabad, book, happiness, dog

### 2. Pronoun — Replaces a Noun
> **Examples:** I, You, He, She, It, We, They
> `Rajesh is smart. **He** is smart.`

### 3. Verb — An Action or State
> **Examples:** run, eat, is, play, think
> `She **runs** every morning.`

### 4. Adjective — Describes a Noun
> **Examples:** beautiful, tall, happy, red, big
> `He has a **beautiful** voice.`

### 5. Adverb — Describes a Verb or Adjective
> **Examples:** quickly, very, always, well, here
> `She sings **beautifully**.`

---

## Quick Identification Test

Identify the parts of speech in this sentence:

**"The tall boy runs quickly."**

| Word | Part of Speech |
|------|---------------|
| The | Article |
| tall | Adjective |
| boy | Noun |
| runs | Verb |
| quickly | Adverb |

> **Pro Tip:** Adjectives come before nouns. Adverbs often end in **-ly**.
"""
    },

    # ─── LEVEL 2 ─────────────────────────────────────────────────────────────
    {
        "level": 2, "practice_url": "/grammar/",
        "name": "Tenses",
        "content": """
# English Tenses — Master Guide

Tenses tell us **WHEN** an action happens. There are 3 main tenses, each with 4 sub-types.

---

## Present Tense

| Type | Structure | Example |
|------|-----------|---------|
| Simple Present | Subject + V1 | I **eat** rice every day. |
| Present Continuous | Subject + is/am/are + V-ing | I **am eating** rice now. |
| Present Perfect | Subject + has/have + V3 | I **have eaten** rice. |

---

## Past Tense

| Type | Structure | Example |
|------|-----------|---------|
| Simple Past | Subject + V2 | I **ate** rice yesterday. |
| Past Continuous | Subject + was/were + V-ing | I **was eating** when you called. |
| Past Perfect | Subject + had + V3 | I **had eaten** before he came. |

---

## Future Tense

| Type | Structure | Example |
|------|-----------|---------|
| Simple Future | Subject + will + V1 | I **will eat** rice tomorrow. |
| Future Continuous | Subject + will be + V-ing | I **will be eating** at 7pm. |

---

## Common Irregular Verbs

| V1 (Present) | V2 (Past) | V3 (Past Participle) |
|---|---|---|
| go | went | gone |
| eat | ate | eaten |
| write | wrote | written |
| speak | spoke | spoken |
| do | did | done |

> **Key Tip:** For daily conversation, master Simple Present, Simple Past and Simple Future first. Then add the others!
"""
    },

    # ─── LEVEL 3 ─────────────────────────────────────────────────────────────
    {
        "level": 3, "practice_url": "/chat/",
        "name": "Daily Use Sentences",
        "content": """
# Daily Use English Sentences

These are real sentences you can use every single day. Memorize them and use them!

---

## At Home

- "Mom, I'm going to college."
- "Please pass me the salt."
- "I'll be back by 6 PM."
- "Can you turn off the fan?"

## At College / Office

- "Excuse me, can I ask a question?"
- "Could you please repeat that?"
- "I'll finish this by today."
- "I have a meeting at 3 o'clock."

## Shopping

- "How much does this cost?"
- "Do you have a smaller size?"
- "Can I get a discount?"
- "I'll take this one, please."

## Restaurant

- "Can I see the menu, please?"
- "I'd like to order [dish name]."
- "This is delicious!"
- "Could I have the bill, please?"

## Travel

- "Which bus goes to the railway station?"
- "How far is it from here?"
- "Could you drop me at this address?"
- "Is this seat taken?"

---

> **Challenge:** Pick 5 sentences from above and use them in real life today!
"""
    },
    {
        "level": 3, "practice_url": "/chat/",
        "name": "Asking Questions",
        "content": """
# Asking Questions in English

Knowing how to ask questions is essential for conversation. Use the **5W + 1H** method!

---

## The 5W + 1H Question Words

| Word | Use | Example |
|------|-----|---------|
| **What** | Thing / Information | "What is your name?" |
| **Who** | Person | "Who is your teacher?" |
| **When** | Time | "When is your birthday?" |
| **Where** | Place | "Where do you live?" |
| **Why** | Reason | "Why are you late?" |
| **How** | Manner / Degree | "How are you?" / "How much?" |

---

## Yes/No Questions

Use **Do / Does / Is / Are / Can** at the start:

- "**Do** you speak English?"
- "**Is** he coming to the party?"
- "**Can** you help me?"

---

## Polite Question Forms

Instead of direct questions, use these polite forms:

| Direct | Polite |
|--------|--------|
| "What is your name?" | "**Could you tell me** your name?" |
| "Where is the station?" | "**Do you know** where the station is?" |
| "How much does it cost?" | "**Would you mind telling me** the price?" |

---

> **Practice:** Think of 5 questions to ask your AI chat partner right now!
"""
    },
    {
        "level": 3, "practice_url": "/chat/",
        "name": "Answering Skills",
        "content": """
# Answering Skills

Great speakers don't just answer — they answer **clearly**, **confidently**, and **completely**.

---

## Short Answers (Yes/No Questions)

| Question | Short Answer | Full Answer |
|----------|-------------|------------|
| "Are you a student?" | "Yes, I am." | "Yes, I am currently studying MCA." |
| "Do you speak Hindi?" | "Yes, I do." | "Yes, I speak Hindi and Telugu." |
| "Is it raining?" | "No, it isn't." | "No, it stopped raining an hour ago." |

---

## Answering "Tell me about..." Questions

Use the **3-Part Answer** structure:
1. **Direct answer** — Answer the question directly
2. **Support** — Give a reason or example
3. **Close** — End confidently

> **Example:** "What do you like about your college?"
> "I really enjoy the library facilities. **(Direct)**
> The library has a large collection of books and fast internet. **(Support)**
> It's a great place for me to study and improve myself." **(Close)**

---

## Filler Phrases (while you think)

Instead of silence or "um... uh...", use:
- "That's a great question. Let me think..."
- "Well, to be honest..."
- "That's interesting. I'd say..."
- "From my experience..."

---

> **Golden Rule:** Never leave a question with just "Yes" or "No". Always add one more sentence!
"""
    },
]


class Command(BaseCommand):
    help = 'Seeds roadmap concepts for Levels 1–3'

    def handle(self, *args, **kwargs):
        for l in LEVELS:
            Level.objects.update_or_create(number=l['number'], defaults=l)
            self.stdout.write(f"  Level {l['number']} ready.")

        for c in CONCEPTS:
            level = Level.objects.get(number=c['level'])
            Concept.objects.update_or_create(
                slug=slugify(c['name']),
                defaults={
                    "level": level,
                    "name": c['name'],
                    "content": c['content'].strip(),
                    "practice_url": c['practice_url'],
                }
            )
            self.stdout.write(f"  [OK] {c['name']}")

        self.stdout.write(self.style.SUCCESS('Levels 1-3 seeded successfully!'))
