from django.contrib import admin
from .models import Employees


class EmployeesAdmin(admin.ModelAdmin):
    list_filter = ['department']
    list_display = ['first_name', 'last_name', 'department']


admin.site.register(Employees, EmployeesAdmin)
