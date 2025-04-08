from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactMessageViewSet, OfficeLocationViewSet

router = DefaultRouter()
router.register(r'contact-messages', ContactMessageViewSet)
router.register(r'office-locations', OfficeLocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
