from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    native_language = models.CharField(max_length=50, default='Telugu')
    learning_goals = models.TextField(blank=True)
    xp = models.IntegerField(default=0)
    streak = models.IntegerField(default=0)
    is_premium = models.BooleanField(default=False)
    
    # Settings Fields
    ai_voice = models.CharField(max_length=50, default='Female - American')
    ai_difficulty = models.CharField(max_length=20, default='Beginner')
    speaking_speed = models.FloatField(default=1.0) # 0.5 to 2.0
    app_theme = models.CharField(max_length=50, default='Dark Neon')
    ai_personality = models.CharField(max_length=50, default='Friendly Teacher')
    preferred_language = models.CharField(max_length=20, default='English')
    
    # Notification Settings (Stored as JSON or simple flags)
    notifications_enabled = models.BooleanField(default=True)
    privacy_visible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.username

class Badge(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.CharField(max_length=50) # FontAwesome icon name
    xp_required = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class UserBadge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='badges')
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)
