"""django_movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from movies.views import MovieDetail, MovieList, index_view, RaterList, RaterDetail, TopMoviesListView, default_view

urlpatterns = [
    url(r'^$', default_view),
    url(r'^movies/$', MovieList.as_view(), name="movie_list"),
    url(r'^movies/(?P<pk>\d+)/$', MovieDetail.as_view(), name="movie_detail"),
    url(r'^users/$', RaterList.as_view(), name="rater_list"),
    url(r'^users/(?P<pk>\d+)/$', RaterDetail.as_view(), name="rater_detail"),
    url(r'^toptwenty/$', TopMoviesListView.as_view(), name="top_twenty"),

    url(r'^admin/', include(admin.site.urls))
]
