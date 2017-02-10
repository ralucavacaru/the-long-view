# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='requirements',
            new_name='impacts',
        ),
    ]
