# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-28 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algo', '0010_algo_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algo',
            name='level',
            field=models.IntegerField(default=10, null=True),
        ),
    ]