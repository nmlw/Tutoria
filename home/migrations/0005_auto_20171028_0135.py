# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_profile_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='wallet',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]