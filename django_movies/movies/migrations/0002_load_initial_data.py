# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pandas as pd


def movie_csv(*args):
    id_info = pd.read_csv('~/iron_yard_hw/django-movies/django_movies/ml-100k/u.data', sep='\t', names=['user_id', 'item_id', 'rating', 'timestamp'])
    movie_info = pd.read_csv('~/iron_yard_hw/django-movies/django_movies/ml-100k/u.item', sep='|', encoding='windows-1252', names=["movie_id", "movie_title", "release_date", "video_release_date", "IMDb_URL", "unknown", "Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"])
    movie_info = movie_info[["movie_id", "movie_title", "release_date"]]
    Movie = movie_info[movie_info['movie_title'] != 'unknown']
    genre = pd.read_csv('~/iron_yard_hw/django-movies/django_movies/ml-100k/u.genre', sep='|', names=['genre', 'genre_id'])
    user_info = pd.read_csv('~/iron_yard_hw/django-movies/django_movies/ml-100k/u.user', sep='|', names=['user_id', 'age', 'gender', 'occupation', 'zip_code'])


class Migration(migrations.Migration):



    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(movie_csv)
    ]
