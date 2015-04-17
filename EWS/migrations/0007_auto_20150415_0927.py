# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('EWS', '0006_hazardreading_reading_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='hazardreading',
            name='image_file',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hazardreading',
            name='reading_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 15, 9, 27, 42, 702695), auto_now_add=True),
            preserve_default=True,
        ),
    ]
