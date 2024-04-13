from django.shortcuts import render
from utils.paginacao import get_paginated_data

from series.models.genre import Genero

from series.models import Serie


def series(request):
    
    series = Serie.objects.filter(active=True, type='serie')

    genre = Genero.objects.all().order_by('genre')

    total_series = len(series)

    paginated_series = get_paginated_data(request, series, items_per_page=6)

    return render(request, 'home/series.html', {'genres': genre, 'paginated_content': paginated_series, 'total_series': total_series})