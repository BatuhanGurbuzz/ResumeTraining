# Generated by Django 5.0 on 2024-01-04 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='name',
        ),
        migrations.AddField(
            model_name='document',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255, verbose_name='Slug'),
        ),
    ]
