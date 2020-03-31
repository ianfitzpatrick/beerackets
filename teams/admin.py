from django.contrib import admin
from .models import Team, Member


class TeamAdmin(admin.ModelAdmin):
    readonly_fields = (
        'open_match', 'created', 'modified', 'wins', 'losses',
        'matches')


admin.site.register(Team, TeamAdmin)
admin.site.register(Member)

