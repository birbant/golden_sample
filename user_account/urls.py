from django.urls import path
from . import views

urlpatterns = [

    path('register', views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('is-logged', views.is_logged, name="is-logged"),
    path('statistics', views.view_statistics, name="statistics")

]
