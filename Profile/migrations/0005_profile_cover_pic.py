# Generated by Django 2.0.6 on 2018-07-08 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0004_remove_profile_cover_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover_pic',
            field=models.ImageField(blank=True, upload_to='cover_images'),
        ),
    ]
