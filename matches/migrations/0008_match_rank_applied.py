# Generated by Django 2.2.11 on 2020-03-22 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0007_auto_20200322_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='rank_applied',
            field=models.BooleanField(default=False),
        ),
    ]