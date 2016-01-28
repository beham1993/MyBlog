# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160107_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name="\u0406\u043c'\u044f")),
                ('birthday_date', models.DateField(verbose_name='\u0414\u0435\u043d\u044c \u043d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f')),
                ('location', models.CharField(max_length=64, verbose_name='\u041c\u0456\u0441\u0442\u043e')),
                ('email', models.EmailField(max_length=64, verbose_name='\u0415\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430 \u043f\u043e\u0448\u0442\u0430')),
                ('skype', models.CharField(max_length=64, verbose_name='\u0421\u043a\u0430\u0439\u043f')),
                ('vk', models.CharField(max_length=64, verbose_name='\u0412\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u0456')),
                ('facebook', models.CharField(max_length=64, verbose_name='\u0424\u0435\u0439\u0441\u0431\u0443\u043a')),
                ('bio', ckeditor.fields.RichTextField(verbose_name='\u041f\u0440\u043e \u0441\u0435\u0431\u0435')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
