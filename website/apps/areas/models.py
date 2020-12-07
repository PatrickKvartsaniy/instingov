from django.db import models

class Area(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='uploaded/areas',blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title