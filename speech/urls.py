from django.urls import path
from . import views

app_name = 'speech'

urlpatterns = [
    path('transcribe/', views.transcribe_audio, name='transcribe'),
]
