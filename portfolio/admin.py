from django.contrib import admin

# Register your models here.
from .models import Project, Technology

class TechnologyInline(admin.TabularInline):
    model = Project.technologies.through
    extra = 1  # how many rows to show

class ProjectAdmin(admin.ModelAdmin):
    inlines = (TechnologyInline,)
    list_display = ('title', 'description')  # fields to display in admin list
    exclude = ('technologies',)

admin.site.register(Project)
admin.site.register(Technology)