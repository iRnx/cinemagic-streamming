from django.shortcuts import render
from utils.paginacao import get_paginated_data

from series.models.collection import  Collections
from series.models.serie import Serie
from filmes.models import Filme

from itertools import chain


def collection_all(request, collection):

    collection_objeto = Collections.objects.get(collection=collection)

    series = Serie.objects.filter(collection=collection_objeto, active=True)
    filmes = Filme.objects.filter( collection=collection_objeto, active=True)


    # Combinar as consultas em uma única lista
    resultados_combinados = list(chain(series, filmes))
    # shuffle(resultados_combinados)

    paginated_content = get_paginated_data(request, resultados_combinados)

    return render(request, 'home/list_collection.html', {'paginated_content': paginated_content, 'collection_objeto': collection_objeto})