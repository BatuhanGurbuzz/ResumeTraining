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
        
@admin.register(Skill)
class SkillSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'percentage', 'updatedDate', 'createdDate']
    search_fields = ['name']
    list_editable = ['order', 'name', 'percentage']
    
    class Meta:
        model = Skill
        
@admin.register(SocialMedia)
class SocialMediaSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'link', 'icon', 'updatedDate', 'createdDate']
    search_fields = ['link', 'icon']
    list_editable = ['order', 'link', 'icon']
    
    class Meta:
        model = SocialMedia