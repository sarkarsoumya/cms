# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0005_auto_20171009_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='resource',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
