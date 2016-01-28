# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160106_1057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['date_of_article']},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='head',
            new_name='head_uk',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='sub_head',
            new_name='sub_head_uk',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='text_article',
            new_name='text_article_uk',
        ),
        migrations.AddField(
            model_name='article',
            name='head_en',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='sub_head_en',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='text_article_en',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
