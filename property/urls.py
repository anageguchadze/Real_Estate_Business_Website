from rest_framework.routers import DefaultRouter
from .views import PropertyTypeViewSet, PropertyViewSet, PropertyImageViewSet, InquiryViewSet, FeatureViewSet, PropertyFilterOptionsView
from django.urls import path, include

router = DefaultRouter()
router.register(r'property-type', PropertyTypeViewSet)
router.register(r'property', PropertyViewSet)
router.register(r'property-image', PropertyImageViewSet)
router.register(r'inquiry', InquiryViewSet)
router.register(r'features', FeatureViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('property-filter-options/', PropertyFilterOptionsView.as_view(), name="property-filter-options"),
]