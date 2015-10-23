# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('genre', models.CharField(max_length=15, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='IdInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('item_id', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('title', models.CharField(max_length=100, blank=True)),
                ('release_date', models.DateField()),
            ],
        ),
    ]
