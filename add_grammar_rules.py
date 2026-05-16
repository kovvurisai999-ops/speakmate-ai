import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept

rules_data = {
    "Adjectives": """
- Adjectives describe nouns or pronouns.
- They usually come before the noun (e.g., 'a red car') or after a linking verb (e.g., 'The car is red').
- Types include descriptive, quantitative, demonstrative, possessive, and interrogative.
- Adjectives have degrees of comparison: Positive (tall), Comparative (taller), Superlative (tallest).
""",
    "Adverbs": """
- Adverbs modify verbs, adjectives, or other adverbs.
- They tell us how, when, where, why, or to what degree an action is performed.
- Many adverbs of manner end in '-ly' (e.g., quickly, beautifully).
- Position: Adverbs can appear at the beginning, middle, or end of a sentence depending on what they modify.
""",
    "Conjunctions": """
- Conjunctions connect words, phrases, or clauses.
- Coordinating conjunctions (FANBOYS: For, And, Nor, But, Or, Yet, So) connect equal parts of a sentence.
- Subordinating conjunctions (Because, Although, If, Since, etc.) connect a dependent clause to an independent clause.
- Correlative conjunctions work in pairs (Both...and, Either...or, Neither...nor).
""",
    "Interjections": """
- Interjections express sudden or strong emotions like joy, surprise, pain, or disgust.
- They are usually followed by an exclamation mark (!).
- They are not grammatically connected to the rest of the sentence.
- Examples: Wow! Ouch! Hurrah! Alas! Oops!
""",
    "Active Voice": """
- In Active Voice, the subject performs the action.
- FORMULA: Subject + Verb + Object.
- It is direct, clear, and easy to read.
- Example: "The cat (Subject) caught (Verb) the mouse (Object)."
""",
    "Passive Voice": """
- In Passive Voice, the subject receives the action.
- FORMULA: Object + 'To be' verb + Past Participle (V3) + by + Subject.
- Used when the action is more important than who did it, or when the doer is unknown.
- Example: "The mouse (Object) was caught (Verb) by the cat (Subject)."
""",
    "Direct Speech": """
- Direct speech quotes the exact words spoken by a person.
- The spoken words are enclosed in quotation marks (" ").
- A comma usually separates the reporting verb from the quoted speech.
- Example: He said, "I am going to the market."
""",
    "Indirect Speech": """
- Indirect speech reports what someone said without quoting their exact words.
- Quotation marks are removed, and the conjunction 'that' is often used.
- Pronouns, tense, and time/place words change according to rules.
- Example: He said that he was going to the market.
""",
    "Modals": """
- Modal verbs express ability, permission, possibility, or obligation.
- Common modals: can, could, may, might, must, shall, should, will, would, ought to.
- They are always followed by the base form of the verb (V1) without 'to' (except 'ought to').
- Modals do not change form depending on the subject (no -s, -ed, or -ing).
""",
    "Question Tags": """
- Question tags are short questions added to the end of a statement to ask for confirmation.
- FORMULA: Auxiliary Verb + Pronoun?
- A positive statement takes a negative tag (e.g., You are coming, aren't you?).
- A negative statement takes a positive tag (e.g., She didn't call, did she?).
- Special case: "I am" takes the tag "aren't I?".
""",
    "Conditional Sentences": """
- Conditional sentences have two parts: the 'if' clause (condition) and the main clause (result).
- Zero Conditional: General truths (If + Present Simple, Present Simple).
- First Conditional: Real future possibilities (If + Present Simple, Will + V1).
- Second Conditional: Unreal present/future (If + Past Simple, Would + V1).
- Third Conditional: Unreal past (If + Past Perfect, Would have + V3).
"""
}

level2 = Level.objects.filter(number=2).first()
if level2:
    for concept_name, rules in rules_data.items():
        concept = Concept.objects.filter(level=level2, name=concept_name).first()
        if concept:
            concept.grammar_rules = rules.strip()
            concept.save()
            print(f"Updated rules for: {concept_name}")
        else:
            print(f"Concept '{concept_name}' not found.")
else:
    print("Level 2 not found.")
