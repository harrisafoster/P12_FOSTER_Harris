from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
import logging
from rest_framework import filters

from .serializers import EventSerializer
from .models import Event
from .permissions import EventPermission


logger = logging.getLogger('django')


class EventViewSet(ModelViewSet):
    """
    Django default API endpoints for CRUD operations relating to the Event object.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, EventPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['event_status']
