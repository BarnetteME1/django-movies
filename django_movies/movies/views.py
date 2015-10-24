from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
from django.views.generic import ListView, DetailView
from movies.models import Movie


def index_view(request):
    return HttpResponse('hello')


def movie_list_view(request):
    movies = Movie.objects.all()
    return render_to_response(template_name='movie_list.html', context={'movie_list': movies})


class MovieList(ListView):
    model = Movie


class MovieDetail(DetailView):
    model = Movie
