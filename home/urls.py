from rest_framework.routers import DefaultRouter
from .views import TestimonalViewSet, FAQViewSet

router = DefaultRouter()

router.register(r'testimonal', TestimonalViewSet)
router.register(r'faq', FAQViewSet)

urlpatterns = router.urls