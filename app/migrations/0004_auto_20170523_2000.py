# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170523_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='css',
            old_name='tamaño',
            new_name='size',
        ),
        migrations.RenameField(
            model_name='css',
            old_name='titulo',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='css',
            old_name='usuario',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='email',
            field=models.TextField(default=''),
        ),
    ]
