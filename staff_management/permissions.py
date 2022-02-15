from rest_framework import permissions


class AccountPermission(permissions.BasePermission):
    """
    Sales, management, and support team members can read via endpoints
    Management team members can create/update/delete users via the admin interface
    """
    def has_permission(self, request, view):
        user = request.user
        if user.groups.filter(name__in=['sales', 'support', 'management']):
            return request.method in permissions.SAFE_METHODS
        else:
            return False
