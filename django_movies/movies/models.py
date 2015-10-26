from django.db import models
from django.db.models import Avg


# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=25)
    zip = models.CharField(max_length=10)

    def __str__(self):
        return self.zip


class Rating(models.Model):
    user_id = models.ForeignKey(Rater)
    movie_id = models.ForeignKey(Movie)
    rating = models.IntegerField()

    def __str__(self):
        return str(self.rating)

