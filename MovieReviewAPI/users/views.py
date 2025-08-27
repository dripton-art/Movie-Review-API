from .models import CustomUser
from rest_framework.views import APIView                                                    # type: ignore
from rest_framework.response import Response                                                # type: ignore
from rest_framework import generics, permissions                                            # type: ignore
from rest_framework.authtoken.models import Token                                           # type: ignore
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer



# Registration View
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = CustomUser.objects.get(username=response.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({'user': UserSerializer(user).data, 'token': token.key})
    
# Login View
class LoginView(APIView):
    serializer_class = LoginSerializer


    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({'user': UserSerializer(user).data, 'token': token.key})
    
# Profile Management View
class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
