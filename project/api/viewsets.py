from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from ..models import Professional
from .permissions import IsAuthenticated, IsOwnerOrAdmin
from .serializers import ProfessionalSerializer


class ProfessionalViewSet(ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
    # permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    # authentication_classes = [JWTAuthentication]
