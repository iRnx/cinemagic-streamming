from django.db import models

from series.models.genre import Genero
from series.models.collection import Collections


class Serie(models.Model):

    class TypeChoices(models.TextChoices):
        DESENHO = 'desenho_serie'
        SERIE = 'serie'

    name_serie = models.CharField(max_length=100)
    name_serie_portuguese = models.CharField(max_length=100, blank=True, null=True)
    image_thumb = models.ImageField(upload_to='images/thumb')
    image_detail = models.ImageField(upload_to='images/detail')
    genre = models.ManyToManyField(Genero)
    type = models.CharField(max_length=13, choices=TypeChoices.choices)
    active = models.BooleanField(default=True)
    collection = models.ForeignKey(Collections, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self) -> str:
        return self.name_serie