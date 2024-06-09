# Generated by Django 5.0.6 on 2024-06-09 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiaryApp', '0005_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='Default.jpg', null=True, upload_to=''),
        ),
    ]
