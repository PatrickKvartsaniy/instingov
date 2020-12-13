from django.contrib import admin

from .models import Contact, UserProfile

admin.site.register(Contact)
admin.site.register(UserProfile)