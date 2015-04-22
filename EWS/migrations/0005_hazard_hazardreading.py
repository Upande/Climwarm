# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EWS', '0004_auto_20150414_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hazard',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('hazard_name', models.CharField(default=b'', max_length=50)),
            ],
            options={
                'db_table': 'hazard',
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
                'db_table': 'hazard_reading',
            },
            bases=(models.Model,),
        ),
    ]
