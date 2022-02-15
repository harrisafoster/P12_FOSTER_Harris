from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
import logging
from rest_framework import filters

from .serializers import ClientSerializer
from .models import Client
from .permissions import ClientPermission


logger = logging.getLogger('django')


class ClientViewSet(ModelViewSet):
    """
    Django default API endpoints for CRUD operations relating to the Client object.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated, ClientPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['company_name']
