from rest_framework.routers import DefaultRouter  

from cride.users.views import UserViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet, 'users')
urlpatterns = router.urls