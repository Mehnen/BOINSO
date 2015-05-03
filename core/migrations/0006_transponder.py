# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150503_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transponder',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('up_low', models.BigIntegerField(blank=True)),
                ('up_high', models.BigIntegerField(blank=True)),
                ('down_low', models.BigIntegerField(blank=True)),
                ('down_high', models.BigIntegerField(blank=True)),
                ('satellite', models.ForeignKey(to='core.Satellite')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
