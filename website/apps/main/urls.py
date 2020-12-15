from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('translate/en', views.translate_en, name='translate_en'),
    path('translate/ua', views.translate_ua, name='translate_ua')
]