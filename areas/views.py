from django.shortcuts import render

from .models import Area

def area(request, area_title):
    area = Area.objects.get(title=area_title)
    return render(request, 'areas/area.html', {'area':area})