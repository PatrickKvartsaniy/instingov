from django.shortcuts import render

from .models import Subscriber

def index(request):
    return render(request, 'landing/index.html')

def subscribe(request):
    if request.method == 'POST':
        Subscriber(email=request.POST['email'], name=request.POST['name']).save()
        return render(request, 'landing/index.html')

    return render(request, 'landing/index.html')