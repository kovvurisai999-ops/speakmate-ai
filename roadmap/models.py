from django.db import models

class Level(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    color = models.CharField(max_length=20, default="#6366f1")

    def __str__(self):
        return f"Level {self.number}: {self.title}"

class Concept(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='concepts')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField(help_text="Detailed explanation of the concept")
    formula = models.CharField(max_length=200, blank=True, null=True, help_text="Grammar Formula (e.g. S+V+O)")
    grammar_rules = models.TextField(blank=True, null=True, help_text="Key rules for this concept")
    examples = models.JSONField(default=list, help_text="[{'en': '...', 'te': '...', 'explanation': '...'}]")
    common_mistakes = models.JSONField(default=list, help_text="[{'wrong': '...', 'right': '...', 'why': '...'}]")
    video_url = models.URLField(blank=True, null=True)
    practice_url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.level.number}. {self.name}"

class Exercise(models.Model):
    EXERCISE_TYPES = (
        ('FILL_BLANK', 'Fill in the Blank'),
        ('READ_ALOUD', 'Read Aloud'),
        ('WRITING', 'Sentence Writing'),
    )
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='exercises')
    type = models.CharField(max_length=20, choices=EXERCISE_TYPES)
    question = models.TextField()
    correct_answer = models.TextField(blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)
    hint = models.CharField(max_length=200, blank=True, null=True)
    options = models.JSONField(default=list, blank=True, null=True, help_text="For Fill in the Blank choices")
    telugu_meaning = models.TextField(blank=True, null=True)
    difficulty = models.CharField(max_length=20, default='Beginner') # Beginner, Intermediate, Advanced
    category = models.CharField(max_length=50, default='General') # home, office, interview, etc.

    def __str__(self):
        return f"{self.concept.name} - {self.get_type_display()}"

from django.conf import settings

class UserConceptProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    last_practiced = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'concept')
