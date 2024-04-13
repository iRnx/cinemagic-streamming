import hashlib
from django.shortcuts import render
from utils.paginacao import get_paginated_data

from series.models.genre import Genero
from series.models.serie import Serie

from filmes.models import Filme
from itertools import chain


def movies_series_by_genero_home(request, genero):
    genero = genero.capitalize()

    # Consulta ao banco de dados para obter filmes desse gênero
    genero_objeto = Genero.objects.get(genre=genero)
    series_genero = Serie.objects.filter(genre=genero_objeto, active=True)
    filmes_genero = Filme.objects.filter(genre=genero_objeto, active=True)

    # Concatena os resultados
    genero_resultados = list(chain(series_genero, filmes_genero))
    
    # Ordena "quase aleatoriamente" com base no hash do ID
    genero_resultados.sort(key=lambda x: int(hashlib.sha1(str(x.id).encode('utf-8')).hexdigest(), 16))

    paginated_content = get_paginated_data(request, genero_resultados)

    return render(request, 'home/movies_series_by_genero_home.html', {'genero': genero, 'paginated_content': paginated_content})