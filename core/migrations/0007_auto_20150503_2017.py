# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_transponder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transponder',
            name='satellite',
            field=models.ForeignKey(to='core.Satellite', related_name='transponders'),
            preserve_default=True,
        ),
    ]
