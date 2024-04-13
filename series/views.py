from django.shortcuts import render, get_object_or_404

from series.models.episode import Episodio
from series.models.season import Temporada
from series.models.serie import Serie
from series.models.genre import Genero

from utils.paginacao import get_paginated_data


def list_series(request):
    
    series = Serie.objects.filter(active=True).order_by('name_serie')
    genre = Genero.objects.all().order_by('genre')
    total_series = series.count()

    paginated_series = get_paginated_data(request, series, items_per_page=12)

    return render(request, 'series/list_series.html', {'genres': genre, 'paginated_content': paginated_series, 'series': series, 'total_series': total_series})


def serie_detail(request, serie_id):

    serie = get_object_or_404(Serie, pk=serie_id)
    return render(request, 'series/serie_detail.html', {'serie': serie})


def episode_detail(request, episodio_id):

    episodio = get_object_or_404(Episodio, pk=episodio_id)
    return render(request, 'series/episode_detail.html', {'episode': episodio})


def return_episode_card_htmx(request):

    temporada_id = request.GET.get('temporada')
    episodios = Episodio.objects.filter(season__id=temporada_id)
    context = {'episodios': episodios}

    return render(request, 'partials/return_episode_card_htmx.html', context)


def series_per_letter(request, letter):
    
    series = Serie.objects.filter(name_serie__istartswith=letter).filter(active=True)
    total_series = series.count()
    paginated_series = get_paginated_data(request, series, items_per_page=6)

    return render(request, 'series/list_series.html', {'paginated_content': paginated_series, 'letter': letter, 'total_series': total_series})



