from rest_framework import permissions


class EventPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method == 'DELETE':
            return False
        if user.groups.filter(name='sales').exists():
            return True
        if user.groups.filter(name='management').exists():
            return request.method in permissions.SAFE_METHODS
        if user.groups.filter(name='support').exists():
            return request.method in ['GET', 'PUT']
        else:
            return False

    def has_object_permission(self, request, view, obj):
        """
        Sales team member must set event to True and assign a support contact
        in order for the support contact to gain access.
        """
        user = request.user
        if user.groups.filter(name="sales").exists():
            return request.method in ['GET', 'PUT']
        if user.groups.filter(name='management').exists():
            return request.method in permissions.SAFE_METHODS
        if user.groups.filter(name='support').exists():
            if user == obj.support_contact and obj.event_status is True:
                return request.method in ['GET', 'PUT']
        else:
            return False
