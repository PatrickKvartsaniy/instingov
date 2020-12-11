from django.db import models

from website.apps.areas.models import Area

class Project(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='uploaded/projects',blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def title_to_url(self):
        return self.title.replace(' ','-')