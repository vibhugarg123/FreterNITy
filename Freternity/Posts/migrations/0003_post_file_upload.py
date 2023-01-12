# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-10 13:22
from __future__ import unicode_literals

import Posts.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_auto_20170910_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file_upload',
            field=models.FileField(default=django.utils.timezone.now, upload_to=Posts.models.file_upload_location),
            preserve_default=False,
        ),
    ]
