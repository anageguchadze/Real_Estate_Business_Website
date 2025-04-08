from django.contrib import admin
from .models import SellingService, ManagementService, InvestmentService

admin.site.register(SellingService)
admin.site.register(ManagementService)
admin.site.register(InvestmentService)