# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('year', models.IntegerField()),
                ('identifier', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('full_story', models.TextField()),
                ('why', models.TextField()),
                ('requirements', models.TextField()),
            ],
        ),
    ]
