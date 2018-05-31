# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('btitle', models.CharField(max_length=200)),
                ('bpub_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('hname', models.CharField(max_length=200)),
                ('hgender', models.BooleanField()),
                ('hconter', models.CharField(max_length=200)),
                ('hbook', models.ForeignKey(to='booktest.Bookinfo')),
            ],
        ),
    ]
