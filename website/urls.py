from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('landing.urls')),
    path('research/', include('research.urls')),
    path('news/', include('news.urls')),
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
]