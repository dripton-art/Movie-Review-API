from django.urls import path
from .views import UserList, UserDetail, SignUp, MyProfile #ProfileDetail



urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('signup/', SignUp.as_view(), name='signup'),
    path("profile/", MyProfile.as_view(), name="my-profile"),
    #path("profile/<int:pk>/", ProfileDetail.as_view(), name="profile-detail"),
]