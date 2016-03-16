# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0014_auto_20151114_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='newSummary',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xe6\x91\x98\xe8\xa6\x81', blank=True),
        ),
    ]
