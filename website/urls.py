from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('website.apps.main.urls')),
    path('projects/', include('website.apps.projects.urls')),
    path('areas/', include('website.apps.areas.urls')),
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('about/', include('website.apps.about.urls')),
    path('contact/', include('website.apps.contact.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)