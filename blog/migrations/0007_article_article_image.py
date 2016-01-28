# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default=b'../assets/images/pic01.jpg', height_field=340, width_field=800, upload_to=b'../assets/images', verbose_name='\u0424\u043e\u0442\u043e \u0434\u043e \u0441\u0442\u0430\u0442\u0442\u0456'),
            preserve_default=True,
        ),
    ]
