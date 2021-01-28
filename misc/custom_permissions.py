from rest_framework.permissions import BasePermission



class IsOwner(BasePermission):
    """
    Allows access owner to update your profile.
    """
    def has_object_permission(self, request, view, obj):
        pass

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)