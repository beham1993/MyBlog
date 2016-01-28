# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('head', models.CharField(max_length=128)),
                ('sub_head', models.CharField(max_length=128)),
                ('date_of_article', models.DateField()),
                ('text_article', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('twitters', models.IntegerField(default=0)),
                ('facebooks', models.IntegerField(default=0)),
                ('vks', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
