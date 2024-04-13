from django.shortcuts import render
from utils.paginacao import get_paginated_data

from series.models.genre import Genero

from filmes.models import Filme


def filmes(request):
    
    filmes = Filme.objects.filter(active=True, type='filme')

    genre = Genero.objects.all().order_by('genre')

    total_filmes = len(filmes)

    paginated_filmes = get_paginated_data(request, filmes, items_per_page=6)

    return render(request, 'home/filmes.html', {'genres': genre, 'paginated_content': paginated_filmes, 'total_filmes': total_filmes})