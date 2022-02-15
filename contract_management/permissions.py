from rest_framework import permissions


class ContractPermission(permissions.BasePermission):
    """
    Custom permission for Contract object:

    Only management users can delete contracts via the admin interface
    Support team users can read contracts
    Sales team users can read/create/update contracts
    """
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return False
        user = request.user
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
