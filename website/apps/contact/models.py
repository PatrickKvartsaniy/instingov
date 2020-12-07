from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    adress = models.CharField(max_length=50, null=True)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254)
    contact_person = models.OneToOneField(User, null=True, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.adress