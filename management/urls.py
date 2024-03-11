from django.urls import path
from . import views


urlpatterns = [
    path('management/', views.sample_management, name='management'),
    path('operations/', views.sample_manage_add, name='operations'),
]