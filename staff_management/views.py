from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import User, Team
from .serializers import UserSerializer, TeamSerializer
from .permissions import AccountPermission


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, AccountPermission]


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated, AccountPermission]
