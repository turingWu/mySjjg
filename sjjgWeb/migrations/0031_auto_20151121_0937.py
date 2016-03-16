# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0030_auto_20151120_2027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tests',
            options={'ordering': ['-num'], 'verbose_name': '\u5728\u7ebf\u6d4b\u8bd5\u8bd5\u5377', 'verbose_name_plural': '\u5728\u7ebf\u6d4b\u8bd5\u8bd5\u5377'},
        ),
        migrations.AddField(
            model_name='tests',
            name='testName',
            field=models.CharField(default=b'\xe8\xaf\x95\xe5\x8d\xb7', max_length=30, verbose_name=b'\xe8\xaf\x95\xe5\x8d\xb7\xe4\xbb\x8b\xe7\xbb\x8d'),
        ),
        migrations.AlterField(
            model_name='coursepublish',
            name='nav',
            field=models.CharField(unique=True, max_length=2, editable=False, choices=[('51', '\u8bfe\u7a0b\u516c\u544a'), ('52', '\u8bfe\u5916\u6d3b\u52a8'), ('61', '\u6559\u7814\u6210\u679c')]),
        ),
    ]
