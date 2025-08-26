from django.urls import path                                                                # type: ignore
from .views import RegisterView, LoginView, ProfileView



urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]