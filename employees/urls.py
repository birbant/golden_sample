from django.urls import path
from . import views
from samples.views import homepage


urlpatterns = [
    path('', homepage, name='homepage'),
    path('employees/', views.employees, name='employees'),
    path('employee/add/', views.employee_add, name='employee-add'),
    path('employee/update/<str:employee_id>', views.employee_update, name="employee-update"),
    path('employee/delete/<str:employee_id>', views.employee_delete, name="employee-delete"),
]
