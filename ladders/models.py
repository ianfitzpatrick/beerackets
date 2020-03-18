from datetime import timedelta
from django.db import models
from leagues.models import League


class Ladder(models.Model):
    league = models.OneToOneField(League, on_delete=models.CASCADE)
    rematch_wait = models.DurationField(default=timedelta(days=7))
    result_deadline = models.DurationField(default=timedelta(days=3))

    def __str__(self):
        return f'Ladder for {self.league}'
