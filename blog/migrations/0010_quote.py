# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160120_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote_text', models.TextField(max_length=256, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0446\u0438\u0442\u0430\u0442\u0438')),
                ('quote_author', models.CharField(max_length=128, verbose_name='\u0410\u0432\u0442\u043e\u0440 \u0446\u0438\u0442\u0430\u0442\u0438')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
