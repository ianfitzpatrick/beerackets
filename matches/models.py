from django.db import models
from django.forms import ValidationError
from teams.models import Team


class Match(models.Model):

    challenger = models.ForeignKey(
        Team, related_name='challenger_matches', on_delete=models.CASCADE)
    defender = models.ForeignKey(
        Team, related_name='defender_matches', on_delete=models.CASCADE)

    scheduled = models.DateTimeField(blank=True, null=True)

    winner = models.ForeignKey(
        Team, related_name='won_matches', on_delete=models.CASCADE, blank=True,
        null=True
    )
    loser = models.ForeignKey(
        Team, related_name='lost_matches', on_delete=models.CASCADE, blank=True,
        null=True
    )

    forfeit_team = models.ForeignKey(
        Team, related_name='forfeit_matches',
        on_delete=models.CASCADE, blank=True, null=True
    )

    rank_applied = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Matches'

    def __str__(self):
        return f'{self.challenger.name} vs {self.defender.name}'

    def end_match(self, winner=None, forfeit_team=None):
        """
        Set Winner and Loser for match. Update Team Ladder Ranks accordingly.

        Sets winner and loser for a match, and updates ladder ranks, according
        to the following rules:
            
            - Rank has NOT already been applied based on the result of match

            - If `winner` argument is specified, assigned winner and loser
              accordingly.

            - If no `forfeit` team argument is specified, assign that team
              as loser and other team as winner

            - If neither argument supplied, mark challenger as winner and
              defender as forfeit.

        Rank logic is applied as follows:

            - If the CHALLENGER wins, the challenger and defender team's
              ladder ranks are swapped.

            - If the DEFENDER wins, all team ranks remain the same.
        """
        # First do some quick sanity checking
        if winner:
            if not (self.challenger or self.defender):
                raise ValueError(
                    'Winner must be a team associated with this match.')

        if forfeit_team:
           if not (self.challenger or self.defender):
                raise ValueError(
                    'Forfeit team must be a team associated with this match.')            

        # Next, set winner and loser depending on which arguments were passed
        teams = Team.objects.filter(
            pk__in=[self.challenger.id, self.defender.id])

        if winner:
            self.winner = winner
            self.loser = teams.exclude(id=self.winner.id).get()

        if forfeit_team:
            self.forfeit_team = forfeit_team    
            self.loser = forfeit_team
            self.winner = teams.exclude(id=self.loser.id).get()

        else:
            self.winner = self.challenger
            self.loser = self.defender


        if not self.rank_applied:
            # Now apply rank according to winner and loser
            if self.winner == self.challenger:
                challenger_old_rank = self.challenger.ladder_rank
                defender_old_rank = self.defender.ladder_rank

                self.challenger.ladder_rank = defender_old_rank
                self.defender.ladder_rank = challenger_old_rank

                self.challenger.save()
                self.defender.save()


            else:
                # If the defender wins, no rank changes occur
                pass

            self.rank_applied = True

        self.save()





