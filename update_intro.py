import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept, Exercise

def main():
    intro_text = """Good morning Sir/Madam,

Thank you for giving me this opportunity to introduce myself.

My name is Sai Venkata Krishna Reddy, and I am from Machavaram.

Currently, I am pursuing my post-graduation at VSM College of Autonomous, Ramachandrapuram. I completed my undergraduate degree from the same college.

Coming to my technical skills, I know frontend technologies like HTML5 and CSS. I also have basic knowledge of JavaScript.

My strength is that I am always ready to take on new challenges and continuously improve myself to contribute to the growth of the company where I work.

Coming to my goals, my short-term goal is to get a job in a reputed multinational company. My long-term goal is to achieve a good position in the organization through hard work and dedication.

My hobbies are learning new skills and playing online games.

Coming to my family, we are a family of four members. My father is a farmer, my mother is a homemaker, and I have an elder sister.

This is all about me.

Thank you Sir/Madam."""

    try:
        self_intro = Concept.objects.get(slug='self-introduction')
    except Concept.DoesNotExist:
        print("Error: Concept 'self-introduction' does not exist.")
        return

    Exercise.objects.create(
        concept=self_intro,
        type='READ_ALOUD',
        question=intro_text,
        explanation="Practice reading this complete self-introduction clearly and confidently."
    )

    print("Successfully added self-introduction as a READ_ALOUD exercise in Phase 3.")

if __name__ == "__main__":
    main()
