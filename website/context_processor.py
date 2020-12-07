from website.apps.projects.models import Project
from website.apps.areas.models import Area
from website.apps.contact.models import Contact
from website.apps.main.models import SiteContent
from website.apps.news.models import Post

def get_projects_to_context(request):
    projects = Project.objects.all()
    areas_of_work = Area.objects.all()
    contacts = Contact.objects.all()
    content  = SiteContent.objects.all()
    posts = Post.objects.all()
    return {'projects':projects, 'areas':areas_of_work, 'contacts':contacts, 'content':content, 'news':posts}
