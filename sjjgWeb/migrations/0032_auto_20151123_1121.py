# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0031_auto_20151121_0937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer_question',
            options={'ordering': ['num'], 'verbose_name': '\u95ee\u7b54\u9898', 'verbose_name_plural': '\u95ee\u7b54\u9898'},
        ),
        migrations.AlterModelOptions(
            name='bool_question',
            options={'ordering': ['num'], 'verbose_name': '\u5224\u65ad\u9898', 'verbose_name_plural': '\u5224\u65ad\u9898'},
        ),
        migrations.AlterModelOptions(
            name='choice_question',
            options={'ordering': ['num'], 'verbose_name': '\u9009\u62e9\u9898', 'verbose_name_plural': '\u9009\u62e9\u9898'},
        ),
        migrations.AddField(
            model_name='comment',
            name='commentDate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='score',
            name='student',
            field=models.ForeignKey(related_name='sscore_set', to='sjjgWeb.Student'),
        ),
    ]
