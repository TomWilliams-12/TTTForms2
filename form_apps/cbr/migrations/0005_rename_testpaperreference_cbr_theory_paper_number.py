# Generated by Django 3.2.7 on 2022-02-08 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbr', '0004_auto_20220116_2145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cbr',
            old_name='testPaperReference',
            new_name='theory_Paper_Number',
        ),
    ]
