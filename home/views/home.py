from django.shortcuts import render


from series.models.collection import  Collections
from series.models.genre import Genero
from series.models.serie import Serie

from filmes.models import Filme
from home.models.banners import Banner
from random import shuffle
from itertools import chain


def home(request):
   
    series_completas_query = list(Serie.objects.filter(active=True, type='serie').only('id', 'image_thumb')[:8])
    series_completas = sorted(series_completas_query, key=lambda x: x.id, reverse=True)
    
    desenhos_series_completos_query = list(Serie.objects.filter(active=True, type='desenho_serie').only('id', 'image_thumb')[:8])
    desenhos_series_completos = sorted(desenhos_series_completos_query, key=lambda x: x.id, reverse=True)

    filmes_completos_query = list(Filme.objects.filter(active=True, type='filme').only('id', 'image_thumb')[:8])
    filmes_completos = sorted(filmes_completos_query, key=lambda x: x.id, reverse=True)

    desenhos_completos_query = list(Filme.objects.filter(active=True, type='desenho_filme').only('id', 'image_thumb')[:8])
    desenhos_completos = sorted(desenhos_completos_query, key=lambda x: x.id, reverse=True)


    series = Serie.objects.filter(active=True, type='serie')
    filmes = Filme.objects.filter(active=True, type='filme')

    # Combinar as consultas em uma única lista
    resultados_combinados = list(chain(series, filmes, ))
    shuffle(resultados_combinados)
    
    generos = Genero.objects.all()
   
    generos_embaralhados = list(generos)
    shuffle(generos_embaralhados)  
    
    series_e_filmes_por_genero = {}

    for genero_nome in generos_embaralhados:
        
        series_genero = Serie.objects.filter(genre=genero_nome, active=True)
        filmes_genero = Filme.objects.filter(genre=genero_nome, active=True)
        genero_resultados = list(chain(series_genero, filmes_genero))
        shuffle(genero_resultados)
        series_e_filmes_por_genero[genero_nome] = genero_resultados

   
    banners = Banner.objects.filter(active=True)
    collections = Collections.objects.all()

    context = {
        'series_completas': series_completas,
        'desenhos_series_completos': desenhos_series_completos,
        'filmes_completos': filmes_completos,
        'desenhos_completos': desenhos_completos,
        'series_e_filmes_por_genero': series_e_filmes_por_genero,
        'resultados_combinados': resultados_combinados,
        'genres': generos,
        'banners': banners,
        'collections': collections,

    }
    
    return render(request, "home/home.html", context)