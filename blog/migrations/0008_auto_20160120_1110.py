# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_article_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'../assets/images', verbose_name='\u0424\u043e\u0442\u043e \u0434\u043e \u0441\u0442\u0430\u0442\u0442\u0456')),
                ('article', models.ForeignKey(related_name=b'images', to='blog.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(upload_to=b'../assets/images', verbose_name='\u0424\u043e\u0442\u043e \u0434\u043e \u0441\u0442\u0430\u0442\u0442\u0456'),
        ),
    ]
