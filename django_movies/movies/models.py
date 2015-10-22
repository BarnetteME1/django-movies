from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=30)


class Rating(models.Model):
    rating = models.IntegerField()
    owner = models.ForeignKey(Person)


class Movie(models.Model):
    movie_id = models.in
    title = models.CharField(max_length=100)
    rating = models.ManyToManyField(Rating)

movie_id, "movie_title", "release_date"