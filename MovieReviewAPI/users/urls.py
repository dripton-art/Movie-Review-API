from django.urls import path
from .views import UserList, UserDetail, SignUp



urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('signup/', SignUp.as_view(), name='signup'),
]