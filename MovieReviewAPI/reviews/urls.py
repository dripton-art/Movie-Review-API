from django.urls import path, include                                                          # type: ignore
from rest_framework.routers import DefaultRouter                                      # type: ignore
from .views import MovieViewSet, ReviewViewSet

router = DefaultRouter()

router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]