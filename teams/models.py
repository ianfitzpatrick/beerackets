from django.db import models
from django.contrib.auth.models import User
from leagues.models import League

class Team(models.Model):
    """
    A group of Member players within a League.
    """
    league = models.ForeignKey(
        League, related_name='teams', on_delete=models.CASCADE)
    captain = models.ForeignKey(
        User, related_name='captained_teams', on_delete=models.CASCADE)
    name = models.CharField(blank=True, max_length=255)
    
    members = models.ManyToManyField(
        'Member', related_name='member_of', blank=True)

    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return f'{self.name} (captained by {self.captain.get_full_name()})'


class Member(models.Model):
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(blank=True, max_length=255)
    discord_username = models.CharField(blank=True, max_length=255)

    def __str__(self):
       return f'{self.name} (@{self.discord_username})'
