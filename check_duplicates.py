import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept, Exercise

duplicated = []
concepts = Concept.objects.all()

for c in concepts:
    if c.examples:
        unique_ex = len({ex.get('en', '') for ex in c.examples if isinstance(ex, dict)})
        if unique_ex < len(c.examples):
            duplicated.append(c.name)

print(f"Total concepts with duplicated examples: {len(duplicated)}")
print("Concepts:", duplicated)
