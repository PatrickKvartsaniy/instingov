from django.db import models

from website.apps.areas.models import Area


def validate_title(title):
    if "-" in title:
        raise ValidationError('Title should not contain "-" symbol', params={'title': title})


class Project(models.Model):
    title = models.CharField(max_length=100, validators=[validate_title])
    title_ua = models.CharField(max_length=100, validators=[validate_title], verbose_name='Title in ukrainian')
    description = models.TextField()
    description_ua = models.TextField(verbose_name='Description in ukrainian')
    image = models.ImageField(upload_to='uploaded/projects',blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def title_to_url(self):
        return self.title.replace(' ','-')