from django.shortcuts import render, get_object_or_404
from series.models.genre import Genero
from .models import Filme, FilmeVideo
from utils.paginacao import get_paginated_data


def list_movies(request):
    filmes = Filme.objects.filter(active=True).order_by('name_movie')
    total_filmes = filmes.count()
    generos = Genero.objects.all().order_by('genre')

    paginated_filmes = get_paginated_data(request, filmes, items_per_page=6)

    return render(request, 'filmes/list_movies.html', {'generos': generos, 'paginated_content': paginated_filmes, 'filmes': filmes, 'total_filmes': total_filmes})


def movie_detail(request, filme_id):
    filme = get_object_or_404(Filme, pk=filme_id)
    return render(request, 'filmes/movie_detail.html', {'filme': filme})


def movie_video(request, id):
    movie = get_object_or_404(Filme, id=id)
    return render(request, 'filmes/videos.html', {'movie': movie})



