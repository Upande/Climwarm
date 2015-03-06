# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column=b'id')),
                ('area_code', models.CharField(default=b'', max_length=50)),
                ('area_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'area',
            },
            bases=(models.Model,),
        ),
    ]
