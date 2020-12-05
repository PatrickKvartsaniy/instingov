from django.shortcuts import render

def index(request):
    return render(request, "about/index.html")

def team(request):
    return render(request, "about/team.html")