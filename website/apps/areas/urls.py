from django.urls import path

from . import views

urlpatterns = [
    path('<str:area_url>', views.area)
]