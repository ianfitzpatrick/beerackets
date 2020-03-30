from django.db import models
from django.contrib.auth.models import User


class League(models.Model):
    """Organize Teams within a League."""
    name = models.CharField(max_length=255, help_text='Name your league')
    captains = models.ManyToManyField(User, related_name='captain_of')

    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
