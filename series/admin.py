from django.contrib import admin


from series.models.season_number import NumeroTemporada
from series.models.episode import Episodio
from series.models.serie import Serie
from series.models.collection import Collections
from series.models.genre import Genero
from series.models.season import Temporada
from series.models.video import Video


@admin.register(Temporada)
class TemporadaAdmin(admin.ModelAdmin):
    list_display = ('id', 'serie', 'season_number')
    list_display_links = ('id', 'serie')
    list_filter = ('serie',)
    search_fields = ('serie__name_serie',)
    ordering = ('serie__name_serie', 'season_number')


@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_serie', 'name_serie_portuguese', 'active')
    list_display_links = ('id', 'name_serie', 'name_serie_portuguese')
    list_editable = ('active',)
    list_filter = ('type', 'name_serie')
    ordering = ('name_serie',)


@admin.register(Episodio)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('season', 'episode_number', 'episode_name')
    list_display_links = ('season', 'episode_name')
    list_filter = ('season',)
    ordering = ('season', 'episode_number')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('get_episode_season', 'get_episode_name', 'get_episode_number', 'video',)
    ordering = ['episode__season', 'episode__episode_number']
    list_filter = ['episode__season']
    search_fields = ['episode__episode_name']


    def get_episode_name(self, obj):
        if obj.episode:
            return obj.episode.episode_name
        return "No Episode"  # Se não houver episódio associado
    
    get_episode_name.short_description = 'Episode Name'
    

    def get_episode_number(self, obj):
        if obj.episode:
            return obj.episode.episode_number
        return "No Episode"  # Se não houver episódio associado
    
    get_episode_number.short_description = 'Episode Number'


    def get_episode_season(self, obj):
        if obj.episode:
            return obj.episode.season
        return "No Episode"  # Se não houver episódio associado
    
    get_episode_season.short_description = 'Episode Season'


    

admin.site.register(NumeroTemporada)
admin.site.register(Genero)
admin.site.register(Collections)
