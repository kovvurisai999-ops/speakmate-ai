import json
import random
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@login_required
def stranger_dashboard(request):
    return render(request, 'stranger_practice/dashboard.html')


# ── Conversation Topics ──────────────────────────────────────
TOPICS = [
    "What is your dream job and why?",
    "Tell me about a place you want to travel to.",
    "What is your favorite food from your hometown?",
    "If you could have any superpower, what would it be?",
    "What was the most interesting thing that happened to you this week?",
    "How do you usually spend your weekends?",
    "Tell me about your favorite movie and why you liked it.",
    "What are your hobbies besides learning English?",
    "Describe a person you admire the most.",
    "What would you do if you won the lottery?",
    "Tell me about a memorable trip you have taken.",
    "What is the most important skill in life? Why?",
    "If you could live in any country, where would you choose?",
    "Describe your perfect day from morning to night.",
    "What is the biggest challenge you have faced in life?",
    "Tell me about an achievement you are proud of.",
    "How do you think technology will change education?",
    "What advice would you give to your younger self?",
    "Describe a book or movie that changed your perspective.",
    "What qualities make a good leader?",
]


@login_required
def get_topic(request):
    """Return a random conversation topic."""
    topic = random.choice(TOPICS)
    return JsonResponse({"topic": topic})


@login_required
@require_POST
def analyze_speech(request):
    """
    HTTP-based grammar analysis for the AI Practice mode.
    Replaces the WebSocket-based feedback loop.
    """
    try:
        data = json.loads(request.body)
        text = data.get("text", "").strip()

        if not text:
            return JsonResponse({"feedback": "Please speak something.", "is_valid": False})

        # Use GrammarChecker for analysis
        from grammar.utils import GrammarChecker
        checker = GrammarChecker()
        correction, feedback, is_valid = checker.check(text)

        # Generate AI coaching tip based on the sentence
        coaching_tip = ""
        if is_valid:
            word_count = len(text.split())
            if word_count < 5:
                coaching_tip = "Try speaking longer sentences for better fluency practice."
            elif word_count < 10:
                coaching_tip = "Good sentence length! Try adding more descriptive words."
            else:
                coaching_tip = "Excellent sentence structure! Keep up the great work."
        else:
            coaching_tip = "Don't worry about mistakes — they help you learn faster!"

        return JsonResponse({
            "original": text,
            "correction": correction,
            "feedback": feedback,
            "is_valid": is_valid,
            "coaching_tip": coaching_tip,
        })

    except Exception as e:
        return JsonResponse({"feedback": f"Analysis error: {str(e)}", "is_valid": False}, status=500)
