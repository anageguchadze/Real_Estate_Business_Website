from django.contrib import admin
from .models import Property, PropertyImage, PropertyType, Inquiry, Feature

admin.site.register(Property)
admin.site.register(PropertyImage)
admin.site.register(PropertyType)
admin.site.register(Inquiry)
admin.site.register(Feature)