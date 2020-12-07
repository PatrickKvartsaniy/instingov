from django.urls import path

from . import views

urlpatterns = [
    path('<str:area_title>', views.area)
]