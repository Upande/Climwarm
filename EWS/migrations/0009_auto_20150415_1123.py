# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('EWS', '0008_auto_20150415_0951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hazardreading',
            old_name='image_file',
            new_name='extent_image_file',
        ),
        migrations.AddField(
            model_name='hazardreading',
            name='risk_image_file',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hazardreading',
            name='vulnerability_image_file',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hazardreading',
            name='reading_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 15, 11, 23, 16, 333588), auto_now_add=True),
            preserve_default=True,
        ),
    ]
