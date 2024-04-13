from django.db import models

class Genero(models.Model):
    genre = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self) -> str:
        return self.genre