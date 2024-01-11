from django.shortcuts import render
from django.http import HttpResponse

from .models import Player
from .forms import GenerateNbaPlayers

import time

def get_random_players(num_players, player_type):
        if player_type == "all":
              players = Player.objects
        elif player_type == "current":
          players = Player.objects.filter(is_active=True)
        elif player_type == "historic":
          players = Player.objects.filter(is_active=False)
  
        return players.order_by('?')[0:int(num_players)]

# Create your views here.
def index(response):
  if response.method == "GET":
    form = GenerateNbaPlayers(response.GET)
  
    if form.is_valid():
      num_players = form.cleaned_data['num_players']
      player_type = form.cleaned_data['player_type']

      players = get_random_players(num_players, player_type)

      return render(response, "nba_play/index.html", {"form":form, "players": players})
  
  else:
    form = GenerateNbaPlayers()
  
  return render(response, "nba_play/index.html", {"form":form})



def guess(response):
  return render(response, "nba_play/guess.html", {})

