from django.contrib import admin
from .models import InquiryType, HeardFrom, OfficeType, ContactMessage, OfficeLocation


admin.site.register(InquiryType)
admin.site.register(HeardFrom)
admin.site.register(OfficeType)
admin.site.register(ContactMessage)
admin.site.register(OfficeLocation)