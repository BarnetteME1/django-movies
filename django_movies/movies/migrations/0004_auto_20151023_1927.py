# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from movies.create_movie_csv import info_csv


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20151023_1927'),
    ]

    operations = [
        migrations.RunPython(info_csv)
    ]
