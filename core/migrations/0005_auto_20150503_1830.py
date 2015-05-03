# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_satellite_catalogue_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satellite',
            name='tle',
            field=models.FileField(null=True, blank=True, upload_to=''),
            preserve_default=True,
        ),
    ]
