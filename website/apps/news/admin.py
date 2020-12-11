from django import forms
from django.contrib import admin

from .models import Post

class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post
        fields = '__all__'

@admin.register(Post)
class Post_Admin(admin.ModelAdmin):
    form = PostAdminForm
