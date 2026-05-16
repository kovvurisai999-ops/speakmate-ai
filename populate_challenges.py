import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_project.settings')
django.setup()

from dashboard.models import DailyChallenge

challenges = [
    {
        'title': 'Morning Greeting',
        'description': 'Record a 30-second introduction.',
        'challenge_type': 'RECORDING',
        'xp_reward': 20
    },
    {
        'title': 'New Words',
        'description': 'Use 5 new vocabulary words in a chat.',
        'challenge_type': 'CHAT',
        'xp_reward': 15
    },
    {
        'title': 'Grammar Master',
        'description': 'Complete 3 grammar exercises perfectly.',
        'challenge_type': 'QUIZ',
        'xp_reward': 25
    },
    {
        'title': 'Reading Aloud',
        'description': 'Read a story aloud for 2 minutes.',
        'challenge_type': 'READING',
        'xp_reward': 20
    },
    {
        'title': 'Daily Chat',
        'description': 'Have a 5-minute conversation with AI.',
        'challenge_type': 'CHAT',
        'xp_reward': 30
    },
    {
        'title': 'Pronunciation Pro',
        'description': 'Practice 10 difficult words pronunciation.',
        'challenge_type': 'RECORDING',
        'xp_reward': 20
    }
]

for c in challenges:
    DailyChallenge.objects.get_or_create(
        title=c['title'],
        defaults={
            'description': c['description'],
            'challenge_type': c['challenge_type'],
            'xp_reward': c['xp_reward']
        }
    )

print("Daily challenges populated successfully.")
