import hashlib
import random
from django.shortcuts import render
from utils.paginacao import get_paginated_data

from series.models.serie import Serie

from filmes.models import Filme
from itertools import chain



def movies_series(request):
    series = Serie.objects.filter(active=True, type='serie')
    filmes = Filme.objects.filter(active=True, type='filme')

    # Combinar as consultas em uma única lista
    resultados_combinados = list(chain(series, filmes))

    # Embaralhamento adicional: adicione um critério de aleatoriedade
    random.seed(42)  # Seed para garantir a mesma aleatoriedade
    random.shuffle(resultados_combinados)

    # Ordenação "quase aleatória" com base no hash do ID ou de outro campo
    resultados_combinados.sort(key=lambda x: (
        int(hashlib.sha1(str(x.id).encode('utf-8')).hexdigest(), 16),
        random.random()  # Adiciona um fator de aleatoriedade adicional
    ))

    paginated_content = get_paginated_data(request, resultados_combinados, items_per_page=6)

    total_filme_series = len(resultados_combinados)

    return render(request, 'home/movies_series.html', {
        'paginated_content': paginated_content,
        'total_filme_series': total_filme_series
    })