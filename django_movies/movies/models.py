from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100, blank=True)
    release_date = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=25)
    zip = models.CharField(max_length=10)

    def __str__(self):
        return self.zip


class IdInfo(models.Model):
    user_id = models.ForeignKey(UserInfo)
    movie_id = models.ForeignKey(Movie)
    rating = models.IntegerField()

    def __str__(self):
        return str(self.rating)
