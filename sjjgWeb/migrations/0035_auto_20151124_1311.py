# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0034_auto_20151124_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publishfile',
            name='url',
        ),
        migrations.AddField(
            model_name='filecontent',
            name='url',
            field=models.URLField(default=b'\xe6\x9c\xaa\xe5\xa1\xab\xe5\x86\x99', verbose_name=b'\xe4\xbc\x98\xe9\x85\xb7\xe9\x93\xbe\xe6\x8e\xa5'),
        ),
    ]
