import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept

level2 = Level.objects.filter(number=2).first()
if level2:
    concepts = Concept.objects.filter(level=level2)
    bad_content = []
    
    for c in concepts:
        if c.content and ("Error" in c.content or "trouble thinking" in c.content):
            bad_content.append(c.name)
            
    print("Concepts with broken 'content':", bad_content)
