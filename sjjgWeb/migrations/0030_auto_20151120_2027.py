# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0029_auto_20151120_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemain',
            name='title',
            field=models.CharField(default=b'\xe6\x9c\xaa\xe5\xa1\xab\xe5\x86\x99\xe6\xa0\x87\xe9\xa2\x98', max_length=30, verbose_name=b'\xe9\x93\xbe\xe6\x8e\xa5\xe6\xa0\x87\xe9\xa2\x98'),
        ),
    ]
