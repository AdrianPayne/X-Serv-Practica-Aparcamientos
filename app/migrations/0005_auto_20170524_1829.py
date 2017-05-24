# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170523_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcamiento',
            name='telefono',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='css',
            name='color',
            field=models.CharField(null=True, blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='css',
            name='size',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='css',
            name='title',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='css',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=''),
        ),
    ]
