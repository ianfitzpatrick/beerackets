# Generated by Django 2.2.11 on 2020-03-22 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_auto_20200322_2001'),
        ('matches', '0006_auto_20200318_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='was_forfeit',
        ),
        migrations.AddField(
            model_name='match',
            name='forfeit_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forfeit_matches', to='teams.Team'),
        ),
    ]
