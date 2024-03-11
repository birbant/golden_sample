from django.contrib import admin
from .models import SampleOperation


class SampleOperationAdmin(admin.ModelAdmin):
    list_filter = ['operation_type']
    list_display = ['sample_id', 'employee_id', 'operation_type', 'storage_place']


admin.site.register(SampleOperation, SampleOperationAdmin)
