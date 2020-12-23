from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    phone = PhoneNumberField(null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    facebook = models.CharField(max_length=50, null=True, blank=True)
    linkedin = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='uploaded/users', blank=True, null=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Team'
