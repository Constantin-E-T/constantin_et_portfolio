from django.contrib import admin

# Register your models here.
from .models import Project, Technology, Testimonial, Footer, Skill, About, FAQ

class TechnologyInline(admin.TabularInline):
    model = Project.technologies.through
    extra = 1  # how many rows to show

class ProjectAdmin(admin.ModelAdmin):
    inlines = (TechnologyInline,)
    list_display = ('title', 'description')  # fields to display in admin list
    exclude = ('technologies',)

admin.site.register(Project)
admin.site.register(Technology)
admin.site.register(Testimonial)
admin.site.register(Footer)
admin.site.register(Skill)

class FAQInline(admin.TabularInline):
    model = FAQ

class AboutAdmin(admin.ModelAdmin):
    inlines = [FAQInline]

admin.site.register(About, AboutAdmin)