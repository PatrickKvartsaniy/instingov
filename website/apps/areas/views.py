from django.http import Http404
from django.shortcuts import render

from .models import Area


def area(request, area_url):
    area_title = area_url.replace('-', ' ')
    areas = Area.objects.get(title=area_title)
    if areas.title == area_url and ' ' in area_url:
        raise Http404
    return render(request, 'areas/area.html', {'area': areas})
