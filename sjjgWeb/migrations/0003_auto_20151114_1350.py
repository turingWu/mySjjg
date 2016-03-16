# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0002_auto_20151114_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='nav',
            name='navName',
            field=models.CharField(default=b'\xe6\x9c\xaa\xe5\xae\x9a\xe4\xb9\x89', max_length=6),
        ),
        migrations.AlterField(
            model_name='nav',
            name='father',
            field=models.SmallIntegerField(choices=[(1, b'\xe8\xaf\xbe\xe7\xa8\x8b\xe4\xbf\xa1\xe6\x81\xaf'), (2, b'\xe6\x95\x99\xe5\xad\xa6\xe5\x9b\xa2\xe9\x98\x9f'), (3, b'\xe6\x95\x99\xe5\xad\xa6\xe8\xb5\x84\xe6\xba\x90'), (4, b'\xe6\x89\xa9\xe5\xb1\x95\xe8\xb5\x84\xe6\xba\x90'), (5, b'\xe8\xb5\x84\xe8\xae\xaf\xe4\xb8\xad\xe5\xbf\x83'), (6, b'\xe6\x95\x99\xe7\xa0\x94\xe6\x88\x90\xe6\x9e\x9c')]),
        ),
    ]
