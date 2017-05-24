# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170524_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='aparcamiento',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]
