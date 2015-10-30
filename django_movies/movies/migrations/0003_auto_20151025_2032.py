# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from movies.create_movie_csv import user_csv


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20151025_2032'),
    ]

    operations = [
        migrations.RunPython(user_csv)
    ]
