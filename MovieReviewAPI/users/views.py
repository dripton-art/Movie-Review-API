from .models import CustomUser, Profile
from rest_framework import generics, permissions, status
from .serializers import UserSerializer, SignUpSerializer, ProfileSerializer, ProfileUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination



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

#class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    #queryset = CustomUser.objects.all()
    #serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

class SignUp(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [permissions.AllowAny]

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

class ProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # This view will return the profile of the currently logged-in user.
        return self.request.user.profile


   # Public profile (view-only)
class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]  # must be logged in
 
class ProfileUpdateView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # This view will get the profile of the currently logged-in user.
        return self.request.user.profile      