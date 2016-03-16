# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0006_auto_20151114_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nav',
            name='number',
            field=models.SmallIntegerField(verbose_name=b'\xe5\xaf\xbc\xe8\x88\xaa\xe6\xa0\x8f\xe7\xbc\x96\xe5\x8f\xb7', auto_created=True, choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6')]),
        ),
    ]
