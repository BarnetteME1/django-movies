from django.contrib import admin

# Register your models here.
from movies.models import Movie, Person, Rating

admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(Rating)