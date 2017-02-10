# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_auto_20170209_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='article',
            field=models.TextField(default=b''),
        ),
    ]
