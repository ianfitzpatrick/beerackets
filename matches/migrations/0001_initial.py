# Generated by Django 2.2.11 on 2020-03-18 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
                ('was_forefit', models.BooleanField(default=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('challenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenger_matches', to='teams.Team')),
                ('defender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='defender_matches', to='teams.Team')),
                ('loser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lost_matches', to='teams.Team')),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='won_matches', to='teams.Team')),
            ],
        ),
    ]
