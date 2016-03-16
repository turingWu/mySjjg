# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0013_auto_20151114_1620'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nav',
            options={'verbose_name': '\u5bfc\u822a\u680f\u7ba1\u7406', 'verbose_name_plural': '\u5bfc\u822a\u680f\u7ba1\u7406'},
        ),
        migrations.AlterModelOptions(
            name='newimage',
            options={'verbose_name': '\u66f4\u591a\u5c55\u793a\u56fe\u7247', 'verbose_name_plural': '\u66f4\u591a\u5c55\u793a\u56fe\u7247'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': '\u559c\u8baf\u7ba1\u7406', 'verbose_name_plural': '\u559c\u8baf\u7ba1\u7406'},
        ),
        migrations.AlterModelOptions(
            name='recomment',
            options={'verbose_name': '\u4f60\u7684\u56de\u590d', 'verbose_name_plural': '\u4f60\u7684\u56de\u590d'},
        ),
        migrations.AlterModelOptions(
            name='testdata',
            options={'verbose_name': '\u8bd5\u9898\u5e93', 'verbose_name_plural': '\u8bd5\u9898\u5e93'},
        ),
        migrations.AlterModelOptions(
            name='tests',
            options={'verbose_name': '\u5728\u7ebf\u6d4b\u8bd5\u8bd5\u5377', 'verbose_name_plural': '\u5728\u7ebf\u6d4b\u8bd5\u8bd5\u5377'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '\u6240\u6709\u7528\u6237', 'verbose_name_plural': '\u6240\u6709\u7528\u6237'},
        ),
        migrations.AddField(
            model_name='news',
            name='publicTime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='cnav',
            name='navName',
            field=models.CharField(default=b'\xe6\x9c\xaa\xe5\xae\x9a\xe4\xb9\x89', unique=True, max_length=6, verbose_name=b'\xe5\xad\x90\xe5\xaf\xbc\xe8\x88\xaa\xe6\xa0\x8f\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='cnav',
            name='number',
            field=models.SmallIntegerField(verbose_name=b'\xe5\xad\x90\xe5\xaf\xbc\xe8\x88\xaa\xe6\xa0\x8f\xe7\xbc\x96\xe5\x8f\xb7', auto_created=True, choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6')]),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe8\x80\x85Id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='nav',
            name='father',
            field=models.SmallIntegerField(verbose_name=b'\xe4\xbb\x8e\xe5\xb1\x9e\xe4\xba\x8e\xe5\x93\xaa\xe4\xb8\xaa\xe4\xb8\xbb\xe5\xaf\xbc\xe8\x88\xaa\xe6\xa0\x8f', editable=False, choices=[(1, '\u8bfe\u7a0b\u4fe1\u606f'), (2, '\u6559\u5b66\u56e2\u961f'), (3, '\u6559\u5b66\u8d44\u6e90'), (4, '\u6269\u5c55\u8d44\u6e90'), (5, '\u8d44\u8baf\u4e2d\u5fc3'), (6, '\u6559\u7814\u6210\u679c')]),
        ),
        migrations.AlterField(
            model_name='newimage',
            name='url',
            field=models.ImageField(upload_to=b'./upload/new/', null=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe4\xbf\x9d\xe5\xad\x98\xe8\xb7\xaf\xe5\xbe\x84', blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='newContent',
            field=models.TextField(verbose_name=b'\xe4\xb8\xbb\xe9\xa2\x98\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='news',
            name='newSummary',
            field=models.CharField(max_length=200, verbose_name=b'\xe6\x91\x98\xe8\xa6\x81'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='testdata',
            name='content',
            field=models.FileField(upload_to=b'./upload/testData', verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe8\xaf\x95\xe9\xa2\x98\xe5\xba\x93'),
        ),
        migrations.AlterField(
            model_name='testdata',
            name='testsName',
            field=models.CharField(max_length=10, verbose_name=b'\xe8\xaf\x95\xe9\xa2\x98\xe5\x90\x8d\xe5\xad\x97'),
        ),
    ]
