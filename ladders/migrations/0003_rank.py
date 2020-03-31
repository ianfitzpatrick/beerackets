# Generated by Django 2.2.11 on 2020-03-31 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_auto_20200331_0240'),
        ('ladders', '0002_auto_20200318_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveSmallIntegerField(default=9999)),
                ('ladder', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ladders.Ladder')),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teams.Team')),
            ],
        ),
    ]