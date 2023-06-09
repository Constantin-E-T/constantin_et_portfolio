# Generated by Django 4.0.5 on 2023-05-18 11:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_project_technologies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Full Name', max_length=200)),
                ('title', models.CharField(help_text='Title or Position', max_length=200)),
                ('organization', models.CharField(help_text='Company/Organization Name', max_length=200)),
                ('testimonial', models.TextField(help_text='Testimonial Text')),
                ('date', models.DateField(default=django.utils.timezone.now, editable=False)),
                ('is_published', models.BooleanField(default=False, help_text='Only display this testimonial on the website if this box is checked.')),
            ],
            options={
                'verbose_name_plural': 'Testimonials',
                'ordering': ['-date'],
            },
        ),
    ]
