from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from .viewsets import ProfessionalViewSet

router = DefaultRouter()
router.register("professional", ProfessionalViewSet)

urlpatterns = [
    path("login/", TokenObtainPairView.as_view()),
    path("", include(router.urls)),
]
