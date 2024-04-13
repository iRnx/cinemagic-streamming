from django.urls import path
from .views import *

urlpatterns = [
    path('', home.home, name='home'),
    path('series/', series.series, name='series'),
    path('filmes/', filmes.filmes, name='filmes'),
    path('movies_series/', movies_series.movies_series, name='movies_series'),
    path('search/', search_home.search_home, name='search_home'),
    path('movies_series_by_genero_home/<str:genero>/', movies_series_by_genero_home.movies_series_by_genero_home, name='movies_series_by_genero_home'),
    path('movies/<str:genero>/', movies_by_genre.movies_by_genre, name='movies_by_genre'),

    path('collections/<str:collection>/', collection_all.collection_all, name='collection_all'),
    path('desenhos_all', desenhos_all.desenhos_all, name='desenhos_all'),
    path('desenhos_serie/', desenhos_series.desenhos_series, name='desenhos_series'),
    path('desenhos_filmes/', desenhos_filmes.desenhos_filmes, name='desenhos_filmes'),


]