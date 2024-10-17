from django.contrib import admin
from django.urls import path, include
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
    path('memory_log/', include('memory_log.urls')),
    path('funeral/', views.funeral),
    path('lawyer/', views.lawyer),
    path('users/', include('users.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)