# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_timecontrol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interval',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
