# Generated by Django 3.2.7 on 2021-11-02 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='company_address',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='company_contact',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
