# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liuyan_01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='liuyan',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('lname', models.CharField(max_length=1000)),
                ('lemil', models.CharField(max_length=1000)),
                ('laddrees', models.CharField(max_length=1000)),
                ('ltext', models.TextField()),
            ],
            options={
                'db_table': 'liuyan',
            },
        ),
    ]
