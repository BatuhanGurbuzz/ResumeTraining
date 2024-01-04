from django.db import models

class GeneralSetting(models.Model):
    name = models.CharField(
        default = '',
        max_length = 255,
        blank = True,
        verbose_name = 'Name',
        help_text = 'This is variable of the setting'
    )
    
    description = models.CharField(
        default = '',
        max_length = 255,
        blank = True,
        verbose_name = 'Description',
        help_text = ''
    )
    
    parameter = models.CharField(
        default = '',
        max_length = 255,
        blank = True,
        verbose_name = 'Parameter',
        help_text = ''
    )
    
    updatedDate = models.DateField(
        blank = True,
        auto_now = True,
        verbose_name = 'Updated Date',
        help_text = ''
    )
    
    createdDate = models.DateField(
        blank = True,
        auto_now_add = True,
        null = True,
        verbose_name = 'Created Date',
        help_text = ''
    )
    
    def __str__(self):
        return f"General Setting: {self.name}"
    
    class Meta:
        verbose_name = 'General Setting'
        
        verbose_name_plural = 'General Settings'
        
        ordering = ('name',)
        

class ImageSetting(models.Model):
         
    name = models.CharField(
        default = '',
        max_length = 255,
        blank = True,
        verbose_name = 'Name',
        help_text = 'This is variable of the setting'
    )
    
    description = models.CharField(
        default = '',
        max_length = 255,
        blank = True,
        verbose_name = 'Description',
        help_text = ''
    )
    
    file = models.ImageField(
        default = '',
        verbose_name= 'Image',
        help_text= '',
        blank=True,
        upload_to= 'images/'
    )
    
    updatedDate = models.DateField(
        blank = True,
        auto_now = True,
        verbose_name = 'Updated Date',
        help_text = ''
    )
    
    createdDate = models.DateField(
        blank = True,
        auto_now_add = True,
        null = True,
        verbose_name = 'Created Date',
        help_text = ''
    )
    
    def __str__(self):
        return f"Image Setting: {self.name}"
    
    class Meta:
        verbose_name = 'Image Setting'
        
        verbose_name_plural = 'Image Settings'
        
        ordering = ('name',)