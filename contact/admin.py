from django.contrib import admin
from contact.models import Message
# Register your models here.
@admin.register(Message)
class DocumentSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'message', 'updatedDate', 'createdDate']
    
    search_fields = ['name', 'email', 'subject', 'message']
    
    readonly_fields = ['name', 'email', 'subject', 'message']
    class Meta:
        model = Message