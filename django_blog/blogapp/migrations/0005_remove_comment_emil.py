# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-10 10:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_comment_emil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='emil',
        ),
    ]
