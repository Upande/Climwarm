# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('EWS', '0007_auto_20150415_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='hazardreading',
            name='threshold_level',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hazardreading',
            name='reading_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 15, 9, 51, 56, 890087), auto_now_add=True),
            preserve_default=True,
        ),
    ]
