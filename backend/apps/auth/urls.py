from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.auth.views import ActivateUserView, RecoveryRequestView, RecoveryPasswordView

urlpatterns = [

    path('', TokenObtainPairView.as_view(), name='auth-login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth-refresh'),
    path('/activate/<str:token>', ActivateUserView.as_view(), name='auth-activate'),
    path('/recovery', RecoveryRequestView.as_view(), name='auth-recovery'),
    path('/recovery/<str:token>', RecoveryPasswordView.as_view(), name='auth-recovery-password'),
]