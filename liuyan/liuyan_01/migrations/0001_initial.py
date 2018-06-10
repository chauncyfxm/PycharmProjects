# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='use',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('uname', models.CharField(max_length=1000)),
                ('upw', models.CharField(max_length=1000)),
                ('uliuyan', models.TextField()),
            ],
            options={
                'db_table': 'use',
            },
        ),
    ]
