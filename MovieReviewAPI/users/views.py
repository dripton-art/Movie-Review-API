from .models import CustomUser
from rest_framework import generics, permissions, status
from .serializers import UserSerializer, SignUpSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for all users.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed if the user is the owner or an admin.
        return obj == request.user or request.user.is_superuser

class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

class SignUp(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "message": "User registration successful 🎉",
                "user": serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )

