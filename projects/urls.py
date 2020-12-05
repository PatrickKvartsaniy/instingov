from django.urls import path

from . import views

urlpatterns = [
    path('<str:project_title>', views.project)
]