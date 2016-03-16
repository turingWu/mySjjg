# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0018_remove_news_newcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='mainContent2',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=b'1'),
        ),
    ]
