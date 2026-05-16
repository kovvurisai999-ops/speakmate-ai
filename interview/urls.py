from django.urls import path
from . import views

app_name = 'interview'

urlpatterns = [
    path('', views.interview_list, name='list'),
    path('start/', views.start_interview, name='start'),
    path('session/<int:pk>/', views.interview_session, name='session'),
    path('session/<int:pk>/evaluate/', views.evaluate_answer, name='evaluate_answer'),
    path('session/<int:pk>/report/', views.download_report, name='download_report'),
    path('detail/<int:pk>/', views.interview_detail, name='detail'),
    path('session/<int:pk>/delete/', views.delete_interview, name='delete'),
    path('download-guide/', views.download_guide, name='download_guide'),
]
