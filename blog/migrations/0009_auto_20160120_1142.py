# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160120_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleimage',
            name='article',
        ),
        migrations.DeleteModel(
            name='ArticleImage',
        ),
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(upload_to=b'images/', verbose_name='\u0424\u043e\u0442\u043e \u0434\u043e \u0441\u0442\u0430\u0442\u0442\u0456'),
        ),
    ]
