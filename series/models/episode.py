from django.db import models

from series.models.season import Temporada


class Episodio(models.Model):
    episode_number = models.PositiveIntegerField()
    episode_name = models.CharField(max_length=100)
    season = models.ForeignKey(Temporada, on_delete=models.CASCADE)
    

    class Meta:
        ordering = ['episode_number']


    def __str__(self) -> str:
        return self.episode_name