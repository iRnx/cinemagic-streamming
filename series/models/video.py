from django.db import models

from series.models.episode import Episodio


class Video(models.Model):
    video = models.FileField(upload_to='videos/series')
    episode = models.ForeignKey(Episodio, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f'{self.episode.season}'
    