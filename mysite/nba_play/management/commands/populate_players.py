from django.core.management.base import BaseCommand
from django.db import transaction
from nba_api.stats.static import players

from nba_play.models import Player

class Command(BaseCommand):
  help = "Populate NBA player data (first, last, active) in database"

  def handle(self, *args, **options):
    all_players = players.get_players()
    try:
      with transaction.atomic():
        for i, row in enumerate(all_players):
          new_player = Player(nba_id = row['id'], first_name = row['first_name'], 
                            last_name = row['last_name'], is_active = row['is_active'])
          new_player.save()
          if i % 100 == 0: print(f'Added {i} players')
        print(f'All {i} players added')
    except Exception as e:
        transaction.rollback()
