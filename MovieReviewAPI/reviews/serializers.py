from rest_framework import serializers                                                # type: ignore
from .models import Movie, Review
from users.models import Profile, CustomUser




class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Movie title cannot be empty.")
        return value

class ReviewSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'movie_title', 'rating', 'review_content', 'created_at', 'profile']
        read_only_fields = ['created_at']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError('Rating must be between 1 and 5')
        return value
    
    def validate_review_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Review content cannot be empty.")
        return value

    def validate(self, data):
        user = self.context['request'].user
        movie = data.get("movie_title")
        if Review.objects.filter(user=user, movie_title=movie).exists():
            raise serializers.ValidationError("You cannot review the same movie again! please review another one instead.")
        return data
