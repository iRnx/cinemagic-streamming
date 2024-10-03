from django.db import models
from series.models import Genero, Collections


class Filme(models.Model):

    class TypeChoices(models.TextChoices):
        DESENHO = 'desenho_filme'
        FILME = 'filme'


    name_movie = models.CharField(max_length=200)
    image_thumb = models.ImageField(upload_to='images/thumb')
    image_detail = models.ImageField(upload_to='images/detail')
    sinopse = models.CharField(max_length=650)
    genre = models.ManyToManyField(Genero)
    type = models.CharField(max_length=13, choices=TypeChoices.choices)
    collection = models.ForeignKey(Collections, on_delete=models.CASCADE, blank=True, null=True)
    hls_url = models.URLField(blank=True) # O campo para a URL do HLS
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name_movie
    

class FilmeVideo(models.Model):
    movie = models.ForeignKey(Filme, on_delete=models.CASCADE)
    file = models.FileField(upload_to='videos/movies')
    

    def __str__(self) -> str:
        return f'Vídeo de {self.movie.name_movie}'