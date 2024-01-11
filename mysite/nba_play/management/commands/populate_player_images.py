from django.core.management.base import BaseCommand
from django.db import transaction

import requests

from nba_play.models import Player, PlayerImage

class Command(BaseCommand):
  help = "Populate whether NBA player has image in database"

  def handle(self, *args, **options):
    all_players = Player.objects.all()
    
    try:
      with transaction.atomic():
        for i, player in enumerate(all_players):
          has_image = requests.get(f"https://cdn.nba.com/headshots/nba/latest/260x190/{player.nba_id}.png").status_code == 403
          new_image = PlayerImage(nba_id = player['nba_id'], has_image = has_image)
          new_image.save()
          if i % 100 == 0: print(f'Added {i} players')
        
        print(f'All {i} players added')
    
    except Exception as e:
        transaction.rollback()
