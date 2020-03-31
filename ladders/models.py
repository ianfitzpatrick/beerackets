from datetime import timedelta
from django.db import models
from leagues.models import League
from matches.models import Match
from teams.models import Team


class Ladder(models.Model):
    league = models.OneToOneField(League, on_delete=models.CASCADE)
    rematch_wait = models.DurationField(default=timedelta(days=7))
    result_deadline = models.DurationField(default=timedelta(days=3))

    def __str__(self):
        return f'Ladder for {self.league}'

    def create_challenge(self, challenger, defender):
        """
        Generate a new match challenge after validating it's possible.
        """
        if self.validate_challenge(challenger, defender):
            match = Match.objects.create(
                challenge=challenger,
                defender=defender
            )
            return match

        return None

    def validate_challenge(self, challenger, defender):
        """
        Confirm a possible challenge match meets required criteria.

        Match challenge criteria are as following:

            - Neither team has an OPEN match challenge pending

            - Both teams are within ONE rank of each other OR
              Both teams have SAME rank

            - Both teams are in the same LEAGUE

            - Both teams are not the SAME team
        """
        # Start with most conservative assumptions
        open_matches = same_team_twice = True
        same_league = teams_within_one_rank = teams_have_same_rank = False

        if not challenger.open_match and not defender.open_match:
            open_matches = False

        if challenger != defender:
            same_team_twice = False

        if challenger.league == defender.league:
            same_league = True

        if defender.ladder_ranking.position - challenger.ladder_ranking.position == 1:
            teams_within_one_rank = True

        if defender.ladder_ranking.position == challenger.ladder_ranking.position:
            teams_have_same_rank = True

        if not open_matches and not same_team_twice:
            if same_league:
                if teams_within_one_rank or teams_have_same_rank:
                    return True

        return False


class LadderRanking(models.Model):
    position = models.PositiveSmallIntegerField(default=9999)
    team = models.OneToOneField(
        Team, related_name='ladder_ranking', on_delete=models.CASCADE)
