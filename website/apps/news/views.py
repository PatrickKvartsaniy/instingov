from django.http import Http404
from django.shortcuts import render, HttpResponse

from .models import Post

def article(request, article_url):
    article_title = article_url.replace('-',' ')
    post = Post.objects.get(title=article_title)
    if post.title == article_url and ' ' in article_url:
        raise Http404
    return render(request, 'news/article.html', {'article':post})