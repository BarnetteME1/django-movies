from django.contrib import admin

# Register your models here.
from movies.models import Movie, Rater, Rating

admin.site.register(Movie)
admin.site.register(Rater)
admin.site.register(Rating)
