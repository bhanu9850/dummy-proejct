from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
    return render(request,"home.html")

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})