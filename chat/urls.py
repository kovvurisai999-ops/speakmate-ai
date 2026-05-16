from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_index, name='index'),
    path('send/', views.send_message, name='send'),
]
