from django.urls import path

from .views import article

urlpatterns = [
    path('<str:article_url>', article)
]