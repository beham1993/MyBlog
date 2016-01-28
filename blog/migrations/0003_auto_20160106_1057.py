# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160106_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_of_article',
            field=models.DateField(),
        ),
    ]
