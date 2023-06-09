# Generated by Django 4.0.5 on 2023-05-18 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_skill_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='faqs',
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('answer', models.TextField()),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faqs', to='portfolio.about')),
            ],
        ),
    ]
