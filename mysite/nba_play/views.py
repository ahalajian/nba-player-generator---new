from django.shortcuts import render
from django.http import HttpResponse

from django.core import serializers

from .models import Player, Result
from .forms import GenerateNbaPlayers, ResultForm

import json

def get_random_players(response):
  form = GenerateNbaPlayers(response.GET)
  
  if form.is_valid():
    num_players = form.cleaned_data['num_players']
    player_type = form.cleaned_data['player_type']
  else:
    num_players = 1
    player_type = 'current'

  if player_type == "all":
    players = Player.objects
  elif player_type == "current":
    players = Player.objects.filter(is_active=True)
  elif player_type == "historic":
    players = Player.objects.filter(is_active=False)

  random_players = players.order_by('?')[0:int(num_players)]

  return HttpResponse(
      json.dumps([player.serialize() for player in random_players]), 
      content_type="application/json")

def save_result(response):
  if response.method == "POST" and response.user.is_authenticated:
    form = ResultForm(response.POST)
    if form.is_valid():
      result = form.save(commit=False)
      result.user = response.user
      result.save()
      return HttpResponse(json.dumps({"success": True}))
    else:
      return HttpResponse(json.dumps({'success': False}))
    
def scores(response):
  user_id = response.user.id
  scores = Result.objects.filter(user_id = user_id)

  sort_by = response.GET.get('sort_by')
  if sort_by == 'date':
    scores = scores.order_by('date')
  elif sort_by == 'score':
    scores = scores.order_by('-score')  

  return render(response, "nba_play/scores.html", {"scores": scores})

def leaderboard(response):
  scores = Result.objects.order_by('-score')[:10]
  return render(response, "nba_play/leaderboard.html", {"scores": scores})

# Create your views here.
def index(response):
  form = GenerateNbaPlayers(response.GET)
  # form = GenerateNbaPlayers(response.GET)
  # get_random_players(response)
  return render(response, "nba_play/index.html", {"form":form})

def guess(response):
  return render(response, "nba_play/guess.html", {})

