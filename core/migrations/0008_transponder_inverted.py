# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150503_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='transponder',
            name='inverted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
