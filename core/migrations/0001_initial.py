# Generated by Django 5.0 on 2024-01-04 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('description', models.CharField(blank=True, default='', max_length=255)),
                ('parameter', models.CharField(blank=True, default='', max_length=255)),
                ('updatedDate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
