from django.urls import path

from .views import project

urlpatterns = [
    path('<str:project_url>', project)
]