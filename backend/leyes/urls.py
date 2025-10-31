from rest_framework.routers import DefaultRouter
from .views import LeyViewSet

router = DefaultRouter()
router.register(r'leyes', LeyViewSet, basename='ley')

urlpatterns = router.urls