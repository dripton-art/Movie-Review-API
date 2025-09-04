from django.db import models                                                         
from django.conf import settings                                      
from users.models import Profile


# Create your models here.

class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    release_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.movie_title

class Review(models.Model):
    movie_title = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews",)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    review_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        unique_together = ('movie_title', 'user')

    def __str__(self):
        return f"{self.movie_title} ({self.rating}/5) by {self.user}"

