from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SellingServiceViewSet,
    ManagementServiceViewSet,
    InvestmentServiceViewSet,
)

router = DefaultRouter()
router.register(r'selling-services', SellingServiceViewSet)
router.register(r'management-services', ManagementServiceViewSet)
router.register(r'investment-services', InvestmentServiceViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
