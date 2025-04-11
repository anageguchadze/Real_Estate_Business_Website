from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactMessageViewSet, OfficeLocationViewSet, InquiryTypeViewSet, HeardFromViewSet, OfficeTypeViewSet


router = DefaultRouter()
router.register(r'contact-messages', ContactMessageViewSet)
router.register(r'office-locations', OfficeLocationViewSet)
router.register(r'inquiry-types', InquiryTypeViewSet)
router.register(r'heard-from', HeardFromViewSet)
router.register(r'office-types', OfficeTypeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
