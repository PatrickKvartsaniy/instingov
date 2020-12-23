from django.contrib import admin

from .models import Subscriber

admin.site.register(Subscriber)

admin.site.site_header = "Instingov Admin"
admin.site.site_title = "Institute of Innovative Governance"
admin.site.index_title = "Institute of Innovative Governance"
