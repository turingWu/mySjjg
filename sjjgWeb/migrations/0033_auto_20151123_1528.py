# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0032_auto_20151123_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReFell',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('connect', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-commentDate'], 'verbose_name': '\u7559\u8a00\u7ba1\u7406', 'verbose_name_plural': '\u7559\u8a00\u7ba1\u7406'},
        ),
    ]
