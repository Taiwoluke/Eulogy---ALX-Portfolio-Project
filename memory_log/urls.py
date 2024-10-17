from django.urls import path
from . import views 

app_name = 'memorials'

urlpatterns = [
    path('', views.memory_log, name="memories"),
    path('log_memory/', views.log_memory, name="log_memory"),
    path('<slug:slug>', views.memory_page, name="memory")
]
