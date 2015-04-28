# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='altitude',
            field=models.FloatField(default=45),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='latitude',
            field=models.FloatField(default=51.483462),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='longitude',
            field=models.FloatField(default=0.0586198),
            preserve_default=True,
        ),
    ]
