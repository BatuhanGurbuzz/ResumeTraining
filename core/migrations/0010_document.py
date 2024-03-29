# Generated by Django 5.0 on 2024-01-04 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_socialmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updatedDate', models.DateField(auto_now=True, verbose_name='Updated Date')),
                ('createdDate', models.DateField(auto_now_add=True, null=True, verbose_name='Created Date')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='Title')),
                ('button_text', models.CharField(blank=True, default='', max_length=255, verbose_name='Button Text')),
                ('file', models.FileField(blank=True, default='', upload_to='documents/', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'ordering': ('order',),
            },
        ),
    ]
