# Generated by Django 3.2.7 on 2022-02-27 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aw', '0006_auto_20220220_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aw',
            name='instructor_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='awInstructor2', to=settings.AUTH_USER_MODEL),
        ),
    ]