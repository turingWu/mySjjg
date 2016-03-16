# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0007_auto_20151114_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='CNav',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.SmallIntegerField(verbose_name=b'\xe5\xaf\xbc\xe8\x88\xaa\xe6\xa0\x8f\xe7\xbc\x96\xe5\x8f\xb7', auto_created=True, choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6')])),
                ('navName', models.CharField(default=b'\xe6\x9c\xaa\xe5\xae\x9a\xe4\xb9\x89', max_length=6, verbose_name=b'\xe5\xaf\xbc\xe8\x88\xaa\xe6\xa0\x8f\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
        ),
        migrations.AlterModelOptions(
            name='nav',
            options={},
        ),
        migrations.AlterField(
            model_name='nav',
            name='father',
            field=models.SmallIntegerField(verbose_name=b'\xe4\xbb\x8e\xe5\xb1\x9e\xe4\xba\x8e\xe5\x93\xaa\xe4\xb8\xaa\xe4\xb8\xbb\xe5\xaf\xbc\xe8\x88\xaa\xe6\xa0\x8f', choices=[(1, '\u8bfe\u7a0b\u4fe1\u606f'), (2, '\u6559\u5b66\u56e2\u961f'), (3, '\u6559\u5b66\u8d44\u6e90'), (4, '\u6269\u5c55\u8d44\u6e90'), (5, '\u8d44\u8baf\u4e2d\u5fc3'), (6, '\u6559\u7814\u6210\u679c')]),
        ),
        migrations.AlterUniqueTogether(
            name='nav',
            unique_together=set([]),
        ),
        migrations.AddField(
            model_name='cnav',
            name='father',
            field=models.ForeignKey(to='sjjgWeb.Nav'),
        ),
        migrations.RemoveField(
            model_name='nav',
            name='navName',
        ),
        migrations.RemoveField(
            model_name='nav',
            name='number',
        ),
    ]
