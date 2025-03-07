from rest_framework.routers import DefaultRouter
from .views import PropertyTypeViewSet, PropertyViewSet, PropertyImageViewSet, InquiryViewSet

router = DefaultRouter()
router.register('property-type', PropertyTypeViewSet)
router.register('property', PropertyViewSet)
router.register('property-image', PropertyImageViewSet)
router.register('inquiry', InquiryViewSet)

urlpatterns = router.urls