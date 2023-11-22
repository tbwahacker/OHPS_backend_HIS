from django.urls import path,include
from . import views
from .views import MyTokenObtainPairView
from rest_framework import routers
from registration.viewsets import RegistrationViewSet

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

#viewsets routes goes here
router = routers.DefaultRouter()
router.register('client',RegistrationViewSet)

#views routes goes here
urlpatterns = [
    path('',views.getRoutes),
    path('',include(router.urls)),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# urlpatterns += router.urls  #combine both vies and viewset in a single url pattern
