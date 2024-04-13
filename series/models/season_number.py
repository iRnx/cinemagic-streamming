from django.db import models


class NumeroTemporada(models.Model):
    number = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return str(self.number)