# Generated by Django 4.0.5 on 2023-05-18 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_footer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footer',
            name='content',
        ),
    ]
