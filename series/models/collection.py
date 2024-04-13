from django.db import models

class Collections(models.Model):
    collection = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.collection