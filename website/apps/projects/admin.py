from django import forms
from django.contrib import admin

from .models import Project
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ProjectAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    description_ua = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Project
        fields = '__all__'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

