# Generated by Django 4.0.5 on 2023-05-21 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_alter_userprofile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(default='profile_pictures/default.jpeg', upload_to='profile_pictures'),
        ),
    ]