from django.db import models

from website.apps.areas.models import Area
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='uploaded/posts',blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def title_to_url(self):
        return self.title.replace(' ','-')