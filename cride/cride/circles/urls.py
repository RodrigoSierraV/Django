from django.urls import path

from rest_framework.routers import DefaultRouter

from circles.views import circles as circle_views


router = DefaultRouter()
router.register(r'circles', circle_views.CircleViewSet, basename='circle')

urlpatterns = router.urls