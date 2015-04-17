# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('EWS', '0009_auto_20150415_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hazardreading',
            name='reading_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 15, 11, 24, 21, 397571), auto_now_add=True),
            preserve_default=True,
        ),
    ]
