from django.urls import path

from rest_framework.routers import DefaultRouter

from cride.circles.views import circles as circle_views
from cride.circles.views import memberships as membership_views

router = DefaultRouter()
router.register(r'circles', circle_views.CircleViewSet, basename='circle')
router.register(
    r'circles/(?P<slug_name>[-a-zA-Z0-9_]+)/members',
    membership_views.MembershipViewSet,
    basename='membership'
)
urlpatterns = router.urls