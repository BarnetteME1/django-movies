# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IdInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100, blank=True)),
                ('release_date', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('occupation', models.CharField(max_length=25)),
                ('zip', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='idinfo',
            name='movie_id',
            field=models.ForeignKey(to='movies.Movie'),
        ),
        migrations.AddField(
            model_name='idinfo',
            name='user_id',
            field=models.ForeignKey(to='movies.UserInfo'),
        ),
    ]
