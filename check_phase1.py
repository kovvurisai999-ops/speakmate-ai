import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Level, Concept

level2 = Level.objects.filter(number=2).first()
if not level2:
    print("Level 2 not found.")
else:
    concepts = Concept.objects.filter(level=level2)
    missing_phase1 = []
    
    for c in concepts:
        missing = []
        if not c.content or len(c.content.strip()) < 10:
            missing.append("content")
        if not c.grammar_rules or len(c.grammar_rules.strip()) < 10:
            missing.append("grammar_rules")
        
        if missing:
            missing_phase1.append(f"{c.name}: Missing {', '.join(missing)}")
            
    print(f"Total concepts checked: {concepts.count()}")
    print("Concepts missing Phase 1 data:")
    for m in missing_phase1:
        print(f"- {m}")
