from django.db import models
from django.conf import settings
from django.utils import timezone

class DailyChallenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    xp_reward = models.IntegerField(default=10)
    challenge_type = models.CharField(max_length=50, choices=[
        ('RECORDING', 'Voice Recording'),
        ('CHAT', 'Chat Practice'),
        ('QUIZ', 'Grammar Quiz'),
        ('READING', 'Read Aloud'),
    ])

    def __str__(self):
        return self.title

class UserDailyChallenge(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='daily_challenges')
    challenge = models.ForeignKey(DailyChallenge, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'challenge', 'date')

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.created_at}"

class PlatformSettings(models.Model):
    is_emergency_shutdown = models.BooleanField(default=False)
    maintenance_mode = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Global Platform Settings"

class ChatReport(models.Model):
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports_sent')
    reported_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports_received')
    reason = models.TextField()
    evidence_audio = models.FileField(upload_to='chat_reports/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Report: {self.reporter} -> {self.reported_user}"

class ToxicDetection(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phrase = models.TextField()
    severity = models.FloatField() # 0 to 1
    room_id = models.CharField(max_length=100)
    detected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Toxic: {self.user.username} - {self.phrase[:20]}"

class ErrorLog(models.Model):
    ERROR_TYPES = [
        ('SERVER', 'Server Crash'),
        ('AI', 'AI API Failure'),
        ('VOICE', 'Speech Engine Error'),
        ('STRANGER', 'Stranger Chat Error'),
        ('DATABASE', 'Database Issue'),
        ('AUTH', 'Authentication Failure'),
    ]
    SEVERITY = [
        ('INFO', 'Information'),
        ('WARNING', 'Warning'),
        ('CRITICAL', 'Critical'),
    ]
    
    error_type = models.CharField(max_length=20, choices=ERROR_TYPES)
    severity = models.CharField(max_length=20, choices=SEVERITY, default='INFO')
    message = models.TextField()
    stack_trace = models.TextField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    browser = models.CharField(max_length=255, null=True, blank=True)
    os = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.severity}] {self.error_type}: {self.message[:50]}"

class Feedback(models.Model):
    CATEGORIES = [
        ('BUG', 'Report a Bug'),
        ('SUGGESTION', 'Suggestion'),
        ('COMPLAINT', 'Complaint'),
        ('OTHER', 'Other'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORIES, default='OTHER')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category}: {self.subject} by {self.user.username}"
