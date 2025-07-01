from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, 'website/home.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'website/projects.html', {'projects': projects})
