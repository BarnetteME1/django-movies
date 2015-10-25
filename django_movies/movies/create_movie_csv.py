import pandas as pd


def movie_csv(apps, schema_edirot):

    movie = pd.read_csv('~/iron_yard_hw/django-movies/django_movies/ml-100k/u.item', sep='|', encoding='windows-1252',
                        names=["movie_id", "movie_title", "release_date", "video_release_date", "IMDb_URL", "unknown",
                               "Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary",
                               "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi",
                               "Thriller", "War", "Western"])
    movie = movie[["movie_id", "movie_title", "release_date"]]
    Movie = apps.get_model('movies', 'Movie')
    for index, row in movie.iterrows():
        movie_id = row.movie_id
        movie_title = row.movie_title
        release_date = row.release_date
        Movie.objects.create(id=movie_id, title=movie_title, release_date=release_date)


def user_csv(apps, schema_edirot):

    user_info = pd.read_csv('~/iron_yard_hw/django-movies/django_movies/ml-100k/u.user', sep='|',
                            names=['user_id', 'age', 'gender', 'occupation', 'zip_code'])
    Rater = apps.get_model('movies', 'Rater')
    for index, row in user_info.iterrows():
        user_id = row.user_id
        age = row.age
        gender = row.gender
        occupation = row.occupation
        zip_code = row.zip_code
        Rater.objects.create(id=user_id, age=age, gender=gender, occupation=occupation, zip=zip_code)


def info_csv(apps, schema_editor):
    id_info = pd.read_csv('~/iron_yard_hw/django-movies/django_movies/ml-100k/u.data', sep='\t',
                          names=['user_id', 'movie_id', 'rating', 'timestamp'])

    Movie = apps.get_model('movies', 'Movie')
    Rater = apps.get_model('movies', 'Rater')
    Rating = apps.get_model("movies", 'Rating')
    for index, row in id_info.iterrows():
        user_id = row.user_id
        movie_id = row.movie_id
        rating = row.rating
        user = Rater.objects.get(id=user_id)
        movie = Movie.objects.get(id=movie_id)
        Rating.objects.create(user_id=user, movie_id=movie, rating=rating)
