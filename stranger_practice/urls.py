from django.urls import path
from . import views

app_name = 'stranger_practice'

urlpatterns = [
    path('dashboard/', views.stranger_dashboard, name='dashboard'),
]
