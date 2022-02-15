from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
import logging

from .serializers import ContractSerializer
from .models import Contract
from .permissions import ContractPermission


logger = logging.getLogger('django')


class ContractViewSet(ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated, ContractPermission]
