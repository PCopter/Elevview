# Generated by Django 5.1.4 on 2025-01-09 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cameras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
