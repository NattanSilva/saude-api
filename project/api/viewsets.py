from rest_framework.views import Response, status
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from ..models import Cuidador, Professional
from .permissions import IsAuthenticated, IsOwnerOrAdmin
from .serializers import CuidadorSerializer, ProfessionalSerializer


class ProfessionalViewSet(ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    authentication_classes = [JWTAuthentication]


class CuidadorViewSet(ModelViewSet):
    queryset = Cuidador.objects.all()
    serializer_class = CuidadorSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = CuidadorSerializer(
            data={**request.data, "enfermeiro": request.user}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
