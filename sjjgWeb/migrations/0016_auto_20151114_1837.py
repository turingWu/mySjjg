# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0015_auto_20151114_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showtable',
            name='image',
        ),
        migrations.AddField(
            model_name='news',
            name='mainContent',
            field=ckeditor.fields.RichTextField(default=b'1'),
        ),
        migrations.AddField(
            model_name='showtable',
            name='content',
            field=ckeditor.fields.RichTextField(default=b'1'),
        ),
        migrations.AlterField(
            model_name='news',
            name='titleImage',
            field=models.ImageField(upload_to=b'./upload/main', verbose_name=b'\xe4\xb8\xbb\xe8\xa6\x81\xe5\xb1\x95\xe7\xa4\xba\xe5\x9b\xbe\xe7\x89\x87'),
        ),
    ]
