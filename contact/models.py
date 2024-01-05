from django.conf import settings
from django.db import models
from core.models import AbstractModel
from django.core.mail import EmailMessage
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
    
    def send_mail(self):
        if self.is_valid():
            name = self.cleaned_data['name']
           
            email = self.cleaned_data['email'] 
           
            subject = self.cleaned_data['subject']
           
            message = self.cleaned_data['message']
           
            message_context = 'Message received. \n\n \
                Name: %s \n\n \
                Email: %s \n\n \
                Subject: %s \n\n \
                Message: %s' % (name, email, subject, message)
            
            email = EmailMessage(
                subject,
                message_context,
                to=[settings.DEFAULT_FROM_EMAIL],
                reply_to= [email]
            )
            
            email.send()
    
    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
    
    
