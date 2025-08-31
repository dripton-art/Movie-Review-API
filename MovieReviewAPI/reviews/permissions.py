from rest_framework import permissions                                                 # type: ignore


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return obj.user == request.username or request.user.is_superuser
        # Only allow owners of the object or admins to edit/delete it.
        