from django.urls import path
from . import views

app_name = 'stranger_practice'

urlpatterns = [
    path('dashboard/', views.stranger_dashboard, name='dashboard'),
    path('analyze/', views.analyze_speech, name='analyze_speech'),
    path('topic/', views.get_topic, name='get_topic'),
]
