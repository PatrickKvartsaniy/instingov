from django.shortcuts import render

from .models import Project

def project(request, project_title):
    project = Project.objects.get(title=project_title)
    return render(request, 'projects/project.html', {'project':project})