# Generated by Django 2.2.11 on 2020-03-18 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0004_remove_match_accepted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='scheduled_date',
            new_name='scheduled',
        ),
    ]
