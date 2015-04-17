# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('EWS', '0010_auto_20150415_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hazardreading',
            name='extent_image_file',
        ),
        migrations.AddField(
            model_name='hazardreading',
            name='hazard_image_file',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hazardreading',
            name='reading_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 17, 8, 25, 55, 517171), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hazardreading',
            name='risk_image_file',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hazardreading',
            name='vulnerability_image_file',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
