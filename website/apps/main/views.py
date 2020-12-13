from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from website.apps.news.models import Post

from .models import Subscriber


def index(request):
    return render(request, 'main/index.html')

def subscribe(request):
    if request.method == 'POST':
        Subscriber(email=request.POST['email'], name=request.POST['name']).save()
        return render(request, 'main/index.html')

    return render(request, 'main/index.html')