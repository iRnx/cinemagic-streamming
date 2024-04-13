from django.shortcuts import render
from utils.paginacao import get_paginated_data

from series.models.genre import Genero

from filmes.models import Filme


def desenhos_filmes(request):
    
    desenhos_filmes = Filme.objects.filter(active=True, type='desenho_filme')

    genre = Genero.objects.all().order_by('genre')
    total_desenhos = len(desenhos_filmes)

    paginated_series = get_paginated_data(request, desenhos_filmes, items_per_page=6)

    return render(request, 'home/desenhos_filmes.html', {'genres': genre, 'paginated_content': paginated_series, 'total_desenhos': total_desenhos})