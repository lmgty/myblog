# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-13 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_userinfo_pwd'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='token',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
