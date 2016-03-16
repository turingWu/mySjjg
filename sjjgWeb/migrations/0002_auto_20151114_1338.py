# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer_question',
            options={'verbose_name': '\u95ee\u7b54\u9898', 'verbose_name_plural': '\u95ee\u7b54\u9898'},
        ),
        migrations.AlterModelOptions(
            name='bool_question',
            options={'verbose_name': '\u5224\u65ad\u9898', 'verbose_name_plural': '\u5224\u65ad\u9898'},
        ),
        migrations.AlterModelOptions(
            name='choice_question',
            options={'verbose_name': '\u9009\u62e9\u9898', 'verbose_name_plural': '\u9009\u62e9\u9898'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '\u5b66\u751f', 'verbose_name_plural': '\u5b66\u751f'},
        ),
        migrations.AlterModelOptions(
            name='tests',
            options={'verbose_name': '\u8bd5\u5377', 'verbose_name_plural': '\u8bd5\u5377'},
        ),
        migrations.AlterModelOptions(
            name='uploadhomework',
            options={'verbose_name': '\u4f5c\u4e1a\u4e0a\u4f20', 'verbose_name_plural': '\u4f5c\u4e1a\u4e0a\u4f20'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '\u7279\u6b8a\u7528\u6237', 'verbose_name_plural': '\u7279\u6b8a\u7528\u6237'},
        ),
        migrations.AlterField(
            model_name='bool_question',
            name='correct',
            field=models.BooleanField(default=True, verbose_name=b'\xe6\xad\xa3\xe7\xa1\xae\xe7\xad\x94\xe6\xa1\x88', choices=[(True, b'\xe6\xad\xa3\xe7\xa1\xae'), (False, b'\xe9\x94\x99\xe8\xaf\xaf')]),
        ),
    ]
