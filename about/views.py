from django.shortcuts import render

def about(request):
    return render(request, "about/about.html")

def contact(request):
    return render(request, "about/contact.html")

def team(request):
    return render(request, "about/team.html")