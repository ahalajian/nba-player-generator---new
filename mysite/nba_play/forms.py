from django import forms

class GenerateNbaPlayers(forms.Form):
  num_players = forms.ChoiceField(
    label="Number of Players",
    choices=[(str(i), str(i))for i in range(1, 13)], 
    widget=forms.Select(attrs={'id': 'num-players'}))
  player_type = forms.ChoiceField(
    label="NBA Player Type",
    choices=[
            ('current', 'Current NBA Players'),
            ('historic', 'Historic NBA Players'),
            ('all', 'All NBA Players'),
        ],
    widget=forms.Select(attrs={'id': 'player-type'}))