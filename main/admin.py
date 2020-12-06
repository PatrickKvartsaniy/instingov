from django.contrib import admin

from .models import SiteContent, Subscriber

admin.site.register(SiteContent)
admin.site.register(Subscriber)

admin.site.site_header = "Instingov Admin"
admin.site.site_title = "Institute of Innovatibe Governance"
admin.site.index_title = "Institute of Innovatibe Governanc"