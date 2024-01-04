from django.db import models

class GeneralSetting(models.Model):
    name = models.CharField(
        default = '',
        max_length = 255,
        blank = True,
    )
    
    description = models.CharField(
        default = '',
        max_length = 255,
        blank = True,
    )
    
    parameter = models.CharField(
        default = '',
        max_length = 255,
        blank = True,
    )
    
    updatedDate = models.DateField(
        blank = True,
        auto_now = True
    )
    
    updatedDate = models.DateField(
        blank = True,
        auto_now_add = True
    )