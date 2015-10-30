from django.db import models


# Create your models here.


class TopTwenty(models.Manager):

    def top_movies(self):
        return sorted(Movie.objects.all(), key=lambda x: x.average, reverse=True)[:20]


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=50)

    objects = TopTwenty()

    def __str__(self):
        return self.title

    @property
    def average(self):
        rating = self.rating_set.all().values_list('rating', flat=True)
        return sum(rating)/rating.count()


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
