from django.db import models
from django.conf import settings

class OnlineUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_looking = models.BooleanField(default=False)
    last_active = models.DateTimeField(auto_now=True)
    level = models.CharField(max_length=20, default='Beginner') # Beginner, Intermediate, Advanced
    
    def __str__(self):
        return f"{self.user.username} - {'Looking' if self.is_looking else 'Idle'}"

class ConversationSession(models.Model):
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='session_user1')
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='session_user2')
    started_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Chat between {self.user1.username} and {self.user2.username}"
