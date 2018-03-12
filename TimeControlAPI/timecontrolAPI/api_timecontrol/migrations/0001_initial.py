# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Interval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('init_date', models.DateTimeField()),
                ('fin_date', models.DateTimeField(null=True, blank=True)),
                ('duration', models.IntegerField(max_length=100, blank=True, null=True)),
            ],
            options={
                'db_table': 'interval',
            },
        ),
        migrations.CreateModel(
            name='TimeBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssid', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'timeblock',
            },
        ),
    ]
