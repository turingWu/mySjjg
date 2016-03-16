# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0023_auto_20151115_1718'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cnav',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='cnav',
            name='father',
        ),
        migrations.RemoveField(
            model_name='newimage',
            name='new',
        ),
        migrations.DeleteModel(
            name='ShowTable',
        ),
        migrations.RemoveField(
            model_name='tests',
            name='max_score',
        ),
        migrations.AddField(
            model_name='tests',
            name='bool_score',
            field=models.SmallIntegerField(default=3, verbose_name=b'\xe6\xaf\x8f\xe9\x81\x93\xe5\x88\xa4\xe6\x96\xad\xe9\xa2\x98\xe5\x88\x86\xe5\x80\xbc'),
        ),
        migrations.AddField(
            model_name='tests',
            name='choice_score',
            field=models.SmallIntegerField(default=3, verbose_name=b'\xe9\x80\x89\xe6\x8b\xa9\xe9\xa2\x98\xe5\x88\x86\xe5\x80\xbc'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': '\u7528\u6237\u540d\u5df2\u7ecf\u5b58\u5728'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username'),
        ),
        migrations.DeleteModel(
            name='CNav',
        ),
        migrations.DeleteModel(
            name='Nav',
        ),
        migrations.DeleteModel(
            name='NewImage',
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
