from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('feedback/', views.submit_feedback, name='user_feedback'),
    path('', views.dashboard_index, name='index'),
    path('analytics/', views.analytics_view, name='analytics'),
    path('settings/', views.settings_view, name='settings'),
    path('admin-panel/', views.admin_dashboard_view, name='admin_panel'),
    path('admin-panel/users/', views.admin_users_view, name='admin_users'),
    path('admin-panel/users/<int:user_id>/', views.admin_user_detail_view, name='admin_user_detail'),
    path('admin-panel/users/<int:user_id>/action/', views.admin_user_action, name='admin_user_action'),
    path('admin-panel/content/', views.admin_content_view, name='admin_content'),
    path('admin-panel/content/level/<int:level_id>/', views.admin_level_detail, name='admin_level_detail'),
    path('admin-panel/content/concept/<int:concept_id>/edit/', views.admin_concept_edit_view, name='admin_concept_edit'),
    path('admin-panel/content/concept/<int:concept_id>/delete/', views.admin_concept_delete, name='admin_concept_delete'),
    path('admin-panel/content/builder/', views.admin_lesson_builder, name='admin_lesson_builder'),
    path('admin-panel/safety/', views.admin_safety_view, name='admin_safety'),
    path('admin-panel/revenue/', views.admin_revenue_view, name='admin_revenue'),
    path('admin-panel/logs/', views.admin_logs_view, name='admin_logs'),
    path('admin-panel/safety/shutdown/', views.toggle_emergency_shutdown, name='emergency_shutdown'),
    path('test-url/', views.dashboard_index, name='test_url'),
]
