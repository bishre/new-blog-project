# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-08 12:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171008_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 8, 12, 26, 17, 176820, tzinfo=utc)),
        ),
    ]
