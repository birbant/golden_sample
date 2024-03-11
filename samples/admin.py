from django.contrib import admin
from .models import Samples


class SamplesAdmin(admin.ModelAdmin):
    list_filter = ['status', 'client']
    list_display = ['part_number', 'part_name', 'status', 'client']


admin.site.register(Samples, SamplesAdmin)
admin.site.site_header = 'Golden Sample administration'
admin.site.index_title = 'Golden Sample'
