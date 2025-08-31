from django_filters.rest_framework import DjangoFilterBackend                                   
from .serializers import MovieSerializer, ReviewSerializer
from rest_framework import viewsets, filters                              
from rest_framework.pagination import PageNumberPagination
from .models import Movie, Review
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from users.models import Profile
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "home.html")

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save()

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = PageNumberPagination

    # Add search, filter, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['movie_title', 'review_content']  # search by movie title or content
    filterset_fields = ['rating']  # filter by rating
    ordering_fields = ['created_at', 'rating']  # sort by created date or rating
    ordering = ['-created_at']  # default: newest first

    def get_queryset(self):
        queryset = Review.objects.all()  # start with all reviews
        movie_title = self.request.query_params.get('movie')  # read ?movie=... from the URL

        if movie_title:  # if a movie title is provided in the query string
            queryset = queryset.filter(movie__title__icontains=movie_title)  
            # keep only reviews where the related movie title contains that text (case-insensitive)
        return queryset  # return the filtered or full list

    def perform_create(self, serializer):
        # Get the profile instance of the currently authenticated user
        profile = Profile.objects.get(user=self.request.user)
        # Save the new review instance, linking it to the user's profile
        serializer.save(user=self.request.user, profile=profile)
        


