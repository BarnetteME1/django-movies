from django.contrib import admin

# Register your models here.
from movies.models import Movie, IdInfo, Genre

admin.site.register(Movie)
admin.site.register(IdInfo)
admin.site.register(Genre)