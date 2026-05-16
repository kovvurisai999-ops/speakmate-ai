from django.urls import path
from . import views

app_name = 'webcam'

urlpatterns = [
    path('', views.mirror_mode, name='index'),
    path('mirror/', views.mirror_mode, name='mirror'),
]
