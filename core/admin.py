from django.contrib import admin
from core.models import *

@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updatedDate', 'createdDate']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']
    
    class Meta:
        model = GeneralSetting
        

