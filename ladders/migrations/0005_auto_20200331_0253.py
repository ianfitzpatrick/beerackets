# Generated by Django 2.2.11 on 2020-03-31 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0008_auto_20200331_0253'),
        ('ladders', '0004_auto_20200331_0244'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rank',
            new_name='Ranking',
        ),
    ]
