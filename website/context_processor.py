from projects.views import Project

def get_projects_to_context(request):
    projects = Project.objects.all()
    return {'projects':projects}
