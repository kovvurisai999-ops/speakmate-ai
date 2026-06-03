from django.db import models
from django.conf import settings

class InterviewSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, default='Software Engineer')
    experience_level = models.CharField(max_length=50, default='Fresher')
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    overall_score = models.IntegerField(default=0)
    feedback = models.TextField(blank=True)
    extracted_skills = models.TextField(blank=True) # JSON stored as text

    def __str__(self):
        return f"{self.user.username} - {self.position} - {self.created_at}"

class InterviewQuestion(models.Model):
    session = models.ForeignKey(InterviewSession, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    user_answer = models.TextField(blank=True)
    ai_feedback = models.TextField(blank=True)
    score = models.IntegerField(default=0)
    audio_response = models.FileField(upload_to='interview_audio/', blank=True, null=True)
