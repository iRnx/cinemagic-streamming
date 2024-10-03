from django.apps import AppConfig


class FilmesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filmes'

    def ready(self):
        from filmes import signals