# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-27 19:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ComicCollectionTracker', '0006_remove_collection_is_default'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='user',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='collection',
        ),
        migrations.AddField(
            model_name='issue',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Collection',
        ),
        migrations.DeleteModel(
            name='DefaultCollection',
        ),
    ]
