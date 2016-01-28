# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160107_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_of_article',
            field=models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0456\u043a\u0430\u0446\u0456\u0457'),
        ),
        migrations.AlterField(
            model_name='article',
            name='head_en',
            field=models.CharField(max_length=128, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='head_uk',
            field=models.CharField(max_length=128, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
        migrations.AlterField(
            model_name='article',
            name='sub_head_en',
            field=models.CharField(max_length=128, null=True, verbose_name='\u041f\u0456\u0434\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='sub_head_uk',
            field=models.CharField(max_length=128, verbose_name='\u041f\u0456\u0434\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text_article_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0441\u0442\u0430\u0442\u0442\u0456', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='text_article_uk',
            field=ckeditor.fields.RichTextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0441\u0442\u0430\u0442\u0442\u0456'),
        ),
    ]
