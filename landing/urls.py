from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('subscribe/', views.subscribe, name='subscribe')
]