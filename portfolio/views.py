from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView  # add this import


from .models import Project

# Create your views here.

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

class ProjectIndexView(ListView):
    template_name = 'portfolio/projects.html' 
    context_object_name = 'projects'

    def get_queryset(self):
        queryset = Project.objects.all()

        # Get the query parameter
        q = self.request.GET.get('q')
        if q:
            # Filter projects by technology stack
            queryset = queryset.filter(technologies__name__icontains=q)


        return queryset
