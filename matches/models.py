from django.db import models
from django.forms import ValidationError
from teams.models import Team


class Match(models.Model):

    challenger = models.ForeignKey(
        Team, related_name='challenger_matches', on_delete=models.CASCADE)
    defender = models.ForeignKey(
        Team, related_name='defender_matches', on_delete=models.CASCADE)

    winner = models.ForeignKey(
        Team, related_name='won_matches', on_delete=models.CASCADE, blank=True,
        null=True
    )

    loser = models.ForeignKey(
        Team, related_name='lost_matches', on_delete=models.CASCADE, blank=True,
        null=True
    )

    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Matches'

    def __str__(self):
        return f'{self.challenger.name} vs {self.defender.name}'

    def end_match(self, winner):
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
        # Set winner and loser depending on which arguments were passed
        teams = Team.objects.filter(
            pk__in=[self.challenger.id, self.defender.id])

        self.winner = winner
        self.loser = teams.exclude(id=self.winner.id).get()

        # Do some quick sanity checking before saving.
        if not (self.winner == self.challenger or self.winner == self.defender):
            raise ValueError(
                'Winner must be a team associated with this match.')

        if not (self.loser == self.challenger or self.loser == self.defender):
            raise ValueError(
                'Loser must be a team associated with this match.')

        self.save()


class LadderMatch(Match):

    rank_applied = models.BooleanField(default=False)
    scheduled = models.DateTimeField(blank=True, null=True)

    def end_match(self, winner=None, forfeit_team=None):
        """
        Override base end_match method to perform extra ladder-related tasks.

        First update ladder ranks, according to the following rules:

            - IF Rank has NOT already been applied based on the result of match

                - IF `winner` argument is specified, assigned winner and loser
                  accordingly.

                - IF `forfeit` team argument is specified, assign that team
                  as loser and other team as winner

                - ELSE IF neither argument supplied, raise ValueError.

        Then, call parent end_match() method, and pass in winner as determined
        above.

        Rank logic is applied as follows:

            - IF the CHALLENGER wins, the challenger and defender team's
              ladder ranks are swapped.

            - IF the DEFENDER wins, all team ranks remain the same.
        """
        if forfeit_team:
            if not (forfeit_team == self.challenger or forfeit_team == self.defender):
                raise ValueError(
                    'Forfeit team must be a team associated with this match.')
        elif winner:
            if not (winner == self.challenger or winner == self.defender):
                raise ValueError(
                    'Winner must be a team associated with this match.')
        else:
            raise ValueError(
                'A winner or forefeiting team must be specified.')

        if forfeit_team:
            self.forfeit_team = forfeit_team
            winner = teams.exclude(id=forfeit_team.id).get()

        if not self.rank_applied:
            # Now apply rank according to winner and loser
            if winner == self.challenger:
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

        super().end_match(winner)
