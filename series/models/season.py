from django.db import models

from series.models.season_number import NumeroTemporada
from series.models.serie import Serie


class Temporada(models.Model):
    season_number = models.ForeignKey(NumeroTemporada, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.serie} - Temporada {self.season_number}"