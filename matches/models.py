from django.db import models
from teams.models import Team

class Match(models.Model):

    challenger = models.ForeignKey(
        Team, related_name='challenger_matches', on_delete=models.CASCADE)
    defender = models.ForeignKey(
        Team, related_name='defender_matches', on_delete=models.CASCADE)
    
    accepted = models.BooleanField(default=False)

    winner = models.ForeignKey(
        Team, related_name='won_matches', on_delete=models.CASCADE, blank=True,
        null=True
    )
    loser = models.ForeignKey(
        Team, related_name='lost_matches', on_delete=models.CASCADE, blank=True,
        null=True
    )

    was_forefit = models.BooleanField(default=False)

    
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Matches'

    def __str__(self):
       return f'{self.challenger.name} challenging {self.defender.name}'
