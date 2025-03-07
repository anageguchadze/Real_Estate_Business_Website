from rest_framework.routers import DefaultRouter
from .views import AchievementViewSet, StepViewSet

router = DefaultRouter()

router.register(r'achievements', AchievementViewSet)
router.register(r'steps', StepViewSet)

urlpatterns = router.urls