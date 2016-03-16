# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0035_auto_20151124_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filecontent',
            name='url',
            field=models.URLField(null=True, verbose_name=b'\xe4\xbc\x98\xe9\x85\xb7\xe9\x93\xbe\xe6\x8e\xa5', blank=True),
        ),
    ]
