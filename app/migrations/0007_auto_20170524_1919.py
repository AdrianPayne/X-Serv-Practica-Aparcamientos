# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170524_1917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aparcamiento',
            old_name='quantity',
            new_name='cantidad',
        ),
    ]
