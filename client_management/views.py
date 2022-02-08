from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .serializers import ClientSerializer
from .models import Client
from .permissions import ClientPermission


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, ClientPermission]
