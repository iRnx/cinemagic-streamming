from django.shortcuts import render

from series.models.serie import Serie

from filmes.models import Filme
from random import shuffle
from django.db.models import Q
from itertools import chain


def search_home(request):
    search = request.GET.get('search').strip()

    # Series
    # series = Serie.objects.filter(nome_serie__icontains=search).filter(active=True)
    series = Serie.objects.filter(
        Q(name_serie__icontains=search) & Q(active=True) | Q(name_serie_portuguese__icontains=search) & Q(active=True))
    
    # Filmes
    filmes = Filme.objects.filter(name_movie__icontains=search).filter(active=True)
    total_filmes = filmes.count()


    resultados_combinados_search = list(chain(series, filmes))
    shuffle(resultados_combinados_search)
    
    total_resultados = len(resultados_combinados_search)

    context = {
        # 'series': series,
        # 'filmes': filmes,
        'resultados_combinados_search': resultados_combinados_search,
        # 'total_resultados': total_resultados,
        'search': search,
        
    }

    return render(request, "home/search.html", context)