from rest_framework import serializers                                                # type: ignore
from .models import Movie, Review




class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Movie title cannot be empty.")
        return value

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = ['id', 'movie_title', 'user', 'rating', 'review_content', 'created_at']
        read_only_fields = ['user', 'created_at']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError('Rating must be between 1 and 5')
        return value
    
    def validate_review_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Review content cannot be empty.")
        return value

