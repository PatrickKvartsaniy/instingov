from django.http import Http404
from django.shortcuts import render

from .models import Area

def area(request, area_url):
    area_title = area_url.replace('-', ' ')
    area = Area.objects.get(title=area_title)
    if area.title == area_url and ' ' in area_url:
        raise Http404
    return render(request, 'areas/area.html', {'area':area})