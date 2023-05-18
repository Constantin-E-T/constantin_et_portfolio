# portfolio/models.py

from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='technology_logos/', blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    url = models.URLField(max_length=200, blank=True)  # GitHub link
    live_url = models.URLField(max_length=200, blank=True)  # Live project link
    technologies = models.ManyToManyField(Technology, blank=True)
    completion_date = models.DateField(null=True, blank=True)
    difficulty_level = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    tags = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
    
from django.db import models
from django.utils import timezone

class Testimonial(models.Model):
    name = models.CharField(max_length=200, help_text="Full Name")
    title = models.CharField(max_length=200, help_text="Title or Position")
    organization = models.CharField(max_length=200, help_text="Company/Organization Name")
    testimonial = models.TextField(help_text="Testimonial Text")
    date = models.DateField(default=timezone.now, editable=False)
    is_published = models.BooleanField(default=False, help_text="Only display this testimonial on the website if this box is checked.")

    class Meta:
        verbose_name_plural = "Testimonials"
        ordering = ['-date']

    def __str__(self):
        return f'{self.name} ({self.organization})'

    def save(self, *args, **kwargs):
        if self.is_published and not self.date:
            self.date = timezone.now()
        super().save(*args, **kwargs)


from django.db import models

class Footer(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title





