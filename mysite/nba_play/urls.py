from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("guess/", views.guess, name="guess"),
    path("get_random_players/", views.get_random_players, name="get_random_players"),
    path('home', views.index, name='index'),
    path("save_result/", views.save_result, name="save_result"),
    path("scores/", views.scores, name="scores"),
    path("leaderboard/", views.leaderboard, name="leaderboard")
]