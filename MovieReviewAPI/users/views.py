from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import UserSerializer


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for all users.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed if the user is the owner or an admin.
        return obj == request.user or request.user.is_superuser

class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrAdmin]
