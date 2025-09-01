from django.urls import path
from .views import UserList, UserDetail, SignUp, ProfileView, ProfileDetail, ProfileUpdateView



urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
]