import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from roadmap.models import Concept, Level

def main():
    phase4_text = """
---
## Phase 4: Speaking Practice — Read Aloud

### Instructions for User

🎤 Click the mic button and read the sentence loudly.
🟢 Correctly spoken words turn **GREEN**.
🔴 Wrong pronunciation words turn **RED**.

**🤖 AI checks:**
* Pronunciation
* Fluency
* Confidence
* Grammar
* Speaking Speed
"""

    try:
        level1 = Level.objects.get(number=1)
        concepts = level1.concepts.all()
        
        for concept in concepts:
            if phase4_text not in concept.content:
                print(f"Adding Phase 4 instructions to {concept.slug}...")
                concept.content += phase4_text
                concept.save()
            else:
                print(f"Phase 4 instructions already exist for {concept.slug}.")
                
    except Level.DoesNotExist:
        print("Level 1 not found.")

if __name__ == "__main__":
    main()
