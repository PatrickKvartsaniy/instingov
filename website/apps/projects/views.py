from django.http import Http404
from django.shortcuts import render

from .models import Project

def project(request, project_url):
    project_title = project_url.replace('-',' ')
    project = Project.objects.get(title=project_title)
    if project.title == project_url and ' ' in project_url:
        raise Http404
    return render(request, 'projects/project.html', {'project':project})