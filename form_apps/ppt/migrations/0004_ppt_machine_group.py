# Generated by Django 3.2.7 on 2022-02-27 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppt', '0003_auto_20220227_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='ppt',
            name='machine_Group',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]