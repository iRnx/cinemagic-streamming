from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_series, name='list_series'),
    path('serie/<int:serie_id>/', views.serie_detail, name='serie_detail'),
    path('episodio/<int:episodio_id>/', views.episode_detail, name='episode_detail'),
    path('return_episode_card_htmx/', views.return_episode_card_htmx, name='return_episode_card_htmx'),


    path('letter/A/', views.series_per_letter, {'letter': 'A'}, name='series_letter_A'),
    path('letter/B/', views.series_per_letter, {'letter': 'B'}, name='series_letter_B'),
    path('letter/C/', views.series_per_letter, {'letter': 'C'}, name='series_letter_C'),
    path('letter/D/', views.series_per_letter, {'letter': 'D'}, name='series_letter_D'),
    path('letter/E/', views.series_per_letter, {'letter': 'E'}, name='series_letter_E'),
    path('letter/F/', views.series_per_letter, {'letter': 'F'}, name='series_letter_F'),
    path('letter/G/', views.series_per_letter, {'letter': 'G'}, name='series_letter_G'),
    path('letter/H/', views.series_per_letter, {'letter': 'H'}, name='series_letter_H'),
    path('letter/I/', views.series_per_letter, {'letter': 'I'}, name='series_letter_I'),
    path('letter/J/', views.series_per_letter, {'letter': 'J'}, name='series_letter_J'),
    path('letter/K/', views.series_per_letter, {'letter': 'K'}, name='series_letter_K'),
    path('letter/L/', views.series_per_letter, {'letter': 'L'}, name='series_letter_L'),
    path('letter/M/', views.series_per_letter, {'letter': 'M'}, name='series_letter_M'),
    path('letter/N/', views.series_per_letter, {'letter': 'N'}, name='series_letter_N'),
    path('letter/O/', views.series_per_letter, {'letter': 'O'}, name='series_letter_O'),
    path('letter/P/', views.series_per_letter, {'letter': 'P'}, name='series_letter_P'),
    path('letter/Q/', views.series_per_letter, {'letter': 'Q'}, name='series_letter_Q'),
    path('letter/R/', views.series_per_letter, {'letter': 'R'}, name='series_letter_R'),
    path('letter/S/', views.series_per_letter, {'letter': 'S'}, name='series_letter_S'),
    path('letter/T/', views.series_per_letter, {'letter': 'T'}, name='series_letter_T'),
    path('letter/U/', views.series_per_letter, {'letter': 'U'}, name='series_letter_U'),
    path('letter/V/', views.series_per_letter, {'letter': 'V'}, name='series_letter_V'),
    path('letter/W/', views.series_per_letter, {'letter': 'W'}, name='series_letter_W'),
    path('letter/X/', views.series_per_letter, {'letter': 'X'}, name='series_letter_X'),
    path('letter/Y/', views.series_per_letter, {'letter': 'Y'}, name='series_letter_Y'),
    path('letter/Z/', views.series_per_letter, {'letter': 'Z'}, name='series_letter_Z'),

]
