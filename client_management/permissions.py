from rest_framework import permissions


class ClientPermission(permissions.BasePermission):
    """
    Custom permission for Client object:

    Only management can delete clients via the admin interface
    Support team users can only read clients
    Sales team users can read, create, update clients
    """
    def has_permission(self, request, view):
        user = request.user
        if request.method == 'DELETE':
            return False
        if user.groups.filter(name='sales').exists():
            return True
        if user.groups.filter(name__in=['support', 'management']):
            return request.method in permissions.SAFE_METHODS
        else:
            return False

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.groups.filter(name="sales").exists():
            return True
        if user.groups.filter(name__in=['support', 'management']):
            return request.method in permissions.SAFE_METHODS
        else:
            return False
