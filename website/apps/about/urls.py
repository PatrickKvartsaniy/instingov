from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='about'),
    path('team', views.team, name='team'),
]