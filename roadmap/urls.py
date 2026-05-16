from django.urls import path
from . import views

app_name = 'roadmap'

urlpatterns = [
    path('', views.index, name='index'),
    path('concept/<slug:slug>/', views.concept_detail, name='concept_detail'),
    path('analyze-speaking/', views.analyze_speaking, name='analyze_speaking'),
    path('analyze-writing/', views.analyze_writing, name='analyze_writing'),
    path('get-exercises/', views.get_exercises, name='get_exercises'),
]
