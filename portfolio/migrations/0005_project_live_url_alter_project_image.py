# Generated by Django 4.0.5 on 2023-05-16 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_remove_project_image_url_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='live_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='project_images/'),
        ),
    ]
