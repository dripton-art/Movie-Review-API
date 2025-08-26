from django.urls import path, include                                                          # type: ignore
from rest_framework.routers import DefaultRouter                                      # type: ignore
from .views import MovieViewSet, ReviewViewSet

router = DefaultRouter()

router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]