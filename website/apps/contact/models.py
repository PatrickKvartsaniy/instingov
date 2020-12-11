from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    adress = models.CharField(max_length=50, null=True)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254)
    contact_person = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.adress