from django.shortcuts import render
from utils.paginacao import get_paginated_data

from series.models.genre import Genero
from series.models.serie import Serie


def desenhos_series(request):
    
    desenhos_series = Serie.objects.filter(active=True, type='desenho_serie')

    genre = Genero.objects.all().order_by('genre')
    total_desenhos = len(desenhos_series)

    paginated_series = get_paginated_data(request, desenhos_series, items_per_page=6)

    return render(request, 'home/desenhos_series.html', {'genres': genre, 'paginated_content': paginated_series, 'total_desenhos': total_desenhos})