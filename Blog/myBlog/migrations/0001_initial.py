# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('btitle', models.CharField(max_length=200)),
                ('bcontent', models.TextField()),
            ],
            options={
                'db_table': 'Blog',
            },
        ),
        migrations.CreateModel(
            name='use',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=1000)),
                ('upw', models.CharField(max_length=1000)),
                ('uliuyan', models.TextField()),
            ],
            options={
                'db_table': 'use',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='bpid',
            field=models.ForeignKey(to='myBlog.use'),
        ),
    ]
