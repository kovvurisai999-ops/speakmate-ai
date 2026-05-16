import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept, Exercise

level_2 = Level.objects.filter(number=2).first()
if not level_2:
    print("Level 2 not found.")
    sys.exit()

for concept in level_2.concepts.all():
    examples_count = len(concept.examples) if isinstance(concept.examples, list) else 0
    blanks_count = concept.exercises.filter(type='FILL_BLANK').count()
    read_aloud_count = concept.exercises.filter(type='READ_ALOUD').count()
    
    print(f"{concept.name}: Examples: {examples_count}/50, Blanks: {blanks_count}/30, Speaking: {read_aloud_count}/30")
