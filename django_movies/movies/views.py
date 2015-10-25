from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
from django.views.generic import ListView, DetailView
from movies.models import Movie, Rating, Rater


def index_view(request):
    context = {}
    return render_to_response(template_name='body.html', context=context)


def movie_list_view(request):
    movies = Movie.objects.all()
    return render_to_response(template_name='movie_list.html', context={'movie_list': movies})


def test_function(request):
    pass


def movie_detail_view(request, movie_id, user_id):
    movie = Movie.objects.get(id=movie_id)
    ratings = Rater.objects.get(id=user_id)
    context = {"movie_object": movie, 'rating': ratings}
    # average_rating = Rater.objects.annotate(average_rating=Avg('rating')).values('movie_id', 'average_rating')
    return render_to_response(template_name='movie_detail.html', context=context)


class MovieList(ListView):
    model = Movie


class MovieDetail(DetailView):
    model = Movie