from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_movies, name='list_movies'),
    path('filme/<int:filme_id>', views.movie_detail, name='movie_detail'),
    path('movie_video/<int:id>', views.movie_video, name='movie_video'),
]