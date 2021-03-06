# Generated by Django 2.2.11 on 2020-03-30 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_auto_20200322_2001'),
        ('matches', '0009_auto_20200330_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laddermatch',
            name='challenger',
        ),
        migrations.RemoveField(
            model_name='laddermatch',
            name='defender',
        ),
        migrations.RemoveField(
            model_name='laddermatch',
            name='forfeit_team',
        ),
        migrations.AddField(
            model_name='match',
            name='challenger',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='challenger_matches', to='teams.Team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='defender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='defender_matches', to='teams.Team'),
            preserve_default=False,
        ),
    ]
