# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170523_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='aparcamiento',
            name='email',
            field=models.TextField(default=0),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='telefono',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='tipo',
            field=models.TextField(default=0),
        ),
    ]
