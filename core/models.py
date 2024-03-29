from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class AbstractModel(models.Model):
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
    
    class Meta:
        abstract = True

class GeneralSetting(AbstractModel):
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
    
    
    
    def __str__(self):
        return f"General Setting: {self.name}"
    
    class Meta:
        verbose_name = 'General Setting'
        
        verbose_name_plural = 'General Settings'
        
        ordering = ('name',)
        

class ImageSetting(AbstractModel):
         
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
       
    
    def __str__(self):
        return f"Image Setting: {self.name}"
    
    class Meta:
        verbose_name = 'Image Setting'
        
        verbose_name_plural = 'Image Settings'
        
        ordering = ('name',)
        
class Skill(AbstractModel):
    order = models.IntegerField(
        default = 0,
        verbose_name = 'Order',
    )
    name = models.CharField(
        default = '',
        max_length = 255,
        blank = True,
        verbose_name = 'Name',
        help_text = 'This is variable of the setting'
    )
    
    percentage = models.IntegerField(
        default = 50,
        verbose_name = 'Percentage',
        validators = [MinValueValidator(0), MaxValueValidator(100)]
    )
    
    def __str__(self):
        return f"Skill: {self.name}"
    
    class Meta:
        verbose_name = 'Skill'
        
        verbose_name_plural = 'Skills'
        
        ordering = ('order',)
        
        
class SocialMedia(AbstractModel):
    order = models.IntegerField(
        default = 0,
        verbose_name = 'Order',
    )
    
    link = models.URLField(
        default = '',
        max_length = 255,
        blank = True,
        verbose_name = 'Link',
    )
    
    icon = models.CharField(
        default = '',
        max_length = 255,
        blank = True,
        verbose_name = 'Icon',
    )
    
    def __str__(self):
        return f"Social Media: {self.link}"
    
    class Meta:
        verbose_name = 'Social Media'
        
        verbose_name_plural = 'Social Media'
        
        ordering = ('order',)
        

class Document(AbstractModel):
    order = models.IntegerField(
        default = 0,
        verbose_name = 'Order',
    )
    
    slug = models.SlugField(
        default = '',
        max_length = 255,
        blank = True,
        verbose_name = 'Slug',
    )
    
    button_text = models.CharField(
        default = '',
        max_length = 255,
        blank = True,
        verbose_name = 'Button Text',
    )
    
    file = models.FileField(
        default = '',
        verbose_name= 'File',
        help_text= '',
        blank=True,
        upload_to= 'documents/'
    )
    
    def __str__(self):
        return f"Document: {self.slug}"
    
    class Meta:
        verbose_name = 'Document'
        
        verbose_name_plural = 'Documents'
        
        ordering = ('order',)