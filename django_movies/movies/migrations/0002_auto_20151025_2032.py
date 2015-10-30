# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from movies.create_movie_csv import movie_csv


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(movie_csv)
    ]
