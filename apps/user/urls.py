from django.urls import path, include
# DRF
from rest_framework.routers import DefaultRouter

from .views import UserSignUpView
router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path("sign-up/", UserSignUpView.as_view()),
]