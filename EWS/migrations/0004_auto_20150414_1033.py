# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EWS', '0003_hazard_hazardreading'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hazardreading',
            name='hazard',
        ),
        migrations.DeleteModel(
            name='Hazard',
        ),
        migrations.DeleteModel(
            name='HazardReading',
        ),
    ]
