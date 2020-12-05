from projects.models import Project
from areas.models import Area

def get_projects_to_context(request):
    projects = Project.objects.all()
    areas_of_work = Area.objects.all()
    return {'projects':projects, 'areas':areas_of_work}
