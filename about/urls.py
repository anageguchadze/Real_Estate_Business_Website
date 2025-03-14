from rest_framework.routers import DefaultRouter
from .views import AchievementViewSet, StepViewSet, StaffViewSet, ClientsViewSet

router = DefaultRouter()

router.register(r'achievements', AchievementViewSet)
router.register(r'steps', StepViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'clients', ClientsViewSet)

urlpatterns = router.urls