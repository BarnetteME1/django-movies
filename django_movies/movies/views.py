from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
from django.views.generic import ListView, DetailView
from movies.models import Movie, Rating, Rater, TopTwenty


def index_view(request):
    context = {}
    return render_to_response(template_name='body.html', context=context)


class MovieList(ListView):
    model = Movie


class MovieDetail(DetailView):
    model = Movie


class RaterList(ListView):
    model = Rater


class RaterDetail(DetailView):
    model = Rater


class TopMoviesListView(ListView):
    model = TopTwenty
    template_name = 'movies/movie_list.html'

    def get_queryset(self):
        return TopTwenty.top_movies
