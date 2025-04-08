from django.contrib import admin
from .models import ContactMessage, OfficeLocation

admin.site.register(ContactMessage)
admin.site.register(OfficeLocation)