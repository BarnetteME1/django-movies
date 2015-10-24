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
from movies.views import index_view, MovieDetail, MovieList, movie_list_view

urlpatterns = [
    url(r'^$', index_view),
    url(r'^movies/$', movie_list_view, name='movie_list'),
    #url(r'^cbv/movies/$', MovieList.as_view(), name="movie_list_cbv"),
    #url(r'^cbv/movies/(?P<pk>\d+)/$', MovieDetail.as_view(), name="movie_detail_cbv"),
    url(r'^admin/', include(admin.site.urls)),
]
