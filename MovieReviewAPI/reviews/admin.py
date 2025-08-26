from django.contrib import admin
from .models import Movie, Review

# Register your models here.

# Define the custom Admin class for the Review model
class ReviewAdmin(admin.ModelAdmin):
    filterset_fields = ('rating')
    ordering_fields = ('created_at', 'rating')
    search_fields = ('movie__title', 'review_content')

# Register the Movie and Review models with their respective admin classes
admin.site.register(Movie) 
admin.site.register(Review, ReviewAdmin)