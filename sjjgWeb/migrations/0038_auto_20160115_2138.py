# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0037_auto_20151124_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadhomework',
            name='warningMess',
            field=models.CharField(default=b'\xe8\xaf\xb7\xe5\x8a\xa1\xe5\xbf\x85\xe8\xae\xa4\xe7\x9c\x9f\xe5\xae\x8c\xe6\x88\x90', max_length=500, verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe6\x8f\x90\xe4\xba\xa4\xe8\xa6\x81\xe6\xb1\x82'),
        ),
        migrations.AlterField(
            model_name='coursemain',
            name='is_publish',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xbb\xe9\xa1\xb5\xe6\x98\xbe\xe7\xa4\xba'),
        ),
        migrations.AlterField(
            model_name='coursepublish',
            name='nav',
            field=models.CharField(unique=True, max_length=2, verbose_name=b'\xe5\xaf\xb9\xe5\xba\x94\xe9\xa1\xb5\xe9\x9d\xa2\xe6\xa8\xa1\xe5\x9d\x97', choices=[('51', '\u8bfe\u7a0b\u516c\u544a'), ('52', '\u8bfe\u5916\u6d3b\u52a8'), ('61', '\u6559\u7814\u6210\u679c')]),
        ),
        migrations.AlterField(
            model_name='information',
            name='nav',
            field=models.CharField(unique=True, max_length=2, verbose_name=b'\xe5\xaf\xb9\xe5\xba\x94\xe9\xa1\xb5\xe9\x9d\xa2\xe6\xa8\xa1\xe5\x9d\x97', choices=[('11', '\u8bfe\u7a0b\u4ecb\u7ecd'), ('12', '\u8bfe\u7a0b\u5927\u7eb2'), ('21', '\u56e2\u961f\u8d1f\u8d23\u4eba'), ('14', '\u8bfe\u7a0b\u8bbe\u8ba1\u5927\u7eb2')]),
        ),
        migrations.AlterField(
            model_name='publishfile',
            name='nav',
            field=models.CharField(unique=True, max_length=2, verbose_name=b'\xe5\xaf\xb9\xe5\xba\x94\xe9\xa1\xb5\xe9\x9d\xa2\xe6\xa8\xa1\xe5\x9d\x97', choices=[('31', '\u6559\u5b66\u5f55\u50cf'), ('32', '\u6388\u8bfe\u6559\u6848')]),
        ),
        migrations.AlterField(
            model_name='publishinformation',
            name='nav',
            field=models.CharField(unique=True, max_length=2, verbose_name=b'\xe5\xaf\xb9\xe5\xba\x94\xe9\xa1\xb5\xe9\x9d\xa2\xe6\xa8\xa1\xe5\x9d\x97', choices=[('13', '\u8bfe\u7a0b\u5b9e\u9a8c'), ('33', '\u8bfe\u5916\u4f5c\u4e1a'), ('41', '\u6848\u4f8b\u5e93'), ('42', '\u4e13\u9898\u8bb2\u5ea7'), ('43', '\u8d44\u6e90\u6559\u6750'), ('62', '\u6559\u7814\u6559\u6539'), ('22', '\u6559\u5b66\u56e2\u961f')]),
        ),
    ]
