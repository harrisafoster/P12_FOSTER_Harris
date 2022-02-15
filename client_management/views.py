from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
import logging

from .serializers import ClientSerializer
from .models import Client
from .permissions import ClientPermission


logger = logging.getLogger('django')


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, ClientPermission]
