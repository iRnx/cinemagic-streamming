from django.shortcuts import render
from utils.paginacao import get_paginated_data


from series.models.genre import Genero
from series.models.serie import Serie

from filmes.models import Filme
from itertools import chain


def desenhos_all(request):
    
    desenhos_series = Serie.objects.filter(active=True, type='desenho_serie')
    desenhos_filmes = Filme.objects.filter(active=True, type='desenho_filme')

    desenhos_combinados = list(chain(desenhos_series, desenhos_filmes))

    genre = Genero.objects.all().order_by('genre')
    total_desenhos = len(desenhos_combinados)

    paginated_series = get_paginated_data(request, desenhos_combinados, items_per_page=6)

    return render(request, 'home/desenhos_all.html', {'genres': genre, 'paginated_content': paginated_series, 'total_desenhos': total_desenhos})