from django import forms

from django.contrib import admin

from .models import Area

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AreaAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    description_ua = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Area
        fields = '__all__'


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    form = AreaAdminForm
