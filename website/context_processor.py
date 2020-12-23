from website.apps.projects.models import Project
from website.apps.areas.models import Area
from website.apps.news.models import Post


def get_projects_to_context(request):
    projects = Project.objects.all()
    areas_of_work = Area.objects.all()
    posts = Post.objects.all()
    return {'projects': projects, 'areas': areas_of_work, 'news': posts, 'titles': get_header_titles(request)}


def get_header_titles(request):
    titles = {
        'en': {
            "home": "Home", "areas": "Areas of work", "projects": "Projects", "about": "About", "contacts": "Contact",
            "news_latest": "Our Latest News", "projects_latest": "Our Latest Projects"
        },
        'ua': {
            "home": "Головна", "areas": "Напрямки роботи", "projects": "Проєкти", "about": "Про нас",
            "contacts": "Контакти", "news_latest": "Наші останні новини", "projects_latest": "Наші останні проєкти"
        },
    }
    try:
        return titles[request.session['language']]
    except KeyError:
        return titles['en']
