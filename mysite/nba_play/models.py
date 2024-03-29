from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
  """
  Player Model
  """
  nba_id = models.IntegerField(primary_key=True)
  last_name = models.CharField(max_length=200)
  first_name = models.CharField(max_length=200)
  is_active = models.BooleanField()

  def serialize(self):
    """
    Serializes a player object
    """
    return {"nba_id": self.nba_id, 
            "last_name": self.last_name, 
            "first_name": self.first_name,
            "is_active": self.is_active}

  class Meta:
    db_table = 'players'
  

class PlayerImage(models.Model):
  """
  Player Image Model
  """
  player = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='image', primary_key=True)
  has_image = models.BooleanField()

  class Meta:
    db_table = 'player_images'

class Result(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  score = models.IntegerField()
  date = models.DateField(auto_now_add=True)
  
  class Meta:
    db_table = 'results'

  def __str__(self):
    return self.user + "\n" + self.score
