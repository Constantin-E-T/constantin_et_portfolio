# portfolio/models.py

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    url = models.URLField(max_length=200, blank=True)  # GitHub link
    live_url = models.URLField(max_length=200, blank=True)  # Live project link

    def __str__(self):
        return self.title
