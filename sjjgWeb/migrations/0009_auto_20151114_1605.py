# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0008_auto_20151114_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(max_length=500, verbose_name=b'\xe4\xbd\xa0\xe7\x9a\x84\xe5\x9b\x9e\xe5\xa4\x8d')),
            ],
        ),
        migrations.AlterModelOptions(
            name='cnav',
            options={'verbose_name': '\u5b50\u5bfc\u822a\u680f', 'verbose_name_plural': '\u5b50\u5bfc\u822a\u680f'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '\u7559\u8a00\u7ba1\u7406', 'verbose_name_plural': '\u7559\u8a00\u7ba1\u7406'},
        ),
        migrations.AlterModelOptions(
            name='nav',
            options={'verbose_name': '\u5bfc\u822a\u680f', 'verbose_name_plural': '\u5bfc\u822a\u680f'},
        ),
        migrations.AlterModelOptions(
            name='score',
            options={'verbose_name': '\u5b66\u751f\u5206\u6570', 'verbose_name_plural': '\u5b66\u751f\u5206\u6570'},
        ),
        migrations.AlterModelOptions(
            name='showtable',
            options={'verbose_name': '\u6559\u7814\u6210\u679c\u5c55\u793a', 'verbose_name_plural': '\u6559\u7814\u6210\u679c\u5c55\u793a'},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='commentTo',
        ),
        migrations.AlterField(
            model_name='cnav',
            name='navName',
            field=models.CharField(default=b'\xe6\x9c\xaa\xe5\xae\x9a\xe4\xb9\x89', unique=True, max_length=6, verbose_name=b'\xe5\xaf\xbc\xe8\x88\xaa\xe6\xa0\x8f\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=500, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='uploadhomework',
            name='content',
            field=models.FileField(upload_to=b'./upload/homework', verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe6\x96\x87\xe4\xbb\xb6'),
        ),
        migrations.AlterUniqueTogether(
            name='cnav',
            unique_together=set([('father', 'number')]),
        ),
    ]
