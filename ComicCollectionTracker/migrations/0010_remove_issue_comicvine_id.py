# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-29 17:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ComicCollectionTracker', '0009_auto_20170329_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='comicvine_id',
        ),
    ]
