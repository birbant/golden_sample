from django.urls import path
from . import views
from samples.views import homepage


urlpatterns = [
    path('', homepage, name='homepage'),
    path('samples/', views.samples, name='samples'),
    path('sample/add', views.sample_add, name='sample-add'),
    path('sample/update/<str:part_number>', views.sample_update, name="sample-update"),
    path('sample/delete/<str:part_number>', views.sample_delete, name="sample-delete"),


]