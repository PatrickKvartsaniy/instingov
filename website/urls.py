from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('landing.urls')),
    path('projects/', include('projects.urls')),
    path('areas/', include('areas.urls')),
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
]