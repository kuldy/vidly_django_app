from django.db import models
from django.utils import timezone


# Create your models here.


class GenreFilm(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rental_rate = models.FloatField()
    is_liked = models.BooleanField(default=False)
    genre_id = models.ForeignKey(GenreFilm, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
