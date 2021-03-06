# Generated by Django 3.2.7 on 2021-10-23 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseNumber', models.CharField(max_length=15, unique=True)),
                ('candidateNumber', models.IntegerField(blank=True, null=True)),
                ('courseType', models.CharField(max_length=30)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('venue', models.CharField(blank=True, max_length=50, null=True)),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courseInstructor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
