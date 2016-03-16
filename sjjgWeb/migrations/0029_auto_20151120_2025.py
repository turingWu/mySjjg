# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0028_auto_20151118_1550'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursemain',
            options={'ordering': ['-publishDate'], 'verbose_name': '\u5185\u5bb9\u53d1\u5e03', 'verbose_name_plural': '\u5185\u5bb9\u53d1\u5e03'},
        ),
        migrations.AddField(
            model_name='coursemain',
            name='publishDate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='coursepublish',
            name='nav',
            field=models.CharField(unique=True, max_length=2, choices=[('51', '\u8bfe\u7a0b\u516c\u544a'), ('52', '\u8bfe\u5916\u6d3b\u52a8'), ('61', '\u6559\u7814\u6210\u679c')]),
        ),
        migrations.AlterField(
            model_name='filecontent',
            name='files',
            field=models.FileField(upload_to=b'file'),
        ),
        migrations.AlterField(
            model_name='information',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name=b'\xe9\xa1\xb5\xe9\x9d\xa2\xe6\x98\xbe\xe7\xa4\xba\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='publishinformation',
            name='nav',
            field=models.CharField(unique=True, max_length=2, editable=False, choices=[('13', '\u8bfe\u7a0b\u5b9e\u9a8c'), ('33', '\u8bfe\u5916\u4f5c\u4e1a'), ('41', '\u6848\u4f8b\u5e93'), ('42', '\u4e13\u9898\u8bb2\u5ea7'), ('43', '\u8d44\u6e90\u6559\u6750'), ('62', '\u6559\u7814\u6559\u6539'), ('22', '\u6559\u5b66\u56e2\u961f')]),
        ),
    ]
