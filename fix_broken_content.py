import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept

content_data = {
    "Present Perfect": "The Present Perfect tense is used to describe an action that happened at an unspecified time before now, or an action that started in the past and continues to the present. It connects the past to the present.",
    "Present Perfect Continuous": "The Present Perfect Continuous tense is used to show that an action started in the past and has continued up to the present moment. It emphasizes the duration or continuous course of the action.",
    "Simple Past": "The Simple Past tense is used to talk about a completed action in a time before now. The time of the action can be in the recent past or the distant past, and action duration is not important.",
    "Past Continuous": "The Past Continuous tense describes actions or events that began in the past, were ongoing at a specific time, and were possibly interrupted by another action.",
    "Past Perfect": "The Past Perfect tense is used to make it clear that one event happened before another in the past. It does not matter which event is mentioned first.",
    "Past Perfect Continuous": "The Past Perfect Continuous tense shows that an action that started in the past continued up until another time in the past.",
    "Simple Future": "The Simple Future tense is used to talk about things that haven't happened yet. We use it to make predictions, promises, or decisions about the future.",
    "Future Continuous": "The Future Continuous tense indicates that something will occur in the future and continue for an expected length of time.",
    "Future Perfect": "The Future Perfect tense is used for actions that will be completed before some other point in the future.",
    "Future Perfect Continuous": "The Future Perfect Continuous tense is used to describe an ongoing action that will be completed at some specified time in the future.",
    "Nouns": "A noun is a word that functions as the name of a specific object or set of objects, such as living creatures, places, actions, qualities, states of existence, or ideas.",
    "Pronouns": "A pronoun is a word that replaces a noun in a sentence. Pronouns are used to avoid repeating the same nouns over and over again.",
    "Verbs": "A verb is a word used to describe an action, state, or occurrence, and forming the main part of the predicate of a sentence.",
    "Helping Verbs": "Helping verbs (also known as auxiliary verbs) help the main verb to describe action or state of being. They help to clarify tense, mood, or voice.",
    "Articles": "Articles are words that define a noun as specific or unspecific. English has two types of articles: definite ('the') and indefinite ('a', 'an').",
    "Prepositions": "A preposition is a word or group of words used before a noun, pronoun, or noun phrase to show direction, time, place, location, spatial relationships, or to introduce an object.",
    "Adjectives": "An adjective is a word that describes or modifies a noun or pronoun. It gives more information about an object's size, shape, age, color, origin or material.",
    "Adverbs": "An adverb is a word that modifies a verb, an adjective, another adverb, or even a whole sentence. Adverbs often end in -ly, but some look exactly the same as their adjective counterparts.",
    "Conjunctions": "A conjunction is a word used to connect clauses or sentences or to coordinate words in the same clause (e.g., and, but, if).",
    "Interjections": "An interjection is a word or phrase that expresses a strong emotion. It is a short exclamation, sometimes inserted into a sentence.",
    "Active Voice": "In the active voice, the subject of the sentence performs the action expressed by the verb. The focus is on the doer of the action.",
    "Passive Voice": "In the passive voice, the subject of the sentence receives the action. The focus is on the action itself or the receiver of the action, rather than the doer.",
    "Direct Speech": "Direct speech is a sentence in which the exact words spoken are reproduced in speech marks (quotation marks).",
    "Indirect Speech": "Indirect speech (also called reported speech) is when we tell someone what another person said without using their exact words.",
    "Modals": "Modal verbs (or modals) are helping verbs that express necessity, ability, permission, or possibility (e.g., can, could, must, should).",
    "Question Tags": "A question tag is a short question added to the end of a statement. It is used to check if the statement is true or to ask for agreement.",
    "Conditional Sentences": "Conditional sentences describe the result of a certain condition. The 'if' clause tells you the condition, and the main clause tells you the result."
}

level2 = Level.objects.filter(number=2).first()
if level2:
    for concept_name, content in content_data.items():
        concept = Concept.objects.filter(level=level2, name=concept_name).first()
        if concept:
            concept.content = content.strip()
            concept.save()
            print(f"Fixed content for: {concept_name}")
        else:
            print(f"Concept '{concept_name}' not found.")
else:
    print("Level 2 not found.")
