from django.db import models
from django.utils import timezone


# Create your models here.
class movie(models.Model):
    category = models.CharField(max_length=250)
    Movie_Name = models.CharField(max_length=250)
    Poster = models.ImageField(upload_to='image')
    Description = models.TextField()
    Release_date = models.DateField()
    Actors = models.TextField()
    Trailer = models.CharField(max_length=250)

    def __str__(self):
        return self.category


class Review(models.Model):
    author = models.CharField(max_length=50, default="anonymous")
    review_date = models.DateTimeField(default=timezone.now)
    rate_choice = (
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)
    )
    stars = models.IntegerField(choices=rate_choice)
    comment = models.TextField(max_length=5000)
    Movie = models.ForeignKey(movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.Movie.category

