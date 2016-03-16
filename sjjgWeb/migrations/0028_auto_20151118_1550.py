# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0027_auto_20151117_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='homeShow',
            field=models.TextField(default=b'\xe6\x9c\xaa\xe5\xa1\xab\xe5\x86\x99\xe5\x86\x85\xe5\xae\xb9', verbose_name=b'\xe4\xb8\xbb\xe9\xa1\xb5\xe6\x98\xbe\xe7\xa4\xba\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='coursemain',
            name='title',
            field=models.CharField(default=b'\xe6\x9c\xaa\xe5\xa1\xab\xe5\x86\x99\xe6\xa0\x87\xe9\xa2\x98', max_length=20, verbose_name=b'\xe9\x93\xbe\xe6\x8e\xa5\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='information',
            name='nav',
            field=models.CharField(unique=True, max_length=2, editable=False, choices=[('11', '\u8bfe\u7a0b\u4ecb\u7ecd'), ('12', '\u8bfe\u7a0b\u5927\u7eb2'), ('21', '\u56e2\u961f\u8d1f\u8d23\u4eba')]),
        ),
        migrations.AlterField(
            model_name='publishinformation',
            name='nav',
            field=models.CharField(unique=True, max_length=2, editable=False, choices=[('13', '\u8bfe\u7a0b\u5b9e\u9a8c'), ('33', '\u8bfe\u5916\u4f5c\u4e1a'), ('41', '\u6848\u4f8b\u5e93'), ('42', '\u4e13\u9898\u8bb2\u5ea7'), ('43', '\u8d44\u6e90\u6559\u6750'), ('52', '\u8bfe\u5916\u6d3b\u52a8'), ('62', '\u6559\u7814\u6559\u6539'), ('22', '\u6559\u5b66\u56e2\u961f')]),
        ),
    ]
