# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-26 16:00
from __future__ import unicode_literals

from server.models import *
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0010_auto_20180726_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='serial',
            field=models.CharField(max_length=200, unique=True, verbose_name=b'Serial Number'),
        ),
    ]