from django.db import models
from core.models import AbstractModel

# Create your models here.

class Message(AbstractModel):
    name = models.CharField(
        default = '',
        max_length=255,
        blank = True,
        null = True,
        verbose_name = 'Name',
        help_text = ''
    )
    
    email = models.EmailField(
        default = '',
        max_length=255,
        blank = True,
        null = True,
        verbose_name = 'Email',
        help_text = ''
    )
    
    subject = models.CharField(
        default = '',
        max_length=255,
        blank = True,
        verbose_name = 'Subject',
        help_text = ''
    )
    
    message = models.TextField(
        default = '',
        blank = True,
        verbose_name = 'Message',
    )
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
    
    
