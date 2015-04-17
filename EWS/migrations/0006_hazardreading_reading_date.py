# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('EWS', '0005_hazard_hazardreading'),
    ]

    operations = [
        migrations.AddField(
            model_name='hazardreading',
            name='reading_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 14, 11, 33, 3, 540944), auto_now_add=True),
            preserve_default=True,
        ),
    ]
