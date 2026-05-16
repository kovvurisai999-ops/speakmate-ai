import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept, Exercise

def main():
    intro_text = """Introducing Myself

Good morning Sir / Mam,

Thankyou for giving this opportunity to introduce myself. My name is Sai Venkata Krishna Reddy. I'm from Machavara. I am pursuing post graduation in VSM college of autonomous Ramachandrapuram. I have done my under graduation in VSM college Ramachandrapuram. Coming to skills , I know the frontend languages like HTML5 , CSS ,I have basic knowledge of Javascript. And my strength is taking any challenges to develop the company where I’m work.

And coming to my goals , to get a job in any Multinational company. My long term goal is to get the best position. My hobbies are learning new skills , and online games.
And coming to family, I am from the family four. My father is a farmer and my mother is a home maker. I have a elder sister.

This is all about me.

THANK YOU SIR / MAM"""

    try:
        self_intro = Concept.objects.get(slug='self-introduction')
        # Update the existing READ_ALOUD exercise
        ex = Exercise.objects.get(concept=self_intro, type='READ_ALOUD')
        ex.question = intro_text
        ex.save()
        print("Successfully updated self-introduction text.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
