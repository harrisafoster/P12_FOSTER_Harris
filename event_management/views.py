from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .serializers import EventSerializer
from .models import Event
from .permissions import EventPermission


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, EventPermission]
