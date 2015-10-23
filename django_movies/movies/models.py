from django.db import models

# Create your models here.


class IdInfo(models.Model):
    user_id = models.IntegerField()
    item_id = models.IntegerField()
    rating = models.IntegerField()


class Genre(models.Model):
    genre = models.CharField(max_length=15, blank=True)


class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100, blank=True)
    release_date = models.DateField()
