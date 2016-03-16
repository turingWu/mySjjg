# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0033_auto_20151123_1528'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='refell',
            options={'verbose_name': '\u5185\u5bb9\u53cd\u9988', 'verbose_name_plural': '\u5185\u5bb9\u53cd\u9988'},
        ),
        migrations.AddField(
            model_name='publishfile',
            name='url',
            field=models.URLField(default=b'\xe6\x9c\xaa\xe5\xa1\xab\xe5\x86\x99', verbose_name=b'\xe4\xbc\x98\xe9\x85\xb7\xe9\x93\xbe\xe6\x8e\xa5'),
        ),
        migrations.AlterField(
            model_name='refell',
            name='connect',
            field=models.CharField(max_length=30, verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe8\x81\x94\xe7\xb3\xbb\xe6\x96\xb9\xe5\xbc\x8f'),
        ),
        migrations.AlterField(
            model_name='refell',
            name='content',
            field=models.TextField(verbose_name=b'\xe5\x8f\x8d\xe9\xa6\x88\xe5\x86\x85\xe5\xae\xb9'),
        ),
    ]
