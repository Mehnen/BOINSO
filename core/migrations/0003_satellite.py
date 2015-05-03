# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150428_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Satellite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('version', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=140)),
                ('nickname', models.CharField(max_length=140)),
                ('tle', models.FileField(null=True, upload_to='')),
                ('status', models.IntegerField(default=0, max_length=2, choices=[(0, 'operation status unknown'), (1, 'operational'), (2, 'non operational'), (3, 'partially operational'), (4, 'on standby'), (5, 'spare'), (6, 'extended mission')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
