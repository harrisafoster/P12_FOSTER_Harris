from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
import logging

from .models import User, Team
from .serializers import UserSerializer, TeamSerializer
from .permissions import AccountPermission


logger = logging.getLogger('django')


class UserViewSet(ModelViewSet):
    """
    Django default API endpoints restricted to READ-ONLY operations related to User object.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, AccountPermission]


class TeamViewSet(ModelViewSet):
    """
    Django default API endpoints restricted to READ-ONLY operations related to Team(group) object.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated, AccountPermission]
