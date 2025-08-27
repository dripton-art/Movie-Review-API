from django.db import models                                                           # type: ignore
from django.contrib.auth import get_user_model                                         # type: ignore

User = get_user_model()


# Create your models here.

class Movie(models.Model):
    movie_title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    release_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.movie_title

class Review(models.Model):
    movie_title = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews",)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    review_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie_title.title} ({self.rating}/5) by {self.user.username}"

