from django.urls import path
from . import views

app_name = 'pronunciation'

urlpatterns = [
    path('', views.pronunciation_index, name='index'),
    path('analyze/', views.analyze_audio, name='analyze'),
]
