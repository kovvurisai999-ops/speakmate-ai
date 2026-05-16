from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('chat/', include('chat.urls')),
    path('speech/', include('speech.urls')),
    path('grammar/', include('grammar.urls')),
    path('interview/', include('interview.urls')),
    path('webcam/', include('webcam.urls')),
    path('pronunciation/', include('pronunciation.urls')),
    path('avatar/', include('avatar.urls')),
    path('stranger/', include('stranger_practice.urls')),
    path('roadmap/', include('roadmap.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
