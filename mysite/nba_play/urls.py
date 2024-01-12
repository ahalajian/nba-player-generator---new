from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("guess/", views.guess, name="guess"),
    path("get_random_players/", views.get_random_players, name="get_random_players"),
    path("guess/get_random_players/", views.get_random_players, name="guess_get_random_players")


]