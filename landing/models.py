from django.db import models

# Create your models here.

class SiteContent(models.Model):
    languages = (
        ('English', "English"),
        ('Ukrainian', "Ukrainian")
    ) 
    lang = models.CharField(max_length=10, choices=languages)
    main_photo = models.ImageField(upload_to='uploaded',blank=True, null=True)
    
    def __str__(self):
        return self.lang

class Subscriber(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email