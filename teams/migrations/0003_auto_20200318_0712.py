# Generated by Django 2.2.11 on 2020-03-18 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20200318_0651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='team',
        ),
        migrations.AlterField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='member_of', to='teams.Member'),
        ),
    ]
