from django.contrib import admin
from core.models import *

@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updatedDate', 'createdDate']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']
    
    class Meta:
        model = GeneralSetting
        

@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'file', 'updatedDate', 'createdDate']
    search_fields = ['name', 'description', 'file']
    list_editable = ['description', 'file']
    
    class Meta:
        model = ImageSetting