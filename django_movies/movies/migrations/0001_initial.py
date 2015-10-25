# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('release_date', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('occupation', models.CharField(max_length=25)),
                ('zip', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('rating', models.IntegerField()),
                ('movie_id', models.ForeignKey(to='movies.Movie')),
                ('user_id', models.ForeignKey(to='movies.Rater')),
            ],
        ),
    ]
