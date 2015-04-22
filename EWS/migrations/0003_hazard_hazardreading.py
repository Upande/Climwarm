# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EWS', '0002_auto_20150306_0713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hazard',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('hazard_name', models.CharField(default=b'', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HazardReading',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('reading', models.DecimalField(default=0.0, max_digits=4, decimal_places=2)),
                ('hazard', models.ForeignKey(to='EWS.Hazard')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
