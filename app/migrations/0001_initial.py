# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='aparcamiento',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nombre', models.TextField(default='')),
                ('url', models.TextField(default='')),
                ('descripcion', models.TextField(default='')),
                ('barrio', models.TextField(default='')),
                ('distrito', models.TextField(default='')),
                ('accesibilidad', models.TextField(default='')),
                ('latitud', models.IntegerField(default=0)),
                ('longitud', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('comentario', models.TextField(default='')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('aparcamiento', models.ForeignKey(to='app.aparcamiento')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CSS',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('titulo', models.TextField(default='Pagina de usuario')),
                ('color', models.CharField(default='#808080', max_length=32)),
                ('tamaño', models.IntegerField(default=1)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='seleccionado',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('aparcamiento', models.ForeignKey(to='app.aparcamiento')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
