from django.shortcuts import render
from utils.paginacao import get_paginated_data

from series.models.genre import Genero

from filmes.models import Filme


def movies_by_genre(request, genero):

    filmes = Filme.objects.filter(genre__genre__icontains=genero)
    generos = Genero.objects.all()
   
    
    paginated_content = get_paginated_data(request, filmes)

    context = {
        'paginated_content': paginated_content,
        'generos': generos,
        'total_filmes': filmes.count()
    }
    return render(request, 'filmes/movies_by_genre.html', context)