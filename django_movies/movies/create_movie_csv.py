import pandas as pd


def movie_csv(*args):
    IDInfo = pd.read_csv('~/iron_yard_hw/django-movies/django_movies/ml-100k/u.data', sep='\t', names=['user_id', 'item_id', 'rating', 'timestamp'])
    Movie = pd.read_csv('~/iron_yard_hw/django-movies/django_movies/ml-100k/u.item', sep='|', encoding='windows-1252', names=["movie_id", "movie_title", "release_date", "video_release_date", "IMDb_URL", "unknown", "Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"])
    Movie = Movie[["movie_id", "movie_title", "release_date"]]
    Movie = Movie[Movie['movie_title'] != 'unknown']
    Genre = pd.read_csv('~/iron_yard_hw/django-movies/django_movies/ml-100k/u.genre', sep='|', names=['genre', 'genre_id'])
    UserInfo = pd.read_csv('~/iron_yard_hw/django-movies/django_movies/ml-100k/u.user', sep='|', names=['user_id', 'age', 'gender', 'occupation', 'zip_code'])
    # look for "iterrows"