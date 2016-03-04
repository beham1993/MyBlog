# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_quote'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date_of_article']},
        ),
        migrations.AddField(
            model_name='quote',
            name='author_url',
            field=models.URLField(default=b'vk.com', verbose_name='\u0421\u0442\u0430\u0442\u0442\u044f \u043f\u0440\u043e \u0430\u0432\u0442\u043e\u0440\u0430'),
            preserve_default=True,
        ),
    ]
