# Generated by Django 3.2.7 on 2022-02-01 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mewp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mewp',
            old_name='finishDate',
            new_name='finish_Date',
        ),
        migrations.RenameField(
            model_name='mewp',
            old_name='startDate',
            new_name='start_Date',
        ),
    ]
