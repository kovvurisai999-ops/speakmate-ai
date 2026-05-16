from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db import models
from roadmap.models import UserConceptProgress
from .models import DailyChallenge, UserDailyChallenge, Feedback
import random
import json
from django.contrib import messages

@login_required
def submit_feedback(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')
        
        Feedback.objects.create(
            user=request.user,
            category=category,
            subject=subject,
            message=message_text
        )
        messages.success(request, "Thank you! Your feedback has been submitted to the admin.")
        return redirect('dashboard:settings')
    return redirect('dashboard:settings')

@login_required
def dashboard_index(request):
    user = request.user
    
    # 1. Calculate Real Statistics
    if user.is_staff:
        # Admin view: Show global stats
        from django.contrib.auth import get_user_model
        User = get_user_model()
        lessons_completed = UserConceptProgress.objects.filter(is_completed=True).count()
        total_users = User.objects.count()
        average_score = UserConceptProgress.objects.all().aggregate(models.Avg('score'))['score__avg'] or 0
        average_score = round(average_score)
    else:
        # Regular user view: Show only their stats
        lessons_completed = UserConceptProgress.objects.filter(user=user, is_completed=True).count()
        progress_records = UserConceptProgress.objects.filter(user=user)
        if progress_records.exists():
            total_score = sum(record.score for record in progress_records)
            average_score = round(total_score / progress_records.count())
        else:
            average_score = 0

    # 2. Daily Challenges Management
    today = timezone.now().date()
    user_challenges = UserDailyChallenge.objects.filter(user=user, date=today)
    
    if not user_challenges.exists():
        # Assign 2 random challenges for today
        all_challenges = list(DailyChallenge.objects.all())
        if len(all_challenges) >= 2:
            selected_challenges = random.sample(all_challenges, 2)
            for challenge in selected_challenges:
                UserDailyChallenge.objects.create(user=user, challenge=challenge, date=today)
            user_challenges = UserDailyChallenge.objects.filter(user=user, date=today)

    # 3. Get Last Completed Task
    last_completed = UserConceptProgress.objects.filter(user=user, is_completed=True).order_by('-last_practiced').first()

    context = {
        'lessons_completed': lessons_completed,
        'average_score': average_score,
        'user_challenges': user_challenges,
        'last_completed': last_completed,
        'is_admin': user.is_staff,
    }
    
    return render(request, 'dashboard/index.html', context)

@login_required
def analytics_view(request):
    user = request.user
    
    # 1. Weekly Progress Data
    today = timezone.now().date()
    days = []
    lesson_counts = []
    scores = []
    
    for i in range(6, -1, -1):
        date = today - timezone.timedelta(days=i)
        days.append(date.strftime('%a'))
        
        if user.is_staff:
            # Global analytics for admin
            count = UserConceptProgress.objects.filter(is_completed=True, last_practiced__date=date).count()
            daily_records = UserConceptProgress.objects.filter(last_practiced__date=date)
        else:
            # Personal analytics for user
            count = UserConceptProgress.objects.filter(user=user, is_completed=True, last_practiced__date=date).count()
            daily_records = UserConceptProgress.objects.filter(user=user, last_practiced__date=date)
            
        lesson_counts.append(count)
        
        if daily_records.exists():
            avg = sum(r.score for r in daily_records) / daily_records.count()
            scores.append(round(avg))
        else:
            scores.append(0)

    # 2. Mastery Data
    if user.is_staff:
        mastery_data = UserConceptProgress.objects.all().order_by('-score')[:10]
    else:
        mastery_data = UserConceptProgress.objects.filter(user=user).order_by('-score')[:5]

    context = {
        'days': json.dumps(days),
        'lesson_counts': json.dumps(lesson_counts),
        'scores': json.dumps(scores),
        'mastery_data': mastery_data,
        'is_admin': user.is_staff,
    }
    
    return render(request, 'dashboard/analytics.html', context)

@login_required
def settings_view(request):
    user = request.user
    if request.method == 'POST':
        user.ai_voice = request.POST.get('ai_voice', user.ai_voice)
        user.ai_difficulty = request.POST.get('ai_difficulty', user.ai_difficulty)
        user.speaking_speed = float(request.POST.get('speaking_speed', user.speaking_speed))
        user.app_theme = request.POST.get('app_theme', user.app_theme)
        user.ai_personality = request.POST.get('ai_personality', user.ai_personality)
        user.preferred_language = request.POST.get('preferred_language', user.preferred_language)
        user.notifications_enabled = request.POST.get('notifications') == 'on'
        user.privacy_visible = request.POST.get('privacy') == 'on'
        user.save()
        
    return render(request, 'dashboard/settings.html', {'user': user})

from django.contrib.auth import get_user_model
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_dashboard_view(request):
    User = get_user_model()
    
    # 1. Stats Cards
    total_users = User.objects.count()
    active_users = User.objects.filter(last_login__gte=timezone.now() - timezone.timedelta(days=7)).count()
    premium_users = User.objects.filter(is_premium=True).count()
    daily_active = User.objects.filter(last_login__date=timezone.now().date()).count()
    
    # 2. Recent Feedback
    recent_feedback = Feedback.objects.all().order_by('-created_at')[:10]
    
    # 3. Recent Activity (Latest progress records)
    recent_activity = UserConceptProgress.objects.all().order_by('-last_practiced')[:15]
    
    # 4. AI Stats (Simulated for now based on total records)
    ai_requests = UserConceptProgress.objects.count() * 5 # Each lesson approx 5 requests
    
    context = {
        'total_users': total_users,
        'active_users': active_users,
        'premium_users': premium_users,
        'daily_active': daily_active,
        'recent_feedback': recent_feedback,
        'recent_activity': recent_activity,
        'ai_requests': ai_requests,
    }
    
    return render(request, 'dashboard/admin_dashboard.html', context)

@staff_member_required
def admin_users_view(request):
    User = get_user_model()
    query = request.GET.get('q', '')
    if query:
        users = User.objects.filter(
            models.Q(username__icontains=query) | 
            models.Q(email__icontains=query)
        ).order_by('-date_joined')
    else:
        users = User.objects.all().order_by('-date_joined')[:50]
    
    context = {
        'users': users,
        'query': query,
    }
    return render(request, 'dashboard/admin_users.html', context)

@staff_member_required
def admin_user_detail_view(request, user_id):
    from django.shortcuts import get_object_or_404
    User = get_user_model()
    target_user = get_object_or_404(User, id=user_id)
    
    # 1. Progress Stats
    progress_records = UserConceptProgress.objects.filter(user=target_user).order_by('-last_practiced')
    lessons_completed = progress_records.filter(is_completed=True).count()
    
    if progress_records.exists():
        avg_score = sum(r.score for r in progress_records) / progress_records.count()
    else:
        avg_score = 0
        
    # 2. Activity Timeline
    timeline = progress_records[:20]
    
    context = {
        'target_user': target_user,
        'lessons_completed': lessons_completed,
        'avg_score': round(avg_score),
        'timeline': timeline,
    }
    return render(request, 'dashboard/admin_user_detail.html', context)

@staff_member_required
def admin_user_action(request, user_id):
    from django.shortcuts import get_object_or_404
    from django.contrib import messages
    User = get_user_model()
    target_user = get_object_or_404(User, id=user_id)
    
    action = request.POST.get('action')
    if action == 'ban':
        target_user.is_active = False
        target_user.save()
        messages.success(request, f"User {target_user.username} has been banned.")
    elif action == 'unban':
        target_user.is_active = True
        target_user.save()
        messages.success(request, f"User {target_user.username} has been unbanned.")
    elif action == 'warn':
        # Simulated warning (could send a notification in a real app)
        messages.info(request, f"Warning sent to {target_user.username}.")
        
    return redirect('dashboard:admin_user_detail', user_id=user_id)

@staff_member_required
def admin_level_detail(request, level_id):
    from roadmap.models import Level, Concept
    from django.shortcuts import get_object_or_404
    level = get_object_or_404(Level, id=level_id)
    concepts = level.concepts.all().order_by('id')
    
    context = {
        'level': level,
        'concepts': concepts,
    }
    return render(request, 'dashboard/admin_level_detail.html', context)

@staff_member_required
def admin_concept_edit_view(request, concept_id):
    from roadmap.models import Concept
    from django.shortcuts import get_object_or_404
    from django.contrib import messages
    concept = get_object_or_404(Concept, id=concept_id)
    
    if request.method == 'POST':
        concept.name = request.POST.get('name')
        concept.content = request.POST.get('content')
        concept.examples = request.POST.get('examples')
        concept.exercises = request.POST.get('exercises')
        concept.grammar_rules = request.POST.get('grammar_rules')
        concept.common_mistakes = request.POST.get('common_mistakes')
        concept.save()
        messages.success(request, f"Concept '{concept.name}' updated successfully.")
        return redirect('dashboard:admin_level_detail', level_id=concept.level.id)
        
    return render(request, 'dashboard/admin_concept_edit.html', {'concept': concept})

@staff_member_required
def admin_concept_delete(request, concept_id):
    from roadmap.models import Concept
    from django.shortcuts import get_object_or_404
    from django.contrib import messages
    concept = get_object_or_404(Concept, id=concept_id)
    level_id = concept.level.id
    name = concept.name
    concept.delete()
    messages.success(request, f"Concept '{name}' deleted successfully.")
    return redirect('dashboard:admin_level_detail', level_id=level_id)

@staff_member_required
def admin_lesson_builder(request):
    if request.method == 'POST':
        topic = request.POST.get('topic')
        level_id = request.POST.get('level_id')
        # Here we will add the AI logic later
        messages.success(request, f"AI Lesson Builder started for: {topic}")
        return redirect('dashboard:admin_content')
        
    from roadmap.models import Level
    levels = Level.objects.all().order_by('number')
    return render(request, 'dashboard/admin_lesson_builder.html', {'levels': levels})

@staff_member_required
def admin_content_view(request):
    from roadmap.models import Concept, Level
    levels = Level.objects.all().order_by('number')
    concepts_count = Concept.objects.count()
    
    context = {
        'levels': levels,
        'concepts_count': concepts_count,
    }
    return render(request, 'dashboard/admin_content.html', context)

@staff_member_required
def admin_safety_view(request):
    from stranger_practice.models import ConversationSession
    from .models import PlatformSettings, ChatReport, ToxicDetection
    
    # 1. Real Counts
    active_rooms = ConversationSession.objects.filter(is_active=True).count()
    reported_users = ChatReport.objects.filter(is_resolved=False).count()
    toxic_detections = ToxicDetection.objects.count()
    
    settings, _ = PlatformSettings.objects.get_or_create(id=1)
    
    # 2. Live Monitoring (Latest sessions)
    live_sessions = ConversationSession.objects.filter(is_active=True).order_by('-started_at')[:10]
    
    # 3. Toxic Logs
    toxic_logs = ToxicDetection.objects.all().order_by('-detected_at')[:10]
    
    context = {
        'active_rooms': active_rooms,
        'reported_users': reported_users,
        'toxic_detections': toxic_detections,
        'is_shutdown': settings.is_emergency_shutdown,
        'live_sessions': live_sessions,
        'toxic_logs': toxic_logs,
    }
    return render(request, 'dashboard/admin_safety.html', context)

@staff_member_required
def toggle_emergency_shutdown(request):
    from .models import PlatformSettings
    from django.contrib import messages
    settings, _ = PlatformSettings.objects.get_or_create(id=1)
    settings.is_emergency_shutdown = not settings.is_emergency_shutdown
    settings.save()
    
    state = "ENABLED" if settings.is_emergency_shutdown else "DISABLED"
    messages.warning(request, f"Emergency Shutdown is now {state}.")
    return redirect('dashboard:admin_safety')

@staff_member_required
def admin_revenue_view(request):
    return render(request, 'dashboard/admin_revenue.html')

@staff_member_required
def admin_logs_view(request):
    from .models import ErrorLog
    from django.utils import timezone
    from datetime import timedelta
    
    today = timezone.now().date()
    
    # 1. Real Counts
    total_today = ErrorLog.objects.filter(timestamp__date=today).count()
    critical_errors = ErrorLog.objects.filter(severity='CRITICAL').count()
    ai_failures = ErrorLog.objects.filter(error_type='AI').count()
    voice_errors = ErrorLog.objects.filter(error_type='VOICE').count()
    
    # 2. Live Logs
    logs = ErrorLog.objects.all().order_by('-timestamp')[:50]
    
    context = {
        'total_today': total_today,
        'critical_errors': critical_errors,
        'ai_failures': ai_failures,
        'voice_errors': voice_errors,
        'logs': logs,
    }
    return render(request, 'dashboard/admin_logs.html', context)
