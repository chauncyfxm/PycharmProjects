# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('btitle', models.CharField(db_column='mybtitle', max_length=20)),
                ('bpub_date', models.DateTimeField()),
                ('bread', models.IntegerField(default=0)),
                ('bcommet', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'mybookInfo',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField(default=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('hcontent', models.CharField(max_length=100)),
                ('hbook', models.ForeignKey(to='modeldemo.BookInfo')),
            ],
        ),
    ]
