from .models import Badge, UserBadge

def add_xp(user, amount):
    user.xp += amount
    user.save()
    check_badges(user)

def check_badges(user):
    available_badges = Badge.objects.filter(xp_required__lte=user.xp)
    for badge in available_badges:
        if not UserBadge.objects.filter(user=user, badge=badge).exists():
            UserBadge.objects.create(user=user, badge=badge)
            # Potentially send notification later

def update_streak(user):
    # Logic to check if last login was yesterday
    # For now, a simple increment for demo
    user.streak += 1
    user.save()
