# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20171112_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='wallet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutor', to='transaction.Wallet'),
        ),
    ]
