from django.shortcuts import render, redirect

from website.apps.news.models import Post

from .models import Subscriber


def index(request):
    return render(request, 'main/index.html')


def translate_ua(request):
    request.session['language'] = 'ua'
    return redirect('index')


def translate_en(request):
    request.session['language'] = 'en'
    return redirect('index')


def subscribe(request):
    if request.method == 'POST':
        Subscriber(email=request.POST['email'],
                   name=request.POST['name']).save()
        return render(request, 'main/index.html')
    return render(request, 'main/index.html')
