# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0025_auto_20151117_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='publishinformation',
            name='title',
            field=models.CharField(default=b'\xe6\xb2\xa1\xe5\x86\x99\xe6\xa0\x87\xe9\xa2\x98', unique=True, max_length=20, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98\xe9\x93\xbe\xe6\x8e\xa5'),
        ),
        migrations.AlterField(
            model_name='coursepublish',
            name='nav',
            field=models.CharField(unique=True, max_length=2, editable=False, choices=[('51', '\u8bfe\u7a0b\u516c\u544a'), ('61', '\u6559\u7814\u6210\u679c')]),
        ),
        migrations.AlterField(
            model_name='information',
            name='nav',
            field=models.CharField(unique=True, max_length=2, editable=False, choices=[('11', '\u8bfe\u7a0b\u4ecb\u7ecd'), ('12', '\u8bfe\u7a0b\u5927\u7eb2'), ('21', '\u56e2\u961f\u8d1f\u8d23\u4eba'), ('22', '\u6559\u5b66\u56e2\u961f')]),
        ),
        migrations.AlterField(
            model_name='publishfile',
            name='nav',
            field=models.CharField(unique=True, max_length=2, editable=False, choices=[('31', '\u6559\u5b66\u5f55\u50cf'), ('32', '\u6388\u8bfe\u6559\u6848')]),
        ),
        migrations.AlterField(
            model_name='publishinformation',
            name='nav',
            field=models.CharField(unique=True, max_length=2, editable=False, choices=[('13', '\u8bfe\u7a0b\u5b9e\u9a8c'), ('33', '\u8bfe\u5916\u4f5c\u4e1a'), ('41', '\u6848\u4f8b\u5e93'), ('42', '\u4e13\u9898\u8bb2\u5ea7'), ('43', '\u8d44\u6e90\u6559\u6750'), ('52', '\u8bfe\u5916\u6d3b\u52a8'), ('62', '\u6559\u7814\u6559\u6539')]),
        ),
    ]
