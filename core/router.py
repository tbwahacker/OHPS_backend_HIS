from registration.viewsets import RegistrationViewSet
from rest_framework import routers
from custom_auth.views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register('client',RegistrationViewSet)


# urlpatterns = [
#     path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]
# urlpatterns=router.urls
# urlpatterns += router.urls  #combine both vies and viewset in a single url pattern


