from django.db import models
from series.models import Serie
from filmes.models import Filme


class Banner(models.Model):

    class CategorieChoices(models.TextChoices):
        FILME = 'Filme'
        SERIE = 'Serie'
       

    title = models.CharField(max_length=200)
    tipo_item = models.CharField(max_length=50, choices=CategorieChoices.choices)
    # Relação com série
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, blank=True, null=True)
    # Relação com filme
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, blank=True, null=True)
    imagem_banner = models.ImageField(upload_to='images_banners/banner')
    
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    