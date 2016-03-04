# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20160304_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='quote_author',
            new_name='quote_author_uk',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='quote_text',
            new_name='quote_text_uk',
        ),
        migrations.AddField(
            model_name='quote',
            name='quote_author_en',
            field=models.CharField(max_length=128, null=True, verbose_name='\u0410\u0432\u0442\u043e\u0440 \u0446\u0438\u0442\u0430\u0442\u0438', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='quote',
            name='quote_text_en',
            field=models.TextField(max_length=256, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0446\u0438\u0442\u0430\u0442\u0438', blank=True),
            preserve_default=True,
        ),
    ]
