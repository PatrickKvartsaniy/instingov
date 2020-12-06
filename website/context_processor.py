from projects.models import Project
from areas.models import Area
from contact.models import Contact
from landing.models import SiteContent

def get_projects_to_context(request):
    projects = Project.objects.all()
    areas_of_work = Area.objects.all()
    contacts = Contact.objects.all()
    content  = SiteContent.objects.all()
    return {'projects':projects, 'areas':areas_of_work, 'contacts':contacts, 'content':content}
