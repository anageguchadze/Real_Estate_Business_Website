from rest_framework.routers import DefaultRouter
from .views import PropertyTypeViewSet, PropertyViewSet, PropertyImageViewSet, InquiryViewSet

router = DefaultRouter()
router.register(r'property-type', PropertyTypeViewSet)
router.register(r'property', PropertyViewSet)
router.register(r'property-image', PropertyImageViewSet)
router.register(r'inquiry', InquiryViewSet)

urlpatterns = router.urls